Methodology overview
====================

An overview of the methodology applied to create Sphinx BlueBrain Theme is
given below:

#. User clones ``sphinx-bluebrain-theme`` git repository::

      git clone --recursive https://github.com/BlueBrain/sphinx-bluebrain-theme.git

#. User runs ``tox`` tox environment::

      tox

#. This environment runs ``translate_templates.py``, which does the following:

   #. Copies required source files from ``mkdocs-material`` theme :file:`src`
      directory.
   #. Applies conversion rules to some files (``.html``, ``.css``, ``.js``, and
      files with extensions ending in ``_t``). These rules are:

      #. Clears specified Jinja ``blocks`` of content.
      #. Replaces specified strings within the source files with their
         replacement values.
      #. Prepends the ``mkdocs-material`` license to files which have had it
         removed (due to minification). Specified files are skipped.

   #. Copies additional source files for the theme from the :file:`src`
      directory.
   #. Renames the :file:`assets` directory to :file:`static` which is required
      by Sphinx.
