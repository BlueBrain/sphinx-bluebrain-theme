"""This module will translate the mkdocs material theme to a Sphinx theme."""

import os
import os.path as osp

from distutils import dir_util  # pylint: disable= no-name-in-module

from mkdocs2sphinx import copy_source, convert_files


def _ignore_on_copy(directory, contents):  # pylint: disable=unused-argument
    """Provides list of items to be ignored.

    Args:
        directory (str): The path to the current directory.
        contents (list): A list of files in the current directory.

    Returns:
        list: A list of files to be ignored.
    """
    if directory.endswith(osp.join("", "material")):
        return ["mkdocs_theme.yml", "main.html", "404.html"]

    if directory.endswith(osp.join("", "partials")):
        return ["integrations"]

    if directory.endswith(osp.join("", "images")):
        return ["favicon.png"]

    return []


if __name__ == "__main__":
    # set some paths
    PWD_PATH = osp.dirname(osp.abspath(__file__))

    # this assumes that the mkdocs material theme is in the same directory
    # as this file's parent directory
    SRC_PATH = osp.join(PWD_PATH, "mkdocs-material", "material")
    OUT_PATH = osp.join(PWD_PATH, "sphinx_bluebrain_theme")
    copy_source(SRC_PATH, OUT_PATH, _ignore_on_copy)

    # convert files from mkdocs to Sphinx
    BLOCK_LIST = ("source", "disqus", "analytics")
    REPLACEMENT_MAP = {
        # do general replacements
        '{% include "assets/': '{% include "static/'
    }
    LICENSE_TEXT = (
        "Copyright (c) 2016-2019 Martin Donath <martin.donath@squidfunk.com>",
        "",
        "Permission is hereby granted, free of charge, to any person obtaining a copy",
        'of this software and associated documentation files (the "Software"), to',
        "deal in the Software without restriction, including without limitation the",
        "rights to use, copy, modify, merge, publish, distribute, sublicense, and/or",
        "sell copies of the Software, and to permit persons to whom the Software is",
        "furnished to do so, subject to the following conditions:",
        "",
        "The above copyright notice and this permission notice shall be included in",
        "all copies or substantial portions of the Software.",
        "",
        'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR',
        "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,",
        "FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE",
        "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER",
        "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING",
        "FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS",
        "IN THE SOFTWARE.",
    )
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
    dir_util.copy_tree(osp.join(PWD_PATH, "src"), OUT_PATH)

    # sphinx expects a 'static' directory so rename the mkdocs-material one
    os.rename(osp.join(OUT_PATH, "assets"), osp.join(OUT_PATH, "static"))
