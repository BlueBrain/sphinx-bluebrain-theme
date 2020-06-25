"""Configuration file for the Sphinx documentation builder."""

# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
from pkg_resources import get_distribution

# these pages will have the version overwritten so that it doesn't fail
# when a new version is released.
REGRESSION_TEST_PAGENAMES = {"regression"}

# -- Project information -----------------------------------------------------

project = u"sphinx-bluebrain-theme"

# read the docs does not like using the cloned repo as the theme
# for the documentation build so the version number will be wrong
on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
    # note: delay import so we only need setuptools_scm on Read the Docs
    from setuptools_scm import get_version
    version = get_version(root="../..", relative_to=__file__)
else:
    version = get_distribution("sphinx-bluebrain-theme").version

release = version

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.autodoc", "sphinx.ext.intersphinx", "sphinx.ext.napoleon"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The master toctree document.
master_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx-bluebrain-theme"
html_title = "Sphinx BlueBrain Theme"
html_favicon = "favicon.ico"
html_theme_options = {
    "repo_url": "https://github.com/BlueBrain/sphinx-bluebrain-theme/",
    "repo_name": "BlueBrain/sphinx-bluebrain-theme",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]


def setup(app):
    """Do the setup for the theme documentation."""

    # pylint: disable=unused-argument
    def override_regression_test_version(app, pagename, templatename, context, doctree):
        """Override the version of regression test pages to prevent failure during a new release."""
        if pagename in REGRESSION_TEST_PAGENAMES:
            context["version"] = "REGRESSION-TEST"
            context["sphinx_version"] = "REGRESSION-TEST"

    # add custom stylesheet
    app.add_css_file("custom.css")

    app.connect("html-page-context", override_regression_test_version)
