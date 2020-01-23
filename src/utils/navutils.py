"""Utilities for building mkdocs compatible navigation objects.

Since the original theme is built for mkdocs, all the templates
expect mkdocs classes (and their attributes), so these classes
provide compatible data structures.

The classes are mainly data holders with a very few
convenience methods to assist with building and maintaining
consistent navigation structures.

See mkdocs description, which lists all the expected attributes:
- https://www.mkdocs.org/user-guide/custom-themes/#nav
- https://www.mkdocs.org/user-guide/custom-themes/#pages

See also mkdocs implementation:
- https://github.com/mkdocs/mkdocs/tree/master/mkdocs/structure
"""


class NavBase(object):  # pylint: disable=useless-object-inheritance
    """Base class for navigation objects."""

    is_page = False

    def __init__(self):
        """Initialize the NavBase object."""
        self.title = None
        self.parent = None
        self.children = []
        self._active = False

    def __iter__(self):
        """Iterates over the object's children."""
        return iter(self.children)

    def __len__(self):
        """Returns the number of children."""
        return len(self.children)

    def __getitem__(self, key):
        """Returns the nth child."""
        return self.children[key]

    @property
    def active(self):
        """Return whether this nav object is active."""
        return self._active

    @active.setter
    def active(self, value):
        """Set the active state of the nav object also setting its parent to active."""
        is_active = bool(value)
        self._active = is_active

        # do not allow making the parent inactive
        if self.parent is not None and is_active:
            self.parent.active = is_active


class Nav(NavBase):
    """Class for top level nav object, container for all others."""

    def __init__(self):
        """Initialize the base class and Nav specific attributes."""
        super(Nav, self).__init__()
        self.homepage = None
        self.pages = []
        self.title = "Base Nav"

    def set_homepage(self, homepage_name):
        """Search for, and set, the homepage."""
        # homepage should be in the top level of pages
        for page in self.children:
            if page.url == homepage_name + ".html" or page.url == "#":
                page.is_homepage = True
                return


class Page(NavBase):
    """Dedicated class for Page."""

    is_page = True

    def __init__(self):
        """Initialize the base class and Page specific attributes."""
        super(Page, self).__init__()
        self.content = None
        self.toc = None
        self.meta = None
        self.url = None
        self.abs_url = None
        self.canonical_url = None
        self.edit_url = None
        self.is_homepage = False
        self.previous_page = None
        self.next_page = None
        self.ancestors = None

    def __eq__(self, other):
        """Evaluates equality based on active status only."""
        return isinstance(other, Page) and self.active and other.active

    def __bool__(self):
        """If the page has a title and url then it is true."""
        return self.title is not None and self.url is not None
