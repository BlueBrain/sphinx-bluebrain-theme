"""This extension provides tabbed code areason an html page."""

from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from sphinx.directives.code import CodeBlock, LiteralInclude


class CodeTabMixin:
    """Common code for code-block and literal-include type tabs."""

    def run_mixin(self, inner):
        """Insert correct nodes for code tabs."""
        # tab title is the second arg
        title = self.arguments.pop()

        # tab_ids start from 1, so increment at start
        self.env.tab_group_tab_id += 1

        # build the tab_id
        group_name = self.env.tab_group_name
        tab_id_int = self.env.tab_group_tab_id
        tab_id = "%s_%s" % (group_name, tab_id_int)

        node = nodes.container()
        node["classes"].append("superfences-content")

        self.add_name(node)

        # include the node for the actual code
        node += inner

        # create the input node for the tab
        inp = tab_node(ids=[tab_id])
        inp.tagname = "input"
        inp["attrs"] = {"type": "radio", "name": group_name}
        if self.env.tab_group_tab_id == 1:
            inp["attrs"]["checked"] = "checked"

        # create the label
        lab = tab_node()
        lab.tagname = "label"
        lab["attrs"] = {"for": tab_id}

        # add text to the label
        txt = nodes.Text(title)
        lab += txt

        return [inp, lab, node]


class CodeTab(CodeTabMixin, CodeBlock):
    """Code tab convenience class to avoid extra directives."""

    required_arguments = 2

    def run(self):
        """Run the CodeTab including mixin."""
        inner = super(CodeTab, self).run()
        return self.run_mixin(inner)


class LiteralTab(CodeTabMixin, LiteralInclude):
    """Literal include convenience class."""

    required_arguments = 2

    def run(self):
        """Run the LiteralTab including mixin."""
        inner = super(LiteralTab, self).run()
        return self.run_mixin(inner)


class tab_node(nodes.General, nodes.Element):
    """Custom tab node that can be used for different tags."""


def visit_tab_node(self, node):
    """Create the opening tab node html including data attributes."""
    attrs = node.get("attrs", {})
    self.body.append(self.starttag(node, node.tagname, "", CLASS="", **attrs))


def depart_tab_node(self, node):
    """Close the tab html."""
    self.body.append("</%s>" % node.tagname)


class TabGroup(SphinxDirective):
    """A container for multiple tabs."""

    has_content = True
    required_arguments = 0
    optional_arguments = 0

    def run(self):
        """Insert correct nodes for directive."""
        self.assert_has_content()
        text = "\n".join(self.content)

        self.env.tab_group_id = getattr(self.env, "tab_group_id", 0) + 1
        self.env.tab_group_name = "__tab_%s" % self.env.tab_group_id
        self.env.tab_group_tab_id = 0
        node = nodes.container(text)
        node["classes"].append("superfences-tabs")

        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]


def setup(app):
    """Register nodes and directives for use."""
    app.add_node(tab_node, html=(visit_tab_node, depart_tab_node))
    app.add_directive("codetab", CodeTab)
    app.add_directive("literaltab", LiteralTab)
    app.add_directive("tabgroup", TabGroup)
