Changelog
=========

0.0.12
------

0.0.11
------
- |fixed| Assert when no metadata given.

0.0.10
------
- |added| Support Sphinx 2.x.
- |added| Support for hyphens in english search.
- |added| Metadata generation from python package metadata.
- |added| Metadata also written to JSON.
- |added| Assumption that ``conf.py`` is in git repository as default for getting contributors.
- |removed| Getting metadata from ``setup.py`` and ``setup.cfg``.

0.0.9
-----
- |fixed| Building when no metadata file is given.

0.0.8
-----
- |added| Metadata generation from ``setup.py``, ``setup.cfg``, or ``.json`` file.
- |removed| Output of built documentation to directory named by version.

0.0.6
-----
- |fixed| Incorrect code block margins.
- |fixed| Broken build when page has no sections.
- |added| Output of built documentation to directory named by version.

0.0.5
-----
- |fixed| Python 2.7 compatibility which failed due missing class in Sphinx < 2.0.

0.0.4
-----
- |fixed| Python 2.7 compatibiity broken by ``re.fullmatch``.
- |fixed| Issue when building theme documentation using ``pip 19.1`` with editable install.
- |fixed| Incorrect ``css`` for anchors and accelator keys.
- |fixed| Poor alignment of MathJax rendered equations.
- |fixed| Poor legibility of code blocks due to lightweight font.
- |added| ``iframe`` directive for embedding ``.html`` files (Doxygen output for example).
- |added| Configurable copyright years in copyright text.

.. |fixed| image:: https://img.shields.io/badge/-fixed-success.svg
              :class: badge
.. |added| image:: https://img.shields.io/badge/-added-seagreen.svg
              :class: badge
.. |changed| image:: https://img.shields.io/badge/-changed-informational.svg
                :class: badge
.. |removed| image:: https://img.shields.io/badge/-removed-slategrey.svg
                :class: badge
.. |deprecated| image:: https://img.shields.io/badge/-deprecated-lightgrey.svg
                   :class: badge
.. |security| image:: https://img.shields.io/badge/-security-tomato.svg
                 :class: badge
