"""Tests for metadata generation utilities."""

from contextlib import contextmanager
import json
import os
import shutil
import sys
import tempfile

import pytest  # pylint: disable=unused-import

from sphinx_bluebrain_theme.utils import metadata


@contextmanager
def setup_tempdir(prefix):
    """Create a temporary directory which will be cleaned up."""
    temp_dir = tempfile.mkdtemp(prefix=prefix)
    try:
        yield temp_dir
    finally:
        if os.path.isdir(temp_dir):
            shutil.rmtree(temp_dir)


def test_temp_change_working_directory():
    """Test changing the working directory temporarily."""
    current_wd = os.getcwd()

    with metadata.change_cwd("/"):
        assert os.getcwd() == "/"

    assert os.getcwd() == current_wd


def test_write_metadata_files():
    """Test that the metadata files are written and their content is correct."""
    with setup_tempdir("docs-path") as docs_path:
        metadata_dict = {"name": "test-data"}
        metadata.write_metadata(metadata_dict, docs_path)

        md_file = os.path.join(docs_path, "metadata.md")
        json_file = os.path.join(docs_path, "metadata.json")

        assert os.path.isfile(md_file)
        assert os.path.isfile(json_file)

        with open(md_file, encoding="utf8") as file_:
            content = file_.read()
            expect = """---
name: test-data
---
"""
            assert content == expect

        with open(json_file, encoding="utf8") as file_:
            content = file_.read()
            expect = """{"name": "test-data"}"""
            assert content == expect


def test_add_to_path():
    """Test using a context manager to temporarily add to the system path."""
    path = "/path/to/nowhere"
    current_path = list(sys.path)
    assert sys.path[0] != path

    with metadata.add_to_path(path):
        assert sys.path[0] == path

    assert sys.path[0] != path
    assert current_path == sys.path


def test_get_metadata_from_json():
    """Test getting metadata from a json file."""

    output = {
        "name": "name",
        "version": "version",
        "description": "description",
        "homepage": "homepage",
        "repository": {"url": "repository"},
        "bugs": {"url": "issuesurl"},
        "license": "license",
        "author": "maintainers",
    }

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as fd:
        fd.write(json.dumps(output))
        fd.flush()

        # get the metadata
        md = metadata.get_metadata_from_json(fd.name)

        # check contributors is blank
        assert md["contributors"] == ""
        del md["contributors"]

        # check all values are the same as their keys
        for k, v in md.items():
            assert k == v


def test_get_metadata_from_distribution():
    """Test getting metadata from a distribution.

    The package itself must be installed in the virtualenv.
    """
    result = metadata.get_metadata_from_distribution("sphinx-bluebrain-theme")
    assert set(result) == {
        "contributors",
        "description",
        "homepage",
        "issuesurl",
        "license",
        "maintainers",
        "name",
        "repository",
        "version",
    }
    # ignore version because not fixed
    del result["version"]
    assert result == {
        "name": "sphinx-bluebrain-theme",
        "description": "Blue Brain Project theme for Sphinx",
        "homepage": "https://github.com/BlueBrain/sphinx-bluebrain-theme",
        "license": "MIT License",
        "maintainers": "Blue Brain Project, EPFL",
        "repository": "https://github.com/BlueBrain/sphinx-bluebrain-theme",
        "issuesurl": "https://github.com/BlueBrain/sphinx-bluebrain-theme/issues",
        "contributors": None,
    }
