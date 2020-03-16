Sample
======

This page includes samples of the expected output of the theme as well as
the input used to generate it.

Second level headings
---------------------

Second level heading section content.

Third level headings
~~~~~~~~~~~~~~~~~~~~

Third level heading section content.

Fourth level headings
*********************

Fourth level heading section content.

Fifth level headings
^^^^^^^^^^^^^^^^^^^^

Fifth level heading section content.

Sixth level headings
++++++++++++++++++++

Sixth level heading section content.

.. literalinclude:: sample.rst
   :language: rst
   :start-at: Sample
   :end-before: .. literalinclude

Lists
-----

Unordered lists
~~~~~~~~~~~~~~~

* list item 1.
* list item 2.

  * nested list item 1.
  * nested list item 2.

    * double nested list item 1.

  * nested list item 3.

.. literalinclude:: sample.rst
   :language: rst
   :start-at: Unordered lists
   :end-before: .. literalinclude

Ordered lists
~~~~~~~~~~~~~

#. List item 1.
#. List item 2.

   #. Nested list item 1.
   #. Nested list item 2.

      #. Double nested list item 1.

   #. Nested list item 3.

.. literalinclude:: sample.rst
   :language: rst
   :start-at: Ordered lists
   :end-before: .. literalinclude

Definition lists
~~~~~~~~~~~~~~~~

Definition list item 1
   Definition text for definition list item 1.

Definition list item 2
   Definition text for definition list item 2.

.. literalinclude:: sample.rst
   :language: rst
   :start-at: Definition lists
   :end-before: .. literalinclude

Code
----

Inline code
~~~~~~~~~~~

.. role:: py3(code)
   :language: python3

Here is some sample inline code: :py3:`if test: return True`.

.. attention::

   If you need inline syntax highlighting, you must include a :file:`docutils.conf`
   file in the same directory as your :file:`conf.py` file.

   The required content of the file is shown below (see https://stackoverflow.com/a/48655335):

   .. literalinclude:: docutils.conf

.. literalinclude:: sample.rst
   :language: rst
   :start-at: Inline code
   :end-before: .. attention

Code blocks
~~~~~~~~~~~

.. code-block:: python3
   :linenos:
   :emphasize-lines: 2

   def double(x):
      return 2 * x

.. literalinclude:: sample.rst
   :language: rst
   :start-at: Code blocks
   :end-before: .. literalinclude

Code tabs
~~~~~~~~~

Tabs can be used to show multiple examples without excessive space. The code
can be entered directly or included from a file.

.. tabgroup::

   .. codetab:: python Python

       import sys

   .. codetab:: ruby Ruby

       require sys

   .. literaltab:: sample.py From file
      :language: python3

.. literalinclude:: sample.rst
   :language: rst
   :start-at: Code tabs
   :end-before: .. literalinclude

Tables
------

.. table::

   ======================== =========== ========== ======= ==== ===
   Table header column 1    Column 2    Column 3   Col. 4  C5   C6
   ======================== =========== ========== ======= ==== ===
   Row 1 data               1.0         0.1234     0.001   10.0 -1
   Row 2 data               1000.0      -1.2345    5.01    \-   \-
   ======================== =========== ========== ======= ==== ===

.. literalinclude:: sample.rst
   :language: rst
   :start-at: Tables
   :end-before: .. literalinclude

Admonitions
-----------

Built-in types
~~~~~~~~~~~~~~

.. attention::

   Attention

.. caution::

   Caution

.. danger::

   Danger

.. error::

   Error

.. hint::

   Hint

.. important::

   Important

.. note::

   Note

.. tip::

   Tip

.. warning::

   Warning

.. literalinclude:: sample.rst
   :language: rst
   :start-at: Built-in types
   :end-before: .. literalinclude

Additional types
~~~~~~~~~~~~~~~~

These types require you to add the class explicitly using ``:class: classname``.
Applicable classnames are shown in each admonition.

.. admonition:: Abstract
   :class: abstract

   - abstract
   - summary
   - tldr

.. admonition:: Info
   :class: info

   - info
   - todo

.. admonition:: Success
   :class: success

   - success
   - check
   - done

.. admonition:: Question
   :class: question

   - question
   - help
   - faq

.. admonition:: Failure
   :class: failure

   - failure
   - fail
   - missing

.. admonition:: Bug
   :class: bug

   - bug

.. admonition:: Example
   :class: example

   - example
   - snippet

.. admonition:: Quote
   :class: quote

   - quote
   - cite

.. literalinclude:: sample.rst
   :language: rst
   :start-at: Additional types
   :end-before: .. literalinclude

Miscellaneous
-------------

Blockquotes
~~~~~~~~~~~

   Blockquote content.

.. literalinclude:: sample.rst
   :language: rst
   :start-at: Blockquotes
   :end-before: .. literalinclude

Nested blockquotes
******************

   Blockquote content.

      Nested blockquote content.

         Double nested blockquote content.

.. literalinclude:: sample.rst
   :language: rst
   :start-at: Nested blockquotes
   :end-before: .. literalinclude

Horizontal rules
~~~~~~~~~~~~~~~~

Here is some text before a horizontal rule.

----

Here is some text after a horizontal rule

.. literalinclude:: sample.rst
   :language: rst
   :start-at: Horizontal rules
   :end-before: .. literalinclude

Epigraphs
~~~~~~~~~

.. epigraph::

   This is an epigraph.

   -- by an Author

.. literalinclude:: sample.rst
   :language: rst
   :start-at: Epigraphs
   :end-before: .. literalinclude

Topics
~~~~~~

.. topic:: Topic title

   This is a topic

.. literalinclude:: sample.rst
   :language: rst
   :start-at: Topics
   :end-before: .. literalinclude

Sidebars
~~~~~~~~

.. sidebar:: Sidebar title
   :class: admonition

   This is a sidebar

Here is some text that will flow around the sidebar that follows.
If we have something interesting to say, we can put it in the
sidebar.

.. literalinclude:: sample.rst
   :language: rst
   :start-at: Sidebars
   :end-before: .. literalinclude

Collapsible blocks
~~~~~~~~~~~~~~~~~~

.. details:: Details hidden by default

   Here is some content that is hidden before opening.

.. details:: Details shown by default
   :open:

   Here is some content that is shown by default

.. literalinclude:: sample.rst
   :language: rst
   :start-at: Collapsible blocks
   :end-before: .. literalinclude

IFrames
~~~~~~~

Embed existing HTML files (such as Doxygen output) in generated pages.

.. iframe:: index.html

.. literalinclude:: sample.rst
   :language: rst
   :start-at: IFrames
   :end-before: .. literalinclude

Images
~~~~~~

Embed an image with optional alignment.

.. image:: _images/epfl-logo-new.svg
   :width: 25%
   :align: left

.. image:: _images/epfl-logo-new.svg
   :width: 25%
   :align: center

.. image:: _images/epfl-logo-new.svg
   :width: 25%
   :align: right

.. literalinclude:: sample.rst
   :language: rst
   :start-at: Images
   :end-before: .. literalinclude
