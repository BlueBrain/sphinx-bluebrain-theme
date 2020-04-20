/*
 * Copyright (c) 2016-2019 Martin Donath <martin.donath@squidfunk.com>
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to
 * deal in the Software without restriction, including without limitation the
 * rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
 * sell copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 * IN THE SOFTWARE.
 */
!function(e,t){for(var n in t)e[n]=t[n]}(window,function(n){var r={};function o(e){if(r[e])return r[e].exports;var t=r[e]={i:e,l:!1,exports:{}};return n[e].call(t.exports,t,t.exports,o),t.l=!0,t.exports}return o.m=n,o.c=r,o.d=function(e,t,n){o.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},o.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},o.t=function(t,e){if(1&e&&(t=o(t)),8&e)return t;if(4&e&&"object"==typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(o.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var r in t)o.d(n,r,function(e){return t[e]}.bind(null,r));return n},o.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return o.d(t,"a",t),t},o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},o.p="",o(o.s=11)}({11:function(e,t,n){"use strict";n.r(t);n(12)},12:function(e,t){var n;(function(i,d,p){function y(e,t){return typeof e===t}function s(e){var t=S.className,n=c._config.classPrefix||"";if(b&&(t=t.baseVal),c._config.enableJSClass){var r=new RegExp("(^|\\s)"+n+"no-js(\\s|$)");t=t.replace(r,"$1"+n+"js$2")}c._config.enableClasses&&(0<e.length&&(t+=" "+n+e.join(" "+n)),b?S.className.baseVal=t:S.className=t)}function a(e,t){if("object"==typeof e)for(var n in e)v(e,n)&&a(n,e[n]);else{var r=(e=e.toLowerCase()).split("."),o=c[r[0]];if(2===r.length&&(o=o[r[1]]),void 0!==o)return c;t="function"==typeof t?t():t,1===r.length?c[r[0]]=t:(!c[r[0]]||c[r[0]]instanceof Boolean||(c[r[0]]=new Boolean(c[r[0]])),c[r[0]][r[1]]=t),s([(t&&!1!==t?"":"no-")+r.join("-")]),c._trigger(e,t)}return c}function m(){return"function"!=typeof d.createElement?d.createElement(arguments[0]):b?d.createElementNS.call(d,"http://www.w3.org/2000/svg",arguments[0]):d.createElement.apply(d,arguments)}function o(e,t,n,r){var o,i,s,a,l,u="modernizr",f=m("div"),c=((l=d.body)||((l=m(b?"svg":"body")).fake=!0),l);if(parseInt(n,10))for(;n--;)(s=m("div")).id=r?r[n]:u+(n+1),f.appendChild(s);return(o=m("style")).type="text/css",o.id="s"+u,(c.fake?c:f).appendChild(o),c.appendChild(f),o.styleSheet?o.styleSheet.cssText=e:o.appendChild(d.createTextNode(e)),f.id=u,c.fake&&(c.style.background="",c.style.overflow="hidden",a=S.style.overflow,S.style.overflow="hidden",S.appendChild(c)),i=t(f,e),c.fake?(c.parentNode.removeChild(c),S.style.overflow=a,S.offsetHeight):f.parentNode.removeChild(f),!!i}function l(e){return e.replace(/([A-Z])/g,function(e,t){return"-"+t.toLowerCase()}).replace(/^ms-/,"-ms-")}function h(e,t){var n=e.length;if("CSS"in i&&"supports"in i.CSS){for(;n--;)if(i.CSS.supports(l(e[n]),t))return!0;return!1}if("CSSSupportsRule"in i){for(var r=[];n--;)r.push("("+l(e[n])+":"+t+")");return o("@supports ("+(r=r.join(" or "))+") { #modernizr { position: absolute; } }",function(e){return"absolute"===function(e,t,n){var r;if("getComputedStyle"in i){r=getComputedStyle.call(i,e,t);var o=i.console;null!==r?n&&(r=r.getPropertyValue(n)):o&&o[o.error?"error":"log"].call(o,"getComputedStyle returning null, its possible modernizr test results are inaccurate")}else r=!t&&e.currentStyle&&e.currentStyle[n];return r}(e,null,"position")})}return p}function u(e,t){return function(){return e.apply(t,arguments)}}function r(e,t,n,r,o){var i=e.charAt(0).toUpperCase()+e.slice(1),s=(e+" "+w.join(i+" ")+i).split(" ");return y(t,"string")||y(t,"undefined")?function(e,t,n,r){function o(){s&&(delete T.style,delete T.modElem)}if(r=!y(r,"undefined")&&r,!y(n,"undefined")){var i=h(e,n);if(!y(i,"undefined"))return i}for(var s,a,l,u,f,c=["modernizr","tspan","samp"];!T.style&&c.length;)s=!0,T.modElem=m(c.shift()),T.style=T.modElem.style;for(l=e.length,a=0;a<l;a++)if(u=e[a],f=T.style[u],!!~(""+u).indexOf("-")&&(u=u.replace(/([a-z])-([a-z])/g,function(e,t,n){return t+n.toUpperCase()}).replace(/^-/,"")),T.style[u]!==p){if(r||y(n,"undefined"))return o(),"pfx"!==t||u;try{T.style[u]=n}catch(e){}if(T.style[u]!==f)return o(),"pfx"!==t||u}return o(),!1}(s,t,r,o):function(e,t,n){var r;for(var o in e)if(e[o]in t)return!1===n?e[o]:y(r=t[e[o]],"function")?u(r,n||t):r;return!1}(s=(e+" "+P.join(i+" ")+i).split(" "),t,n)}function e(e,t,n){return r(e,p,p,t,n)}var f=[],t={_version:"3.7.1",_config:{classPrefix:"",enableClasses:!0,enableJSClass:!0,usePrefixes:!0},_q:[],on:function(e,t){var n=this;setTimeout(function(){t(n[e])},0)},addTest:function(e,t,n){f.push({name:e,fn:t,options:n})},addAsyncTest:function(e){f.push({name:null,fn:e})}},c=function(){};c.prototype=t,c=new c;var v,n,g=[],S=d.documentElement,b="svg"===S.nodeName.toLowerCase();v=y(n={}.hasOwnProperty,"undefined")||y(n.call,"undefined")?function(e,t){return t in e&&y(e.constructor.prototype[t],"undefined")}:function(e,t){return n.call(e,t)},t._l={},t.on=function(e,t){this._l[e]||(this._l[e]=[]),this._l[e].push(t),c.hasOwnProperty(e)&&setTimeout(function(){c._trigger(e,c[e])},0)},t._trigger=function(e,t){if(this._l[e]){var n=this._l[e];setTimeout(function(){var e;for(e=0;e<n.length;e++)(0,n[e])(t)},0),delete this._l[e]}},c._q.push(function(){t.addTest=a}),c.addTest("json","JSON"in i&&"parse"in JSON&&"stringify"in JSON),c.addTest("svg",!!d.createElementNS&&!!d.createElementNS("http://www.w3.org/2000/svg","svg").createSVGRect);var C=t.testStyles=o;c.addTest("checked",function(){return C("#modernizr {position:absolute} #modernizr input {margin-left:10px} #modernizr :checked {margin-left:20px;display:block}",function(e){var t=m("input");return t.setAttribute("type","checkbox"),t.setAttribute("checked","checked"),e.appendChild(t),20===t.offsetLeft})}),c.addTest("target",function(){var e=i.document;if(!("querySelectorAll"in e))return!1;try{return e.querySelectorAll(":target"),!0}catch(e){return!1}}),c.addTest("dataset",function(){var e=m("div");return e.setAttribute("data-a-b","c"),!(!e.dataset||"c"!==e.dataset.aB)}),c.addTest("details",function(){var t,n=m("details");return"open"in n&&(C("#modernizr details{display:block}",function(e){e.appendChild(n),n.innerHTML="<summary>a</summary>b",t=n.offsetHeight,n.open=!0,t=t!==n.offsetHeight}),t)}),c.addTest("fetch","fetch"in i);var _="Moz O ms Webkit",w=t._config.usePrefixes?_.split(" "):[];t._cssomPrefixes=w;var x={elem:m("modernizr")};c._q.push(function(){delete x.elem});var T={style:x.elem.style};c._q.unshift(function(){delete T.style});var P=t._config.usePrefixes?_.toLowerCase().split(" "):[];t._domPrefixes=P,t.testAllProps=r,t.testAllProps=e;var j="CSS"in i&&"supports"in i.CSS,O="supportsCSS"in i;c.addTest("supports",j||O),c.addTest("csstransforms3d",function(){return!!e("perspective","1px",!0)}),function(){var e,t,n,r,o,i;for(var s in f)if(f.hasOwnProperty(s)){if(e=[],(t=f[s]).name&&(e.push(t.name.toLowerCase()),t.options&&t.options.aliases&&t.options.aliases.length))for(n=0;n<t.options.aliases.length;n++)e.push(t.options.aliases[n].toLowerCase());for(r=y(t.fn,"function")?t.fn():t.fn,o=0;o<e.length;o++)1===(i=e[o].split(".")).length?c[i[0]]=r:(!c[i[0]]||c[i[0]]instanceof Boolean||(c[i[0]]=new Boolean(c[i[0]])),c[i[0]][i[1]]=r),g.push((r?"":"no-")+i.join("-"))}}(),s(g),delete t.addTest,delete t.addAsyncTest;for(var z=0;z<c._q.length;z++)c._q[z]();i.Modernizr=c})(n=window,document),e.exports=n.Modernizr}}));