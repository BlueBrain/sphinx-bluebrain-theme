"""Utilities for the translation of file contents from mkdocs-material to Sphinx."""

import io
import os
import re
import shutil
from collections import defaultdict

from mkdocs2sphinx.clear_blocks import remove_blocks


def copy_source(source_path, output_path, ignore_on_copy):
    """Copies a directory from one location to another, removing existing if necessary.

    Args:
        source_path (str): A path to the directory to be copied.
        output_path (str): A path to the directory where the source will be copied.
        ignore_on_copy (callable): A callable returning the names of files
            or directories to be ignored during the copy.
    """
    if os.path.isdir(output_path):
        shutil.rmtree(output_path)

    shutil.copytree(source_path, output_path, ignore=ignore_on_copy)


def do_replacements(src_text, replacement_map, stats):
    """Replace some mkdocs specific information with Sphinx equivalent.

    Args:
        src_text (str): The text in which targets will be replaced.
        replacement_map (dict): A dictionary containing strings or compiled
            regexs to find (the keys) and the strings (or functions for regexs)
            to replace them with (the values).
        stats (collections.defaultdict): A dictionary for storing the number of times a
            particular replacement occurred.

    Returns:
        str: The results of all replacements.
    """
    for fnd, rep in replacement_map.items():
        if isinstance(fnd, re._pattern_type):  # pylint: disable=protected-access
            stats[fnd] += len(re.findall(fnd, src_text))
            src_text = re.sub(fnd, rep, src_text)
        elif isinstance(fnd, str):
            count_pre = src_text.count(fnd)
            # this is fragile since it relies on *exact* matches
            src_text = src_text.replace(fnd, rep)
            stats[fnd] += count_pre

    return src_text


def prepend_license(license_text, src_text, filename):
    """Prepend a license notice to the file commented out based on the extension.

    Args:
        src_text (str): The text which will have the license prepended.
        filename (str): The name of the file including extension.

    Returns:
        str: The full text of the prepended file.
    """
    # opening, new line prepend, closing
    comment_symbols = {
        ".css": ("/*", " * ", " */"),
        ".html": ("<!--", "  ", "-->"),
        ".js": ("/*", " * ", " */"),
    }

    # get the file extension
    _, ext = os.path.splitext(filename)
    ext = ext.lower()

    if ext not in comment_symbols:
        return src_text

    com = comment_symbols[ext]

    lic = "\n".join(("".join((com[1], l)) for l in license_text))
    lic = "\n".join((com[0], lic, com[2]))

    if ext == ".html":
        lic = "\n".join(("{#", lic, "#}"))

    src_text = "\n".join((lic, src_text))

    return src_text


def convert_files(path, block_list, replacement_map, license_text, files_no_license):
    """Converts the files contained within the path given to be compatible with Sphinx.

    Args:
        path (str): The path to the directory containing files to be converted.
        block_list (list): A list of block names which will be cleared.
        replacement_map (dict): A dictionary containing strings to find
            (the keys) and the strings to replace them with (the values).
        files_no_license (set): A set of file names which do not require
            the mkdocs-material license to be prepended.

    Returns:
        dict: A dictionary storing the number of replacements which have been done.
    """
    stats = defaultdict(int)

    for root, dirs, files in os.walk(path):  # pylint: disable=unused-variable
        for fl in files:
            # get the file extension
            _, ext = os.path.splitext(fl)
            ext = ext.lower()

            # only converting HTML files at the moment
            if ext not in {".html", ".css", ".js"} and not ext.endswith("_t"):
                continue

            # we need to read and then write back to this file
            with io.open(os.path.join(root, fl), "r+", encoding="utf-8") as write_file:
                file_contents = write_file.read()
                file_contents = remove_blocks(file_contents, block_list)
                file_contents = do_replacements(file_contents, replacement_map, stats)

                if fl not in files_no_license:
                    file_contents = prepend_license(license_text, file_contents, fl)

                # reset to start of file, write, and then truncate
                write_file.seek(0)
                write_file.write(file_contents)
                write_file.truncate()

    return stats
