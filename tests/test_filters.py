"""
Test for the custom filters.
"""

from sphinx.application import Sphinx
import pytest  # pylint: disable=unused-import
from sphinx_bluebrain_theme.utils.filters import add_filters, url_filter


def test_add_filter():
    """
    Test that the filters are correctly added.
    """
    app = Sphinx("./", None, "./build", "./doctree", "html")
    add_filters(app)
    # pylint: disable=comparison-with-callable
    assert app.builder.templates.environment.filters["url"] == url_filter


def test_url_filter():
    """
    Test the conversion of urls.
    """

    def pathto(x, _):
        return x

    context = {"pathto": pathto}
    url_static = "_static/test_asset.css"
    url_assets = "assets/test_asset.css"

    # test a url that shouldn't be changed
    url = url_filter(context, url_static)
    assert url == url_static

    # test a url which should be converted
    url = url_filter(context, url_assets)
    assert url == url_static
