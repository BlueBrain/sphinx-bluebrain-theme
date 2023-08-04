#!/usr/bin/env python
"""Check for regresssions of building simple docs."""

import json
from pathlib import Path
import sys


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

    def find_differing_offset(l0, l1):
        for i in range(min(len(l0), len(l1))):
            if l0[i] != l1[i]:
                return i
        assert False, "Should never get here"

    expected = Path("tests/data/regression.html")
    new = Path("doc/build/html/regression.html")

    with expected.open(encoding="utf8") as fd:
        expected_lines = fd.readlines()

    with new.open(encoding="utf8") as fd:
        new_lines = fd.readlines()

    for i, (expected_line, new_line) in enumerate(zip(expected_lines, new_lines)):
        expected_line, new_line = expected_line.strip(), new_line.strip()
        if expected_line == new_line:
            continue

        start = find_differing_offset(expected_line, new_line)
        quote = new_line[start:].find('"')
        if quote != -1 and int(new_line[start : start + quote], 16):
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
