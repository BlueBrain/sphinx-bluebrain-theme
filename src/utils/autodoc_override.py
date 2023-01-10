"""Override autodoc output to wrap in a div."""

from docutils import nodes
import sphinx.ext.autodoc as sea
from sphinx.ext.autodoc.directive import AutodocDirective


class AutodocDirectiveOverride(AutodocDirective):
    """Extends AutodocDirective to wrap output in a div."""

    def run(self):
        """Wrap the autodoc output in a div with autodoc class."""
        result = super().run()
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

        # These are found by looking for class members named `objtype` in
        # sphinx/ext/autodoc/__init__.py
        documenters = [
            "ModuleDocumenter",
            "FunctionDocumenter",
            "DecoratorDocumenter",
            "ClassDocumenter",
            "ExceptionDocumenter",
            "DataDocumenter",
            "MethodDocumenter",
            "AttributeDocumenter",
            "PropertyDocumenter",
            # removed in https://github.com/sphinx-doc/sphinx/pull/10700/files
            # and released in v6.1.2
            "NewTypeDataDocumenter",
            "NewTypeAttributeDocumenter",
        ]
        allowed_missing = {
            "NewTypeDataDocumenter",
            "NewTypeAttributeDocumenter",
        }

        for documentor_name in documenters:
            try:
                documentor = getattr(sea, documentor_name)
            except AttributeError as e:
                if documentor_name in allowed_missing:
                    continue
                raise e

            app.add_directive(
                "auto" + documentor.objtype, AutodocDirectiveOverride, override=True
            )
