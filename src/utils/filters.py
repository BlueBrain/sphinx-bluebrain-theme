"""This module contains custom filters for the translation from mkdocs to sphinx."""

from jinja2 import contextfilter


def add_filters(app):
    """Register custom filters for page rendering.

    Args:
        app: The Sphinx application.
    """
    app.builder.templates.environment.filters["url"] = url_filter


@contextfilter
def url_filter(context, path):
    """Returns the path to static content allowing for the 'assets/' path used by mkdocs.

    If the path is not to the 'assets/' directory, the given path is returned unchanged.

    Args:
        context (dict): The Jinja context for the page being rendered. This is
            given by Jinja due to the use of the @contextfilter decorator.
        path (str): A path to static (or other) content.

    Returns:
        str: A path to the content accounting for the mkdocs static content path of 'assets/'.
    """
    if "assets/" in path and "pathto" in context:
        path = path.replace("assets/", "_static/")
        path = context["pathto"](path, 1)

    return path
