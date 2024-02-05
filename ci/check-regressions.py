#!/usr/bin/env python
"""Check for regressions of building simple docs."""

import itertools
import json
import re
import sys
from pathlib import Path

import sphinx


def _get_expected_path():
    if sphinx.version_info < (7, 2):
        # sphinx 7.2.0 dropped Python 3.8 support
        return Path("tests/data/regression_sphinx_7.1.html")
    return Path("tests/data/regression.html")


def check_empty_search_index_json():
    """Ibid."""
    path = Path("doc/build/html/_static/search/search_index.json")
    if not path.exists():
        print(f"{path} does not exist")
        return False
    with path.open(encoding="utf8") as fd:
        try:
            json.load(fd)
        except json.JSONDecodeError:
            print(f"Could not decode json for {path}")
            raise
    return True


def diff_contents():
    """Check the contents to see if they match.

    Note: We have to do this manually so we can ignore certain changes, like
    the cache busting appends that are done for static files
    """
    pattern = re.compile(r"\?v=[0-9A-Fa-f]*")

    expected = _get_expected_path()
    new = Path("doc/build/html/regression.html")

    with expected.open(encoding="utf8") as fd:
        expected_lines = fd.readlines()

    with new.open(encoding="utf8") as fd:
        new_lines = fd.readlines()

    for i, (expected_line, new_line) in enumerate(
        itertools.zip_longest(expected_lines, new_lines)
    ):
        expected_line, new_line = expected_line.strip(), new_line.strip()
        if expected_line == new_line:
            continue

        if pattern.sub("", new_line) == pattern.sub("", expected_line):
            continue

        print(f"on line {i}, `{expected_line}` != `{new_line}`")
        return False

    return True


if __name__ == "__main__":
    ret = True
    for fn in (
        check_empty_search_index_json,
        diff_contents,
    ):
        ret = fn() and ret
    if not ret:
        sys.exit(-1)
