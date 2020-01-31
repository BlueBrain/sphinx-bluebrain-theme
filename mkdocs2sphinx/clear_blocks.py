"""This module is used to clear the contents of Jinja blocks within given source text."""

import re


def build_block_list(src_text):
    """Constructs a list of 'block'/'endblock' matches, ordered by location within the source text.

    Args:
        src_text (str): The string to construct the match list from.

    Returns:
        list: A list of 'block' and 'endblock' regex matches ordered by their
        location in the ``src_text``.
    """
    # make these non-greedy to account for situation where there are two
    # blocks immediately adjacent
    start_matches = re.finditer(r"{% block (.*?) %}", src_text)
    end_matches = re.finditer(r"{% endblock\s*(.*?) %}", src_text)

    match_list = [
        {"type": t, "match": m, "block_name": m.groups()[0] or None}
        for t, it in zip(("block", "endblock"), (start_matches, end_matches))
        for m in it
    ]

    # sort by location in the text
    match_list.sort(key=lambda v: v["match"].start())

    return match_list


def remove_block(src_text, block_name_to_remove, keep_nested=True):
    """Removes the contents of a Jinja block specified by name.

    Optionally retaining any blocks nested within the block.

    Args:
        src_text (str): The text to remove the block contents from.
        block_name_to_remove (str): The block name to remove content from.
        keep_nested (bool): If true, any blocks within the target block (and
            their contents) will be retained.

    Returns:
        str: The text with the block contents cleared.
    """
    # keep this inside this function as the src_text may be different for each
    # call (due to previous block clearing), so we need to rebuild each time
    match_list = build_block_list(src_text)

    do_skip = True
    start = None
    end = None

    keep_list = []

    nesting_level = 0

    for match in match_list:
        is_target = match["block_name"] == block_name_to_remove

        if do_skip and not is_target:
            # we haven't found an instance of the target block yet
            continue

        if match["type"] == "block" and is_target:
            # we've found a target block so we need to take note of all
            # blocks/endblocks from here on
            do_skip = False
            start = match["match"]
        elif match["type"] == "block":
            # we only need to note the first level of nested blocks since if
            # their content is retained it will included any doubly nested
            # blocks
            if nesting_level == 0 and keep_nested:
                keep_list.append(match["match"])
            nesting_level += 1
        elif match["type"] == "endblock" and nesting_level == 0:
            # if we're back to an endblock matching the target, then we're done
            end = match["match"]
            break
        elif match["type"] == "endblock":
            # we only need to note the first level of nested blocks since if
            # their content is retained it will included any doubly nested
            # blocks
            if nesting_level == 1 and keep_nested:
                keep_list.append(match["match"])
            nesting_level -= 1

    if start is None or end is None:
        # no instances of the target block found, return original text
        return src_text

    # start with text prior to target block, note .end() is required because
    # we want to keep the block tag
    tmp_text = src_text[: start.end()]

    if keep_list:
        # if there are any nested blocks, keep their contents
        for m_start, m_end in zip(keep_list[:-1], keep_list[1:]):
            tmp_text += src_text[m_start.start() : m_end.end()]

    # append all text after the matched endblock, note .start() is required
    # because we want to keep the block tag
    tmp_text += src_text[end.start() :]

    return tmp_text


def remove_blocks(src_text, block_names, keep_nested=True):
    """Removes the content of a series of blocks from the given source text.

    Args:
        src_text (str): The text to remove the block contents from.
        block_names (list): A list of strings of the block names whose content
            will be removed.

    Returns:
        str: The text with blocks cleared.
    """
    for name in block_names:
        src_text = remove_block(src_text, name, keep_nested)

    return src_text
