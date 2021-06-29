Sphinx BlueBrain Theme
======================

|build_status| |license| |black| |docs|

Introduction
------------

Sphinx BlueBrain Theme is the standard Blue Brain Project documentation theme.

You can view the |changelog| to see what has changed recently.

Installation
------------

You can install the theme using `pip`::

   pip install sphinx-bluebrain-theme

Usage
-----

Refer to the |usage| for how to use the theme.

License
-------

The code for the theme is licensed under the MIT License.

The name "Blue Brain Project" and the EPFL logo are property of their respective
owners and do not fall under the MIT license.

The theme incorporates third party components which are listed below, along with their relevant licenses:

`Material for MkDocs theme <https://squidfunk.github.io/mkdocs-material/>`__
   MIT License, see `the license <https://github.com/squidfunk/mkdocs-material/blob/master/LICENSE>`__.
`Open Sans font <https://fonts.google.com/specimen/Open+Sans>`__
   Apache License Version 2.0, see `the license <https://github.com/BlueBrain/sphinx-bluebrain-theme/blob/master/src/assets/fonts/open-sans/LICENSE.txt>`__.
`Titillium Web font <https://fonts.google.com/specimen/Titillium+Web>`__
   Open Font License Version 1.1, see `the license <https://github.com/BlueBrain/sphinx-bluebrain-theme/blob/master/src/assets/fonts/titillium-web/OFL.txt>`__.
EPFL logo
   The EPFL logo is copyright EPFL. All rights reserved.

About
-----

Sphinx BlueBrain Theme is a Sphinx theme based on the excellent *Material for
MkDocs* theme by Martin Donath (@squidfunk).

The `original theme <https://github.com/squidfunk/mkdocs-material>`__ is
licensed under the MIT license and is hosted on GitHub.

You can see examples (and the associated ``rst`` source) in the |sample| page.

Sphinx BlueBrain Theme is built through a combination of text replacement rules,
HTML template overrides, a small amount of additional CSS and Javascript, and
a python module which injects additional required context.

Acknowledgement
---------------

The development of this software was supported by funding to the Blue Brain Project, a research center of the École polytechnique fédérale de Lausanne (EPFL), from the Swiss government’s ETH Board of the Swiss Federal Institutes of Technology.

Copyright (c) 2020-2021 Blue Brain Project/EPFL


.. |build_status| image:: https://travis-ci.com/BlueBrain/sphinx-bluebrain-theme.svg?branch=master
                     :target: https://travis-ci.com/BlueBrain/sphinx-bluebrain-theme
                     :alt: Build Status

.. |license| image:: https://img.shields.io/pypi/l/sphinx-bluebrain-theme
                :target: https://github.com/BlueBrain/sphinx-bluebrain-theme/blob/master/LICENSE.txt

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
              :target: https://github.com/psf/black

.. |docs| image:: https://readthedocs.org/projects/sphinx-bluebrain-theme/badge/?version=latest
             :target: https://sphinx-bluebrain-theme.readthedocs.io/
             :alt: documentation status

.. substitutions
.. |changelog| replace:: changelog_
.. _changelog: CHANGELOG.rst
.. |usage| replace:: `usage guide <usage_>`_
.. _usage: doc/source/usage.rst
.. |sample| replace:: `samples <sample_>`_
.. _sample: doc/source/sample.rst
