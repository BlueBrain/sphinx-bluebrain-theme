Building the theme
==================

In order to build the theme, you must first checkout the
``sphinx-bluebrain-theme`` source::

   git clone --recursive ssh://bbpcode.epfl.ch/nse/sphinx-bluebrain-theme

This will also clone the ``mkdocs-material`` submodule which is required.

Building the theme is very simple::

   tox -e build-theme

This will run the necessary conversion scripts and copy the required source
files.

Once the theme has been built, the theme will be located in the
:file:`sphinx_bluebrain_theme` directory.

.. warning::

   You should never edit files in the :file:`sphinx_bluebrain_theme` directory
   by hand, any changes will be overwritten next time someone builds the theme.
