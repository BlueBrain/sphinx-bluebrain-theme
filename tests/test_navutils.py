"""
Test nav utils
"""

# pylint: disable=import-error
from nose import tools as nt
from sphinx_bluebrain_theme.utils import navutils


def test_set_active():
    """
    Test setting a child to active, which should make ancestors active.
    """
    page = navutils.Page()
    parent = navutils.Page()

    page.parent = parent

    nt.assert_equal(page.active, False)
    nt.assert_equal(parent.active, False)

    page.active = True

    nt.assert_equal(page.active, True)
    nt.assert_equal(parent.active, True)


def test_page_equality():
    """
    Tests pages for equality.
    """

    page1 = navutils.Page()
    page2 = navutils.Page()
    nav = navutils.Nav()

    nt.assert_equal(page1 == page2, False)
    nt.assert_equal(page1 == nav, False)

    page1.active = True
    page2.active = True
    nav.active = True

    nt.assert_equal(page1 == nav, False)
    nt.assert_equal(page1 == page2, True)


def test_page_bool():
    """
    Tests that a page evaluates correctly as a boolean.

    This is required so that the Prev/Next links on pages
    will work.
    """
    page = navutils.Page()

    nt.assert_equal(bool(page), False)

    page.title = "Test Title"
    page.url = "www.testurl.com"

    nt.assert_equal(bool(page), True)


def test_navbase():
    """
    Tests the NavBase class functionality.
    """
    nb = navutils.NavBase()
    nb.children = [0, 1, 2, 3]

    nt.assert_sequence_equal(list(nb), list(nb.children))
    nt.assert_equal(len(nb), len(nb.children))
    nt.assert_equal(len(nb), 4)
    nt.assert_equal(nb[0], 0)
    nt.assert_equal(nb[3], 3)

    nb.children.pop(0)

    nt.assert_sequence_equal(list(nb), list(nb.children))
    nt.assert_equal(len(nb), len(nb.children))
    nt.assert_equal(len(nb), 3)
    nt.assert_equal(nb[0], 1)
    nt.assert_equal(nb[2], 3)


def test_set_homepage():
    """
    Tests finding the homepage for a Nav.
    """
    page1 = navutils.Page()
    page1.url = "otherpage.html"
    page2 = navutils.Page()
    page2.url = "homepage.html"
    nav = navutils.Nav()

    nt.eq_(page1.is_homepage, False)
    nt.eq_(page2.is_homepage, False)

    nav.children = [page1, page2]
    nav.set_homepage("homepage")

    nt.eq_(page1.is_homepage, False)
    nt.eq_(page2.is_homepage, True)

    page2.is_homepage = False
    page2.url = "#"

    nt.eq_(page1.is_homepage, False)
    nt.eq_(page2.is_homepage, False)

    nav.set_homepage("another_page")

    nt.eq_(page1.is_homepage, False)
    nt.eq_(page2.is_homepage, True)
