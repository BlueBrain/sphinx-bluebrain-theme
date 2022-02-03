Contributing
============

This page includes some guidelines to enable you to contribute to the project.

Found a bug?
------------

If you find a bug in the source code or in using the theme, you can
`open an issue <https://github.com/BlueBrain/sphinx-bluebrain-theme/issues>`__ on GitHub.
Even better, you can
`submit a pull request <https://github.com/BlueBrain/sphinx-bluebrain-theme/pulls>`__
with a fix.

Submission guidelines
---------------------

Submitting an issue
~~~~~~~~~~~~~~~~~~~

Before you submit an issue, please search the issue tracker, maybe an issue
for your problem already exists and the discussion might inform you of workarounds
readily available.

We want to fix all the issues as soon as possible, but before fixing a bug we
need to reproduce and confirm it. In order to reproduce bugs we will need as
much information as possible, and preferably a sample demonstrating the issue.

Submitting a pull request (PR)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you wish to contribute to the code base, please open a pull request by
following GitHub's guidelines.

Development Conventions
-----------------------

Sphinx BlueBrain Theme uses:
   - Black for formatting code
   - PyLint for linting code
   - PyDocStyle for checking docstrings

Tests and linting can be run using the ``tox`` command.

Continuous Integration (CI)
---------------------------

1) Create a PR with the changes.

2) Test the changes installing the package

   ``pip3 install 'git+https://github.com/BlueBrain/sphinx-bluebrain-theme.git@<BRANCH_NAME>#egg=sphinx-bluebrain-theme'``

3) Amend the necessary items on the PR until the package is working properly.

4) Merge the PR to the default branch.

5) Then you can tag with a release version vX.Y.Z the merged commit and a release version
   will be produced in pypi.

6) The documentation is `built <https://readthedocs.org/projects/sphinx-bluebrain-theme/builds>`_
   on push to the default branch.
