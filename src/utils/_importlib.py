"""Ensure that the right version of importlib is imported."""

# pylint: disable=unused-import

import sys

if sys.version_info >= (3, 10, 2):
    from importlib import metadata, resources
else:
    import importlib_metadata as metadata
    import importlib_resources as resources
