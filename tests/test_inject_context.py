"""
Test for context injection.
"""

from collections import defaultdict

from mock import patch  # pylint: disable=import-error
from nose import tools as nt  # pylint: disable=import-error
from sphinx_bluebrain_theme.utils import inject_context


def test_build_adjacent_page():
    """
    Test the construction of an adjacent page from dict.
    """
    data = {"title": "test page", "link": "./test-url.html"}

    page = inject_context.build_adjacent_page(data)

    nt.assert_equal(page.title, "test page")
    nt.assert_equal(page.url, "./test-url.html")


def test_build_adjacent_page_none():
    """
    Test the construction of an adjacent page when there is none.
    """
    page = inject_context.build_adjacent_page(None)

    nt.assert_is_none(page)


def test_build_no_font():
    """Test building the font context variable with no specified font."""
    context = defaultdict(lambda: None)
    context["theme_use_google_fonts"] = False
    font = inject_context.build_font(context)

    nt.assert_false(font)


def test_build_no_font_with_google_font():
    """Test building the font context variable with: no specified font, but using google fonts."""
    context = defaultdict(lambda: None)
    context["theme_use_google_fonts"] = True
    font = inject_context.build_font(context)

    nt.assert_true(font)


def test_build_font():
    """Test building the font context variable."""
    context = {}
    context["theme_use_google_fonts"] = True
    context["theme_font_text"] = "font-text"

    # without code font first
    context["theme_font_code"] = None
    font = inject_context.build_font(context)

    nt.assert_equal(font["text"], "font-text")
    nt.assert_equal(font["code"], "")

    # now set code font
    context["theme_font_code"] = "font-code"
    font = inject_context.build_font(context)

    nt.assert_equal(font["text"], "font-text")
    nt.assert_equal(font["code"], "font-code")


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
        nt.assert_equal(mock_logger.warning.call_count, 1)


def test_copyright_no_warning():
    """Test copyright giving no warning when it is not defined."""
    context = {"theme_address": None, "theme_social": None, "config": {}}

    with patch("sphinx_bluebrain_theme.utils.inject_context.logger") as mock_logger:
        inject_context.bbp_context_cleanup(context)
        nt.assert_equal(mock_logger.warning.call_count, 0)


def test_build_extra_empty():
    """Build the extra context variable with no entries."""
    context = defaultdict(lambda: None)
    extra = inject_context.build_extra(context, None)

    for e in extra:
        yield nt.assert_is_none, extra[e]


def test_build_extra():
    """Build extra context variable."""
    context = {
        "theme_repo_icon": "icon",
        "theme_social": "social",
        "theme_manifest": "manifest",
    }
    extra = inject_context.build_extra(context, "en")

    nt.assert_equal(extra["repo_icon"], "icon")
    nt.assert_equal(extra["social"], "social")
    nt.assert_equal(extra["manifest"], "manifest")
    nt.assert_equal(extra["search"], {"tokenizer": r"[\s]+"})
    nt.assert_is_none(extra["disqus"])


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
    nt.assert_equal(context["theme_address"], ["Blue Brain Project", "Geneva"])

    # check the social output
    social_result = [
        {"type": "facebook", "link": "facebook.com"},
        {"type": "linkedin", "link": "linkedin.com"},
    ]
    nt.assert_equal(context["config"]["extra"]["social"], social_result)
