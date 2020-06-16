"""This module will translate the mkdocs material theme to a Sphinx theme."""

from pathlib import Path

from distutils import dir_util  # pylint: disable= no-name-in-module

from mkdocs2sphinx import copy_source, convert_files


def _ignore_on_copy(directory, contents):  # pylint: disable=unused-argument
    """Provides list of items to be ignored.

    Args:
        directory (Path): The path to the current directory.
        contents (list): A list of files in the current directory.

    Returns:
        list: A list of files to be ignored.
    """
    # shutil passes strings, so ensure a Path
    directory = Path(directory)
    if directory.name == "material":
        return ["mkdocs_theme.yml", "main.html", "404.html"]

    if directory.name == "partials":
        return ["integrations"]

    if directory.name == "images":
        return ["favicon.png"]

    return []


if __name__ == "__main__":
    # set some paths
    PWD_PATH = Path(__file__).parent

    # this assumes that the mkdocs material theme is in the same directory
    # as this file's parent directory
    SRC_PATH = PWD_PATH / "mkdocs-material" / "material"
    OUT_PATH = PWD_PATH / "sphinx_bluebrain_theme"
    copy_source(SRC_PATH, OUT_PATH, _ignore_on_copy)

    # convert files from mkdocs to Sphinx
    BLOCK_LIST = ("source", "disqus", "analytics")
    REPLACEMENT_MAP = {
        # do general replacements
        '{% include "assets/': '{% include "static/'
    }

    # ensure mkdocs-material licenses are included
    LICENSE_PATH = PWD_PATH / "mkdocs-material" / "LICENSE"
    LICENSE_TEXT = LICENSE_PATH.read_text().splitlines()
    FILES_NOT_NEEDING_LICENSE = {
        "font-awesome.css",  # license information already included
        "material-icons.css",  # license information already included
    }

    STATS = convert_files(
        OUT_PATH, BLOCK_LIST, REPLACEMENT_MAP, LICENSE_TEXT, FILES_NOT_NEEDING_LICENSE
    )

    # show all replacement rules
    print("Replacement rules running, see below for details:")
    print("[replaced string]: [number of occurrences]")
    for k, v in STATS.items():
        colour = "\033[31m" if v == 0 else "\033[32m"
        end_colour = "\033[0m"
        print("{0}{1}: {2}{3}".format(colour, k, v, end_colour))

    # copy some additional files into the theme
    # copy_tree requires strings not paths, we use it here
    # as it allows directories to be merged (shutil.copytree does not)
    dir_util.copy_tree(str(PWD_PATH / "src"), str(OUT_PATH))

    # sphinx expects a 'static' directory so rename the mkdocs-material one
    (OUT_PATH / "assets").rename(OUT_PATH / "static")
