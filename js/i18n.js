/* =============================================================
   DERIN AKADEMI - i18n System v2
   Loads translations from /locales/tr.json & /locales/en.json
   Usage : daToggleLang()  /  daSetLang('en')
   Stores: localStorage key 'da-lang'  ('tr' | 'en')
   Attrs : data-i18n            => sets textContent
           data-i18n-html       => sets innerHTML
           data-i18n-placeholder=> sets placeholder attr
           data-i18n-title      => sets textContent on <title>
============================================================= */

(function () {
  'use strict';

  /* Detect the correct base path
     Root pages  (/index.html)          => 'locales/'
     Sub-pages   (/egitimler/foo.html)  => '../locales/'  */
  var pathParts = window.location.pathname.split('/').filter(Boolean);
  var BASE = pathParts.length >= 2 ? '../locales/' : 'locales/';

  /* In-memory cache { tr: {...}, en: {...} } */
  var _cache = {};

  /* Load a locale JSON file (with caching) */
  function loadLocale(lang) {
    if (_cache[lang]) return Promise.resolve(_cache[lang]);
    return fetch(BASE + lang + '.json?v=2')
      .then(function(r) {
        if (!r.ok) throw new Error('Cannot load ' + lang + '.json');
        return r.json();
      })
      .then(function(data) {
        _cache[lang] = data;
        return data;
      });
  }

  /* Apply a translations dict to the page */
  function applyTranslations(dict, lang) {
    document.querySelectorAll('[data-i18n]').forEach(function(el) {
      var key = el.getAttribute('data-i18n');
      if (dict[key] !== undefined) el.textContent = dict[key];
    });
    document.querySelectorAll('[data-i18n-html]').forEach(function(el) {
      var key = el.getAttribute('data-i18n-html');
      if (dict[key] !== undefined) el.innerHTML = dict[key];
    });
    document.querySelectorAll('[data-i18n-placeholder]').forEach(function(el) {
      var key = el.getAttribute('data-i18n-placeholder');
      if (dict[key] !== undefined) el.setAttribute('placeholder', dict[key]);
    });
    var titleEl = document.querySelector('title[data-i18n-title]');
    if (titleEl) {
      var tKey = titleEl.getAttribute('data-i18n-title');
      if (dict[tKey] !== undefined) titleEl.textContent = dict[tKey];
    }
    document.documentElement.lang = lang;
    var btn = document.getElementById('langToggle');
    if (btn) btn.textContent = lang === 'tr' ? 'EN' : 'TR';
    window.dispatchEvent(new CustomEvent('da-lang-changed', { detail: { lang: lang, dict: dict } }));
  }

  /* Public: switch to a specific language */
  window.daSetLang = function(lang) {
    localStorage.setItem('da-lang', lang);
    loadLocale(lang)
      .then(function(dict) { applyTranslations(dict, lang); })
      .catch(function(err) { console.warn('[i18n] ' + err.message); });
  };

  /* Public: toggle between TR and EN */
  window.daToggleLang = function() {
    var current = localStorage.getItem('da-lang') || 'tr';
    window.daSetLang(current === 'tr' ? 'en' : 'tr');
  };

  /* Public: synchronous lookup helper (returns key if not yet loaded) */
  window.daT = function(key) {
    var lang = localStorage.getItem('da-lang') || 'tr';
    return (_cache[lang] && _cache[lang][key]) || key;
  };

  /* Initialise once DOM is ready */
  function init() {
    var saved = localStorage.getItem('da-lang') || 'tr';
    /* Pre-fetch both locales in the background for instant switching */
    Promise.all([loadLocale('tr'), loadLocale('en')]).catch(function() {});
    /* Set button label immediately to avoid flicker */
    var btn = document.getElementById('langToggle');
    if (btn) btn.textContent = saved === 'tr' ? 'EN' : 'TR';
    /* Only swap page text if language is EN (TR is the default) */
    if (saved === 'en') {
      loadLocale('en')
        .then(function(dict) { applyTranslations(dict, 'en'); })
        .catch(function(err) { console.warn('[i18n] ' + err.message); });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
