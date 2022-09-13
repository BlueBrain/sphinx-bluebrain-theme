
(function () {
  const firstPartReg = new RegExp('^\/([^\/]+).*$');
  const bbpCatalogBase = 'documentation';
  const readthedocsUrl = 'readthedocs.io';

  function processHomeUrl() {
    // will find the first part of path after url
    const prunedPath = firstPartReg.exec(window.location.pathname);
    if (prunedPath.length < 2) return '#';

    const basePath = prunedPath[1];
    if (basePath === bbpCatalogBase) {
      return `${window.location.origin}/${basePath}`;
    }
    if (window.location.host.includes(readthedocsUrl)) {
      return `${window.location.origin}`; // go to root
    }
    return '#';
  }

  const redirectUrl = processHomeUrl();
  const anchorElem = document.getElementById('homepageLink');
  anchorElem.href = redirectUrl;
})();
