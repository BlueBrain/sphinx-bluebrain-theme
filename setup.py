#!/usr/bin/env python
"""setup.py for theme."""

import subprocess

from setuptools import setup
from setuptools.command.sdist import sdist


class BuildPy(sdist):
    """Build the theme on sdist."""

    def run(self):
        """Run the build process."""
        subprocess.call(("python", "translate_templates.py"))
        sdist.run(self)


setup(use_scm_version={"write_to": "src/version.py"}, cmdclass={"sdist": BuildPy})
