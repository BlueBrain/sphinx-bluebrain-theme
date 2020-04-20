"""This module contains the classes used to build the search_index.json file for lunr search.

See https://github.com/mkdocs/mkdocs/blob/master/mkdocs/contrib/search/search_index.py
which shows the expected structure of the JSON search index and the
approach used by mkdocs to generate it
"""

import re
from json import dumps

try:
    from html.parser import HTMLParser
except ImportError:
    from HTMLParser import HTMLParser


class IndexEntry:
    """Holds the data for each entry in the search index."""

    MULTI_SPACE_REGEX = re.compile(r"\s+")

    def __init__(self, location="", title=""):
        """Initialize the index entry."""
        self.location = location
        self.title = title
        self.text_list = []

    @property
    def text(self):
        """Generates the search index text for on an entry.

        Generates the joined and cleaned text for the entry from the list
        of text found in the page/section of the entry.
        """
        text = "\n".join(self.text_list)
        text = text.replace(u"\u00B6", " ")  # remove the pilcrow symbol
        text = self.MULTI_SPACE_REGEX.sub(" ", text).strip()

        return text

    def as_dict(self):
        """Returns a dict containing the data required for the search index, used by json.dumps."""
        return {k: getattr(self, k) for k in ("location", "title", "text")}


# pylint: disable=abstract-method
class SearchIndexBuilder(HTMLParser):
    """Class is used to generate the search_index.json file.

    It is intended to hold all the data required and then be dumped
    into a jinja templated file using __repr__.
    """

    HEADING_TAGS = {"h" + str(i) for i in range(1, 7)}

    def __init__(self):
        """Initialize the parser and additional attributes."""
        HTMLParser.__init__(self)
        self._entries = []
        self._current_page = None
        self._current_section = None
        self._current_section_id = None
        self._current_section_id = None
        self._is_heading = False

    def add_page_to_index(self, page):
        """Adds a single page to the search index.

        This takes care of creating the entry for the complete page as well as splitting it into
        each section.
        """
        # the path needs to move to the parent directory as the index is
        # stored in the _static directory
        self._current_page = IndexEntry("../" + page.url, page.title)
        self._entries.append(self._current_page)

        contents = page.content or ""
        self.feed(contents)

    def __repr__(self):
        """Returns the dumped json as the repr for the entry.

        The dumped json is used for the search index build.
        """
        return dumps(
            {"docs": [e.as_dict() for e in self._entries], "config": {}}, sort_keys=True
        )

    def handle_starttag(self, tag, attrs):
        """Handles the possible HTML tags as required for building the index."""
        attrsdict = dict(attrs)

        # sphinx puts each section inside a div which actually has the
        # id for the section. this is changed with JS for the final
        # page rendering, but at this point we need to get the id
        # from the enclosing div.
        if tag == "div" and "section" in attrsdict.get("class", ""):
            self._current_section_id = attrsdict.get("id", None)
            return

        if tag in self.HEADING_TAGS and self._current_section_id is not None:
            # add the anchor for the section to the page url
            section_location = "#".join(
                (self._current_page.location, self._current_section_id)
            )
            self._current_section = IndexEntry(section_location)
            self._entries.append(self._current_section)
            self._is_heading = True
            self._current_section_id = None
        else:
            self._is_heading = False

    def handle_endtag(self, tag):
        """Handles closing tags, particularly headings."""
        if tag in self.HEADING_TAGS and self._current_section_id is not None:
            self._is_heading = False
            self._current_section_id = None

    def handle_data(self, data):
        """Handles appending data to the correct place (heading or section)."""
        # always add the data to the complete page entry
        self._current_page.text_list.append(data)

        if self._is_heading:
            self._current_section.title = data
        elif self._current_section is not None:
            self._current_section.text_list.append(data)
