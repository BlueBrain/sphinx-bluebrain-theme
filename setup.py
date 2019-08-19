#!/usr/bin/env python
"""setup.py for theme."""

import sys
import subprocess
import imp

from setuptools import setup
from setuptools.command.sdist import sdist


class BuildPy(sdist):
    """Build the theme on sdist."""

    def run(self):
        """Run the build process."""
        subprocess.call(("python", "translate_templates.py"))
        sdist.run(self)


VERSION = imp.load_source("", "sphinx_bluebrain_theme/version.py").__version__

if sys.version_info < (2, 7):
    sys.exit("Sorry, Python < 2.7 is not supported")

setup(
    name="sphinx-bluebrain-theme",
    author="BlueBrain NSE",
    author_email="bbp-ou-nse@groupes.epfl.ch",
    version=VERSION,
    description="BlueBrain project theme for Sphinx",
    url="https://github.com/BlueBrain/sphinx-bluebrain-theme/issues",
    project_urls={
        "Tracker": "https://github.com/BlueBrain/sphinx-bluebrain-theme/issues",
        "Source": "https://github.com/BlueBrain/sphinx-bluebrain-theme",
    },
    license="MIT License",
    install_requires=["sphinx>=1.8.0"],
    include_package_data=True,
    packages=[
        "sphinx_bluebrain_theme",
        "sphinx_bluebrain_theme.ext",
        "sphinx_bluebrain_theme.utils",
    ],
    entry_points={
        "sphinx.html_themes": ["sphinx-bluebrain-theme = sphinx_bluebrain_theme"]
    },
    cmdclass={"sdist": BuildPy},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Framework :: Sphinx",
        "Framework :: Sphinx :: Theme",
        "License :: OSI Approved :: MIT License",
        "Topic :: Documentation",
        "Topic :: Documentation :: Sphinx",
        "Operating System :: OS Independent",
    ],
)
