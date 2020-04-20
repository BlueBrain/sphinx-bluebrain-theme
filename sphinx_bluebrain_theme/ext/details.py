"""This extension provides collapsible areas on an html page."""

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


class details_node(nodes.General, nodes.Element):
    """Details node."""


def visit_details_node(self, node):
    """Create the opening details node html."""
    attrs = {}

    if node.get("open", False):
        attrs["open"] = ""

    self.body.append(
        self.starttag(node, "details", CLASS=" ".join(node["classes"]), **attrs)
    )


def depart_details_node(self, node):
    """Close the details html."""
    del node
    self.body.append("</details>")


class summary_node(nodes.General, nodes.Element):
    """Summary node."""


def visit_summary_node(self, node):
    """Create the opening summary node html."""
    self.body.append(self.starttag(node, "summary", "", CLASS=""))


def depart_summary_node(self, node):
    """Close the summary html."""
    del node
    self.body.append("</summary>")


class Details(SphinxDirective):
    """A container for details/summary."""

    has_content = True
    required_arguments = 1
    final_argument_whitespace = True
    option_spec = {"class": directives.class_option, "open": directives.flag}

    def run(self):
        """Insert correct nodes for directive."""
        self.assert_has_content()

        node = details_node()

        node["classes"] += self.options.get("class", [])
        node["open"] = "open" in self.options

        summary = summary_node()
        summary += nodes.Text(self.arguments[-1])
        node += summary

        self.add_name(node)

        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]


def setup(app):
    """Register nodes and directives for use."""
    app.add_node(details_node, html=(visit_details_node, depart_details_node))
    app.add_node(summary_node, html=(visit_summary_node, depart_summary_node))
    app.add_directive("details", Details)
