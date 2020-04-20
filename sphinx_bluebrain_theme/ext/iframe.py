"""This extension provides iframes for embedding html."""

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


class iframe_node(nodes.General, nodes.Element):
    """iframe node."""


def visit_iframe_node(self, node):
    """Create the opening iframe node html."""
    attrs = node.get("attrs", {})

    self.body.append(
        self.starttag(node, "iframe", CLASS=" ".join(node["classes"]), **attrs)
    )


def depart_iframe_node(self, node):
    """Close the iframe html."""
    del node
    self.body.append("</iframe>")


class Iframe(SphinxDirective):
    """A container for iframe."""

    has_content = False
    required_arguments = 1
    final_argument_whitespace = False
    option_spec = {"class": directives.class_option}

    def run(self):
        """Insert correct nodes for directive."""
        node = iframe_node()

        node["classes"] += ["sphinx-iframe"]
        node["classes"] += self.options.get("class", [])

        node["attrs"] = {"src": self.arguments[0], "scrolling": "no"}

        self.add_name(node)

        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]


def setup(app):
    """Register nodes and directives for use."""
    app.add_node(iframe_node, html=(visit_iframe_node, depart_iframe_node))
    app.add_directive("iframe", Iframe)
