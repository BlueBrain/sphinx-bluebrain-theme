"""
Test nav utils
"""

# pylint: disable=import-error
import pytest
from sphinx_bluebrain_theme.utils import navutils


def test_set_active():
    """
    Test setting a child to active, which should make ancestors active.
    """
    page = navutils.Page()
    parent = navutils.Page()

    page.parent = parent

    assert not page.active
    assert not parent.active

    page.active = True

    assert page.active
    assert parent.active


def test_page_equality():
    """
    Tests pages for equality.
    """

    page1 = navutils.Page()
    page2 = navutils.Page()
    nav = navutils.Nav()

    assert page1 != page2
    assert page1 != nav

    page1.active = True
    page2.active = True
    nav.active = True

    assert page1 != nav
    assert page1 == page2


def test_page_bool():
    """
    Tests that a page evaluates correctly as a boolean.

    This is required so that the Prev/Next links on pages
    will work.
    """
    page = navutils.Page()

    assert not bool(page)

    page.title = "Test Title"
    page.url = "www.testurl.com"

    assert bool(page)


def test_navbase():
    """
    Tests the NavBase class functionality.
    """
    nb = navutils.NavBase()
    nb.children = [0, 1, 2, 3]

    assert list(nb) == list(nb.children)
    assert len(nb) == len(nb.children)
    assert len(nb) == 4
    assert nb[0] == 0
    assert nb[3] == 3

    nb.children.pop(0)

    assert list(nb) == list(nb.children)
    assert len(nb) == len(nb.children)
    assert len(nb) == 3
    assert nb[0] == 1
    assert nb[2] == 3


def test_set_homepage():
    """
    Tests finding the homepage for a Nav.
    """
    page1 = navutils.Page()
    page1.url = "otherpage.html"
    page2 = navutils.Page()
    page2.url = "homepage.html"
    nav = navutils.Nav()

    assert not page1.is_homepage
    assert not page2.is_homepage

    nav.children = [page1, page2]
    nav.set_homepage("homepage")

    assert not page1.is_homepage
    assert page2.is_homepage

    page2.is_homepage = False
    page2.url = "#"

    assert not page1.is_homepage
    assert not page2.is_homepage

    nav.set_homepage("another_page")

    assert not page1.is_homepage
    assert page2.is_homepage
