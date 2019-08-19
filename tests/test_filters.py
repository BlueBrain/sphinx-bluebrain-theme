"""
Test for the custom filters.
"""

# pylint: disable=import-error
from sphinx.application import Sphinx
from nose import tools as nt
from sphinx_bluebrain_theme.utils.filters import add_filters, url_filter


def test_add_filter():
    """
    Test that the filters are correctly added.
    """
    app = Sphinx("./", None, "./build", "./doctree", "html")
    add_filters(app)
    nt.assert_equal(app.builder.templates.environment.filters["url"], url_filter)


def test_url_filter():
    """
    Test the conversion of urls.
    """

    pathto = lambda x, y: x
    context = {"pathto": pathto}
    url_static = "_static/test_asset.css"
    url_assets = "assets/test_asset.css"

    # test a url that shouldn't be changed
    url = url_filter(context, url_static)
    nt.assert_equal(url, url_static)

    # test a url which should be converted
    url = url_filter(context, url_assets)
    nt.assert_equal(url, url_static)
