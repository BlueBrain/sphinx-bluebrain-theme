"""Functions to inject additional context for the translation from mkdocs to sphinx."""

import datetime
from collections import defaultdict

import sphinx
import sphinx.util.logging

from sphinx_bluebrain_theme.utils.search_builder import SearchIndexBuilder
from sphinx_bluebrain_theme.utils.navutils import Page


logger = sphinx.util.logging.getLogger(__name__)


def build_adjacent_page(data):
    """Builds an adjacent page with the minimum required data."""
    if not data:
        return None

    page = Page()
    page.title = data.get("title", "")
    page.url = data.get("link", "")

    return page


def build_page(con, pagename):
    """Builds a mkdocs compatible page object and returns it.

    Args:
        con (dict): A dictionary of the context used to build the page.
        pagename (str): The current page name.

    Returns:
        A dictionary representing the page.
    """
    # add the page context variable
    page = Page()

    # Ensure this is set before .parents otherwise it will try to set recursively.
    page.active = True

    page.previous_page = build_adjacent_page(con["prev"])
    page.next_page = build_adjacent_page(con["next"])
    page.toc = con["localtoc"] or []
    page.url = pagename + ".html"
    page.edit_url = None
    page.content = con["body"] or ""
    page.meta = con["meta"]
    page.title = con["title"]
    page.canonical_url = con["pageurl"]
    page.ancestors = con["parents"]

    pm = page.meta

    if pm:
        if "authors" in pm:
            pm["authors"] = pm["authors"].split(",")
        if "source" in pm:
            pm["source"] = pm["source"].split(",")
        if "redirect" in pm:
            pm["redirect"] = con["pathto"](pm["redirect"])

    page.is_homepage = con["pagename"] == con["master_doc"]

    return page


def build_font(con):
    """Build font from context."""
    fonts = {"text": con["theme_font_text"], "code": con["theme_font_code"]}
    font = con["theme_use_google_fonts"] is True

    if font and any(fonts.values()):
        font = {"text": fonts["text"] or "", "code": fonts["code"] or ""}

    return font


def build_extra(con, lang):
    """Build the extra from context."""
    extra = {
        "repo_icon": con["theme_repo_icon"],
        "social": con["theme_social"],
        "disqus": None,  # disqus not currently supported
        "manifest": con["theme_manifest"],
    }

    # default tokenizer for english splits on hypens,
    # preserve them instead
    if lang == "en":
        extra["search"] = {"tokenizer": r"[\s]+"}

    return extra


def build_config(con):
    """
    This fuctions builds a mkdocs compatible config entry.

    Args:
        con (dict): A dictionary of the context used to build the page.

    Returns:
        A dictionary representing the config for the page.
    """
    # do this first so we can set the search tokenizer in
    # extra.search.tokenizer
    lang = con["language"] or "en"

    # add config context variable
    extra = build_extra(con, lang)
    font = build_font(con)

    config = {
        "extra_css": [],
        "site_name": con["docstitle"],
        "theme": {
            "feature": {"tabs": con["theme_feature_tabs"]},
            "palette": {
                "primary": con["theme_palette_primary"],
                "accent": con["theme_palette_accent"],
            },
            "font": font,
            "language": lang,
            # note we use 'assets/' below since the urls use the url filter
            # which will automatically clean up and convert '_static/'
            "logo": "assets/" + (con["logo"] or con["theme_logo"])
            if con["logo"] or con["theme_logo"]
            else {"icon": con["theme_logo_icon"]},
            "favicon": "assets/" + con["favicon"] if con["favicon"] else "",
        },
        "repo_url": con["theme_repo_url"],
        "repo_name": con["theme_repo_name"],
        "copyright": con["copyright"],
        "title_url": con["pathto"](con["master_doc"]),
        "extra": extra,
        "site_url": con["theme_logo_url"] or con["pathto"](con["master_doc"]),
        "site_author": con["theme_site_author"],
        "site_description": con["theme_site_description"],
        "plugins": {"search"},  # need to include for search bar to show
    }

    return config


# pylint: disable=unused-argument
def inject_context_variables(app, pagename, templatename, context, doctree):
    """This function injects the additional context for the translation from mkdocs to sphinx.

    Args:
        app: The Sphinx application.
        pagename (str): The name of the current page.
        templatename (str): The name of the template used to render the page.
        context (dict): The context passed to the page template for rendering.
        doctree: A doctree when the page is created from reST documents.
    """
    con = defaultdict(lambda: None)
    con.update(context)

    extra_context = {}

    # build the page
    extra_context["page"] = build_page(con, pagename)

    # build the config context entry
    extra_context["config"] = build_config(con)

    # fix the nav variable
    extra_context["nav"] = con["globaltoc"]

    # inject new context
    context.update(extra_context)

    # cleanup some defaults which are useful for BBP
    bbp_context_cleanup(context)

    # handle adding the page to the search index
    search_index = app.builder.globalcontext.get("search_index", SearchIndexBuilder())
    search_index.add_page_to_index(context["page"])
    app.builder.globalcontext["search_index"] = search_index

    # remove the "title" context variable as it is now in page.title
    # and conflicts with nav_item.title template code
    if "title" in context:
        del context["title"]


def bbp_context_cleanup(context):
    """Cleans up some theme defaults which are required for BBP projects.

    theme.conf variables are all strings, but templates expect
    other types to be passed (lists and dicts).

    Args:
        context (dict): The context passed to the page template for rendering.
    """
    # do some convenience updates for BBP defaults
    if isinstance(context["theme_address"], str):
        context["theme_address"] = context["theme_address"].strip().split("\n")

    if isinstance(context["theme_social"], str):
        pairs = [p.split(",") for p in context["theme_social"].strip().split("\n")]
        social = [{k: v.strip() for k, v in zip(("type", "link"), p)} for p in pairs]
        # we need to update the constructed context
        context["config"]["extra"]["social"] = social

    if "copyright" in context and context["copyright"]:
        logger.warning(
            "you have defined 'copyright' in your conf.py, "
            "the default Blue Brain project copyright will be used."
        )

    context["config"]["copyright"] = (
        "&copy; Blue Brain Project/EPFL 2005-%s. All rights reserved."
        % datetime.datetime.now().year
    )
