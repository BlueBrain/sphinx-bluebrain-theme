Guide
=====

.. toctree::
   :hidden:
   :titlesonly:

   Guide <self>
   sample

Quickstart
----------

The Sphinx BlueBrain Theme must be installed from PyPi::

   pip install sphinx-bluebrain-theme

You can then use the theme by specifying::

   html_theme = "sphinx-bluebrain-theme"

in the :file:`conf.py` for your documentation.

Generating tables of contents
-----------------------------

When structuring your documentation in Sphinx, you generally require multiple
``toctree`` commands which define the structure of the documentation.

As ``sphinx-bluebrain-theme`` shows tables of contents (ToC) on each page, you
can hide the ToC from the page body by specifying the ``:hidden:`` option::

   .. toctree::
      :hidden:
      :maxdepth: 2

      usage
      building

By default you cannot navigate to pages which contain ToCs from the sidebar ToC.
In order to allow users to view the content on these pages, you need to include
``self`` in the ToC on that page::

   .. toctree::
      :hidden:
      :maxdepth: 2

      Home <self>
      usage
      building

Note that the above example also specifies a custom name for the ``self`` page.
This is optional.

Metadata generation
-------------------

You can generate required BlueBrain Project metadata from either your python package, or a ``.json`` file.
In order to take advantage of this, specify the either the ``metadata_distribution`` or ``metadata_file``
variable in the ``html_theme_options`` dict in your ``conf.py``.

``metadata_distribution``
   Provide the name of a python package (installed in the current python environment) from
   which to extract the required metadata.

   The package you specify must provide at least the following metadata to ``setuptools``. This is shown in the
   ``setup()`` function below, however it can be specified in any way compatible with
   ``setuptools``:

   .. code-block:: python3
      :linenos:

      setup(
         ...
         name="project-name",
         author="project-author",
         version="project-version",
         description="project-description",
         url="project-homepage-url",
         project_urls={
             "Tracker": "project-bug-tracker-url",
             "Source": "project-source-repository-url",
         },
         license="project-license",
         ...
      )

``metadata_file``
   Provide the path (relative to the ``conf.py``) of a ``.json`` which contains the required metadata.
   It must follow the structure of a standard ``package.json`` file, although it can be named differently.

The metadata may also contain a key ``contributors`` for attribution.
If not provided, the top five contributors will be extracted from the git history of the
directory containing the ``conf.py``. You may override this by providing the ``repo_path``
value in ``html_theme_options``, it should be a path (relative to the ``conf.py``) to the
``.git`` folder of the repository.


Sphinx options
--------------

Most of the normal `Sphinx configuration options <http://www.sphinx-doc.org/en/master/usage/configuration.html>`__
should function as expected. However, some options will have different or no
effect at all.

``html_sidebars``
   Passing custom sidebar templates/globbing patterns will have no effect.
   The sidebars are always: global table of contents on the left, and local
   table of contents on the right.

Hero header text
----------------

You can add hero text in the header for any page by adding ``hero`` metadata to
any page. Example usage is shown below, this must be placed above all other
content in the page's ``.rst`` source:

.. highlight:: rst

::

   :hero: This is some hero text for the header

Configuration options
---------------------

The theme can be configured using the ``html_theme_options`` variable in the
:file:`conf.py` file. The following options are available:

``site_author``
   Sets the author for the documentation which will be used in the HTML meta tags.

``site_description``
   A brief description of the site which will be included in the HTML meta tags.

.. ``palette_primary``, ``palette_accent``
   Specify the primary and accent colors used for the documentation. Available
   values can be found in the `Material for MkDocs documentation <https://squidfunk.github.io/mkdocs-material/getting-started/#color-palette>`__

..   Default ``palette_primary``: ``blue``

..   Default ``palette_accent``: ``blue``

.. ``language_direction``
   You can specify if the language (set using the ``language`` Sphinx configuration
   parameter) should be rendered from left-to-right (``ltr``) or from
   right-to-left (``rtl``).

..   Default: ``ltr``

.. ``logo_icon``
   An icon to be displayed next to the documentation title in the header. Use
   the Sphinx option ``html_logo`` to provide an image.

.. ``logo_url``
   Provide a url for the logo in the header.

``repo_url``
   Set the url for the repository for the project you are documenting.

``repo_name``
   The name to be shown for the repository in the header.

``repo_icon``
   An icon to be shown for the repository in the header. If none is specified,
   then the theme will attempt to choose one based on the ``repo_url`` providing
   logos for GitHub, BitBucket, and GitLab repositories.

``feature_tabs``
   If you wish to add tabbed navigation to the header of your documentation,
   you must set this value to ``True``. Top level table of contents entries (which have
   children) will be shown in the header rather than in the Table of Contents.

   .. warning::

      When using tabs you cannot use ``self`` in any table of contents except the top
      level (usually ``index.rst``) or tabs will break.

.. ``use_google_fonts``
   If this value is set to ``True``, the theme will use fonts (specified by
   ``font_text``, ``font_code``, ``font_header``) from the Google font server. Note that this
   `may not comply <https://github.com/google/fonts/issues/1495>`__ with GDPR
   requirements and so is disabled by default.

.. ``font_text``, ``font_code``
   These values specify override values for the font used for the general text
   and code snippets.

.. ``font_header``
   Specify a different font for the header, page headings, and footer company
   name.

.. ``title_prefix``
   Include a string before the project title in the page header.

.. ``social_title``
   Provide a text header to be used above the social links in the footer.

.. ``social``
   This is a list of :ref:`dict` that contain ``type`` and ``link`` keys.
   Each ``type`` value specifies the symbol shown for the link, and must be a
   valid `Font Awesome <https://fontawesome.com/>`__ icon.

.. ``company``
   Provide the name of the company to be located in the footer.

.. ``address``
   Provide the address of the company (as a sequence of strings) to be included
   in the footer.

.. ``legal``
   Provide a list of tuples to be included in the legal notices in the footer.
   Each tuple should include the text of the link and the url::

..       html_theme_options = {
          "legal": [
              {
                  "text": "Link text",
                  "link": "Link url",
              }
          ]
      }

.. ``use_original_style``
   If set to true, BBP specific style overrides will not be included.
