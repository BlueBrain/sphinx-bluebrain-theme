"""Override autodoc output to wrap in a div."""

from docutils import nodes
import sphinx.ext.autodoc as sea
from sphinx.ext.autodoc.directive import AutodocDirective


class AutodocDirectiveOverride(AutodocDirective):
    """Extends AutodocDirective to wrap output in a div."""

    def run(self):
        """Wrap the autodoc output in a div with autodoc class."""
        result = super(AutodocDirectiveOverride, self).run()
        container = nodes.container()
        container["classes"].append("autodoc-output")
        container += result
        return [container]


def add_autodoc_override(app):
    """Override the autodoc definitions to wrap them in a div."""
    if "sphinx.ext.autodoc" in app.extensions:
        # this will override the normal autodoc directive if required. See:
        # https://github.com/sphinx-doc/sphinx/blob/master/sphinx/ext/autodoc/__init__.py#L1464
        # https://github.com/sphinx-doc/sphinx/blob/15bc5a32bb0b78b432803e55fffa10c801182c75/sphinx/application.py#L996
        documenters = [
            sea.ModuleDocumenter,
            sea.ClassDocumenter,
            sea.ExceptionDocumenter,
            sea.DataDocumenter,
            sea.FunctionDocumenter,
            sea.DecoratorDocumenter,
            sea.MethodDocumenter,
            sea.AttributeDocumenter,
            sea.InstanceAttributeDocumenter,
        ]

        for d in documenters:
            app.add_directive(
                "auto" + d.objtype, AutodocDirectiveOverride, override=True
            )
