"""
Test for the conversion of files.
"""

from collections import defaultdict

# pylint: disable=import-error
from nose import tools as nt
from mkdocs2sphinx.convert_files import do_replacements, prepend_license


def test_do_replacements():
    """
    Test replacements with text blocks.
    """
    stats = defaultdict(int)

    text = """This is some text
<a>specific_text</a>
Some text embedded in a <hello> line"""

    rep = {"specific_text": "first", "<hello>": "goodbye"}

    text = do_replacements(text, rep, stats)

    result = """This is some text
<a>first</a>
Some text embedded in a goodbye line"""

    nt.assert_equal(text, result)


def test_prepend_license():
    """
    Test the prepending of the license to text.
    """

    lic = "LICENSE"
    text = """This is some test
text that will be used to check licenses."""

    # first test an unknown file type
    lictext = prepend_license((lic,), text, "hello.py")
    nt.assert_equal(lictext, text)

    # test css
    lictext = prepend_license((lic,), text, "hello.css")
    nt.assert_true(lictext.startswith("/*\n * LICENSE"))
