"""Classes and functions used to convert Sphinx generated Tables of Contents.

The original theme was built for mkdocs and so expects mkdocs classes to be
provided to templates for rendering. These classes do the job of converting
the HTML table of contents generated by Sphinx into a format compatible
with the theme.

mkdocs ToC HTML parser is built for their specific markdown output. See here:
- https://github.com/mkdocs/mkdocs/blob/master/mkdocs/structure/toc.py
"""

try:
    from html.parser import HTMLParser
except ImportError:
    from HTMLParser import HTMLParser

from sphinx_bluebrain_theme.utils.navutils import Nav, Page


# pylint: disable=abstract-method
class TocHTMLParser(HTMLParser):
    """Customised Sphinx Table of Contents HTML parser.

    This parser will construct the table of contents from the HTML produced by Sphinx.
    """

    def __init__(self, allow_parent_links=False):
        """Initialize the ToC parser."""
        HTMLParser.__init__(self)

        self.nav = Nav()
        self._current_item = None
        self._use_data = False
        self._parent_stack = [self.nav]
        self._is_first_ul = True
        self._allow_parent_links = allow_parent_links

    def reset(self):
        """Reset the HTML parser."""
        HTMLParser.reset(self)

        self.nav = Nav()
        self._current_item = None
        self._use_data = False
        self._parent_stack = [self.nav]
        self._is_first_ul = True

    def handle_starttag(self, tag, attrs):
        """Called when the parser encounters a new opening tag.

        Args:
            tag (str): The name of the tag.
            attrs (tuple): The HTML attributes of the tag.
        """
        if tag == "ul":
            if self._is_first_ul:
                self._is_first_ul = False
            else:
                # a new list, so we push the current item on the parent stack to
                # prepare to add children to it
                self._parent_stack.append(self._current_item)
                if not self._allow_parent_links:
                    self._current_item.url = None
        elif tag == "li":
            # this is a child item, so create a new item and append it to the
            # current parent

            self._current_item = Page()
            self._current_item.parent = self._parent_stack[-1]
            self._parent_stack[-1].children.append(self._current_item)

            # find the active page
            for attr, data in attrs:
                if attr == "class":
                    self._current_item.active = "current" in data
        elif tag == "a":
            # get the url associated and make sure we will capture the next
            # data element, it is the text of the ToC entry
            for attr, data in attrs:
                if attr == "href":
                    self._current_item.url = data
            self._use_data = True

    def handle_endtag(self, tag):
        """Called when the parser encounters a closing tag.

        Args:
            tag (str): The name of the tag which is closed.
        """
        # we've reached the end of a list, and the end of the current item
        if tag == "ul":
            self._current_item = self._parent_stack.pop()

    def handle_data(self, data):
        """Called when the parser encounters data enclosed by a tag.

        Args:
            data (str): The data enclosed by a tag.
        """
        # if we need the link text, get it
        if self._use_data:
            self._current_item.title = data
            self._use_data = False


# pylint: disable=unused-argument
def build_tocs(app, pagename, templatename, context, doctree):
    """Injects the global and local Tables of Contents into the HTML context.

    Args:
        app: The Sphinx application.
        pagename (str): The name of the current page.
        templatename (str): The name of the template used to render the page.
        context (dict): The context passed to the page template for rendering.
        doctree: A doctree when the page is created from reST documents.
    """
    # build the global table of contents
    if "toctree" in context:
        global_toc_html = context["toctree"](
            maxdepth=-1, collapse=False, includehidden=True, titles_only=True
        )
        parser = TocHTMLParser()
        parser.feed(global_toc_html)
        homepage_url = context["pathto"](context["master_doc"], 1)
        parser.nav.set_homepage(homepage_url)
        context["globaltoc"] = parser.nav

    # build the local table of contents
    if "toc" in context:
        parser = TocHTMLParser(allow_parent_links=True)
        parser.feed(context["toc"])

        # check there is a heading and only set the local ToC if there is
        if len(parser.nav):
            context["localtoc"] = parser.nav[0]
