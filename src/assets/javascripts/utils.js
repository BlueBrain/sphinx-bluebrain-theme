
(() => {
  // find the first part of path after origin
  const firstPartReg = new RegExp('^\/([^\/]+).*$');
  const bbpCatalogBase = 'documentation';
  const readthedocsOrigin = 'readthedocs.io';

  function processHomeUrl() {
    const prunedPath = firstPartReg.exec(window.location.pathname);
    if (prunedPath.length < 2) return '#';

    const basePath = prunedPath[1];
    if (basePath === bbpCatalogBase) {
      return `${window.location.origin}/${basePath}`;
    }
    if (window.location.host.includes(readthedocsOrigin)) {
      return `${window.location.origin}`; // go to root
    }
    return '#';
  }

  const redirectUrl = processHomeUrl();
  const anchorElem = document.getElementById('homepageLink');
  anchorElem.href = redirectUrl;
})();
