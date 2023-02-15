"""
Test for context injection.
"""

from collections import defaultdict

from unittest.mock import patch
import pytest  # pylint: disable=unused-import
from sphinx_bluebrain_theme.utils import inject_context


def test_build_adjacent_page():
    """
    Test the construction of an adjacent page from dict.
    """
    data = {"title": "test page", "link": "./test-url.html"}

    page = inject_context.build_adjacent_page(data)

    assert page.title == "test page"
    assert page.url == "./test-url.html"


def test_build_adjacent_page_none():
    """
    Test the construction of an adjacent page when there is none.
    """
    page = inject_context.build_adjacent_page(None)

    assert page is None


def test_build_no_font():
    """Test building the font context variable with no specified fo"""
    context = defaultdict(lambda: None)
    context["theme_use_google_fonts"] = False
    font = inject_context.build_font(context)

    assert not font


def test_build_no_font_with_google_font():
    """Test building the font context variable with: no specified font, but using google fonts."""
    context = defaultdict(lambda: None)
    context["theme_use_google_fonts"] = True
    font = inject_context.build_font(context)

    assert font


def test_build_font():
    """Test building the font context variable."""
    context = {}
    context["theme_use_google_fonts"] = True
    context["theme_font_text"] = "font-text"

    # without code font first
    context["theme_font_code"] = None
    font = inject_context.build_font(context)

    assert font["text"] == "font-text"
    assert font["code"] == ""

    # now set code font
    context["theme_font_code"] = "font-code"
    font = inject_context.build_font(context)

    assert font["text"] == "font-text"
    assert font["code"] == "font-code"


def test_copyright_warning():
    """Test copyright giving a warning when it will be overwritten."""
    context = {
        "copyright": "copyright-notice",
        "theme_address": None,
        "theme_social": None,
        "config": {},
    }

    with patch("sphinx_bluebrain_theme.utils.inject_context.logger") as mock_logger:
        inject_context.bbp_context_cleanup(context)
        assert mock_logger.warning.call_count == 1


def test_copyright_no_warning():
    """Test copyright giving no warning when it is not defined."""
    context = {"theme_address": None, "theme_social": None, "config": {}}

    with patch("sphinx_bluebrain_theme.utils.inject_context.logger") as mock_logger:
        inject_context.bbp_context_cleanup(context)
        assert mock_logger.warning.call_count == 0


def test_build_extra_empty():
    """Build the extra context variable with no entries."""
    context = defaultdict(lambda: None)
    extra = inject_context.build_extra(context, None)
    assert extra == {
        "repo_icon": None,
        "social": None,
        "disqus": None,
        "manifest": None,
    }


def test_build_extra():
    """Build extra context variable."""
    context = {
        "theme_repo_icon": "icon",
        "theme_social": "social",
        "theme_manifest": "manifest",
    }
    extra = inject_context.build_extra(context, "en")

    assert extra["repo_icon"] == "icon"
    assert extra["social"] == "social"
    assert extra["manifest"] == "manifest"
    assert extra["search"] == {"tokenizer": r"[\s]+"}
    assert extra["disqus"] is None


def test_bbp_cleanup():
    """
    Test the BBP specific clean up of context.
    """

    address = """Blue Brain Project
Geneva"""

    social = """facebook,facebook.com
linkedin,linkedin.com"""

    context = {
        "theme_address": address,
        "theme_social": social,
        "config": {"extra": {"social": None}},
    }

    inject_context.bbp_context_cleanup(context)

    # check the address
    assert context["theme_address"] == ["Blue Brain Project", "Geneva"]

    # check the social output
    social_result = [
        {"type": "facebook", "link": "facebook.com"},
        {"type": "linkedin", "link": "linkedin.com"},
    ]
    assert context["config"]["extra"]["social"] == social_result
