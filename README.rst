Sphinx BlueBrain Theme
======================

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
      :class: badge
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
      :class: badge

Introduction
------------

Sphinx BlueBrain Theme is the standard Blue Brain Project documentation theme.

You can view the :doc:`changelog` to see what has changed recently.

Installation
------------

You can install the theme using `pip`::

   pip install sphinx-bluebrain-theme

Usage
-----

Refer to the :doc:`usage guide <usage>` for how to use the theme.

License
-------

The code for the theme is licensed under the MIT License. Note that the EPFL
logo is **not** licensed under the MIT License.

The theme incorporates third party components which are listed below, along with their relevant licenses:

`Material for MkDocs theme <https://squidfunk.github.io/mkdocs-material/>`__
   MIT License, see :file:`mkdocs-material/LICENSE`.
`Open Sans font <https://fonts.google.com/specimen/Open+Sans>`__
   Apache License Version 2.0, see :file:`src/assets/fonts/open-sans/LICENSE.txt`.
`Titillium Web font <https://fonts.google.com/specimen/Titillium+Web>`__
   Open Font License Version 1.1, see :file:`src/assets/fonts/titillium-web/OFL.txt`.
EPFL logo
   The EPFL logo is copyright EPFL. All rights reserved.

About
-----

Sphinx BlueBrain Theme is a Sphinx theme based on the excellent *Material for
MkDocs* theme by Martin Donath (@squidfunk).

The `original theme <https://github.com/squidfunk/mkdocs-material>`__ is
licensed under the MIT license and is hosted on GitHub.

You can see examples (and the associated ``rst`` source) in the
:doc:`samples <sample>` page.

Sphinx BlueBrain Theme is built through a combination of text replacement rules,
HTML template overrides, a small amount of additional CSS and Javascript, and
a python module which injects additional required context.
