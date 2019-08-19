"""Tests for metadata generation utilities."""

from contextlib import contextmanager
import json
import os
import shutil
import sys
import tempfile

from nose import tools as nt  # pylint: disable=import-error

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
        nt.eq_(os.getcwd(), "/")

    nt.eq_(os.getcwd(), current_wd)


def test_write_metadata_files():
    """Test that the metadata files are written and their content is correct."""
    with setup_tempdir("docs-path") as docs_path:
        metadata_dict = {"name": "test-data"}
        metadata.write_metadata(metadata_dict, docs_path)

        md_file = os.path.join(docs_path, "metadata.md")
        json_file = os.path.join(docs_path, "metadata.json")

        nt.assert_true(os.path.isfile(md_file))
        nt.assert_true(os.path.isfile(json_file))

        with open(md_file) as file_:
            content = file_.read()
            expect = """---
name: test-data
---
"""
            nt.eq_(content, expect)

        with open(json_file) as file_:
            content = file_.read()
            expect = """{"name": "test-data"}"""
            nt.eq_(content, expect)


def test_add_to_path():
    """Test using a context manager to temporarily add to the system path."""
    path = "/path/to/nowhere"
    current_path = list(sys.path)
    nt.assert_not_equal(sys.path[0], path)

    with metadata.add_to_path(path):
        nt.eq_(sys.path[0], path)

    nt.assert_not_equal(sys.path[0], path)
    nt.eq_(current_path, sys.path)


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

        # check contributors is None
        nt.assert_is_none(md["contributors"])
        del md["contributors"]

        # check all values are the same as their keys
        for k, v in md.items():
            nt.eq_(k, v)
