"""
Test for the manipulation of Jinja blocks in text using the
mkdocs2sphinx module functions.
"""

import pytest  # pylint: disable=unused-import
from mkdocs2sphinx import clear_blocks as cb


def test_block_list():
    """
    Test the construction of the list of blocks from text.
    """

    text = """Outer text
{% block outer %}
Inner text
{% block inner %}
Innermost text
{% endblock inner %}
Additional text
And even more text
{% endblock %}
"""

    bl = cb.build_block_list(text)

    # check the first block opening
    assert bl[0]["type"] == "block"
    assert bl[0]["block_name"] == "outer"

    # inner block
    assert bl[1]["type"] == "block"
    assert bl[1]["block_name"] == "inner"

    # inner endblock
    assert bl[2]["type"] == "endblock"
    assert bl[2]["block_name"] == "inner"

    # outer endblock
    assert bl[3]["type"] == "endblock"
    assert bl[3]["block_name"] is None


def test_block_clearing():
    """
    Test the clearing of blocks with various options.
    """

    text = """Outer text
{% block outer %}
Inner text
{% block inner %}
Innermost text
{% endblock inner %}
Additional text
And even more text
{% endblock %}
"""

    # remove inner content
    tx = cb.remove_block(text, "outer", keep_nested=False)
    assert (
        tx
        == """Outer text
{% block outer %}{% endblock %}
"""
    )

    # remove inner content, keeping nested
    tx = cb.remove_block(text, "outer", keep_nested=True)
    assert (
        tx
        == """Outer text
{% block outer %}{% block inner %}
Innermost text
{% endblock inner %}{% endblock %}
"""
    )

    # remove innermost content
    tx = cb.remove_block(text, "inner", keep_nested=True)
    assert (
        tx
        == """Outer text
{% block outer %}
Inner text
{% block inner %}{% endblock inner %}
Additional text
And even more text
{% endblock %}
"""
    )

    # try to remove a non-existant block
    tx = cb.remove_block(text, "imaginary", keep_nested=True)
    assert text == tx


def test_block_clearing_multiple():
    """
    Test the clearing of multiple blocks.
    """

    text = """Outer text
{% block outer %}
Inner text
{% block inner %}
Innermost text
{% endblock inner %}
Additional text
And even more text
{% endblock %}
"""

    # remove inner content
    tx = cb.remove_blocks(text, ["outer", "inner"], keep_nested=True)
    assert (
        tx
        == """Outer text
{% block outer %}{% block inner %}{% endblock inner %}{% endblock %}
"""
    )
