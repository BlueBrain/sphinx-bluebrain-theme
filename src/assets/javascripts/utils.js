
(() => {

  /*
    Script to toggle show or hide the 'home' button depending if the it runs in
    our internal documentation or external such as ReadTheDocs (in which case the home makes no sense)

    Documentation could be served under (epfl.ch + documentation is always there)
    https://bbp.epfl.ch/documentation/all.html
    https://bbpteam.epfl.ch/documentation/all.html
  */
  const bbpOrigin = "epfl.ch";
  const bbpCatalogBase = "documentation";
  const bbpDocReg = new RegExp(`${bbpOrigin}\/${bbpCatalogBase}`);

  const homeBtnContainerId = "homeBtnContainer";
  const homeButtonId = "homepageLink";

  if (!bbpDocReg.test(window.location.href)) {
    const homeContainer = document.getElementById(homeBtnContainerId);
    if (!homeContainer) { return; }
    homeContainer.style.display = "none";
    return;
  }

  const redirectUrl = `${window.location.origin}/${bbpCatalogBase}`;
  const anchorElem = document.getElementById(homeButtonId);
  if (!anchorElem) { return; }
  anchorElem.href = redirectUrl;
})();
