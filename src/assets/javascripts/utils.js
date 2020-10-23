
(function () {
  function processHomeUrl() {
    // will find the first part of path after url
    const firstPartReg = new RegExp('^\/([^\/]+).*$');
    const prunedPath = firstPartReg.exec(window.location.pathname);

    if (!firstPartReg || prunedPath.length < 2) return;

    const redirectUrl = `${window.location.origin}/${prunedPath[1]}`;

    const anchorElem = document.getElementById('homepageLink');
    anchorElem.href = redirectUrl;
  }
  processHomeUrl();
})();
