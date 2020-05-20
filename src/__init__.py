"""sphinx_bluebrain_theme package."""

from os import path

from sphinx_bluebrain_theme import utils


def setup(app):
    """Initialise the theme and connect theme specific functions to events."""
    app.add_html_theme("sphinx-bluebrain-theme", path.dirname(path.abspath(__file__)))
    app.setup_extension("sphinx_bluebrain_theme.ext.tabs")
    app.setup_extension("sphinx_bluebrain_theme.ext.details")
    app.setup_extension("sphinx_bluebrain_theme.ext.iframe")
    app.connect("builder-inited", utils.add_filters)
    app.connect("builder-inited", utils.add_autodoc_override)
    app.connect("env-updated", utils.write_metadata_sphinx)
    app.connect("html-page-context", utils.build_tocs)
    app.connect("html-page-context", utils.inject_context_variables)
