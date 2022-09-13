"""
Test for search index builder which is required for lunr
search used by mkdocs-material.
"""

import pytest  # pylint: disable=unused-import
from sphinx_bluebrain_theme.utils import search_builder


def test_index_entry():
    """
    Test the construction of the list of blocks from text.
    """
    text_list = ("Line one \u00B6.", "Line two.   ")
    entry = search_builder.IndexEntry()
    entry.text_list.extend(text_list)

    text = """Line one . Line two."""

    assert text == entry.text


def test_index_as_dict():
    """
    Test the returned dictionary representation.
    """
    text_list = ("Line one \u00B6.", "Line two.   ")
    entry = search_builder.IndexEntry(location="/", title="test")
    entry.text_list.extend(text_list)

    as_dict = {"location": "/", "title": "test", "text": """Line one . Line two."""}

    assert as_dict == entry.as_dict()
