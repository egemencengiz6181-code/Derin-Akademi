#!/usr/bin/env python3
"""Find remaining hardcoded Turkish text in egitimler pages (not covered by data-i18n)."""
import re, glob

for fn in sorted(glob.glob('egitimler/*.html')):
    content = open(fn).read()
    results = []

    # <p> without data-i18n
    for m in re.finditer(r'<p(?![^>]*data-i18n)[^>]*>([^<]{20,})', content):
        t = m.group(1).strip()
        if any(c in t for c in 'çğışöüÇĞİŞÖÜ') or 'Egitim' in t:
            results.append(('p', t[:100]))

    # <h3> without data-i18n
    for m in re.finditer(r'<h3(?![^>]*data-i18n)[^>]*>([^<]{5,})</h3>', content):
        t = m.group(1).strip()
        if any(c in t for c in 'çğışöüÇĞİŞÖÜ') or len(t) > 5:
            results.append(('h3', t[:100]))

    # <span> without data-i18n (non-checkmark)
    for m in re.finditer(r'<span(?![^>]*data-i18n)(?![^>]*outcome-check)[^>]*>([^<]{10,})</span>', content):
        t = m.group(1).strip()
        if any(c in t for c in 'çğışöüÇĞİŞÖÜ'):
            results.append(('span', t[:100]))

    # <li> items in ul lists
    for m in re.finditer(r'<li[^>]*>([^<]{5,})</li>', content):
        t = m.group(1).strip()
        if any(c in t for c in 'çğışöüÇĞİŞÖÜ'):
            results.append(('li', t[:100]))

    if results:
        print(f'\n=== {fn} ===')
        for kind, text in results:
            print(f'  [{kind}] {text}')

print('\nDone.')
