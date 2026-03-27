#!/usr/bin/env python3
"""
Add data-i18n attributes to the 6 consulting detail pages.
Each page needs:
- cs-step-title / cs-step-desc (5 steps each)
- cs-val-title / cs-val-desc (4 values each)
- cs-quote-text
- cs-cta-title (already has span, will use data-i18n-html)
- cs-cta-desc
- cs-cta-actions buttons
"""
import re, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAGES = {
    "gelecege-hazir-kadro": "kadro",
    "gelisimi-olc": "olc",
    "iceriden-guclen": "guclen",
    "stratejiyi-gundelik-hayata": "strateji",
    "ucret-stratejisi": "ucret",
    "yetenek-yonetimi": "yetenek",
}

def add_i18n_to_class(html, cls, key, use_html=False):
    """Add data-i18n to the first div/p with the given class that doesn't already have it."""
    attr = 'data-i18n-html' if use_html else 'data-i18n'
    # Match opening tag with this class, skip if already has data-i18n
    pattern = rf'(<(?:div|p)\s[^>]*class="[^"]*\b{re.escape(cls)}\b[^"]*"[^>]*)(?<!data-i18n[^>]*)(>)'
    def replacer(m):
        tag = m.group(1)
        if 'data-i18n' in tag:
            return m.group(0)
        return f'{tag} {attr}="{key}"{m.group(2)}'
    return re.sub(pattern, replacer, html, count=1)

def process_page(page_file, prefix, html):
    """Process a consulting detail page, adding all data-i18n attributes."""
    lines = html.split('\n')
    result = []
    
    step_num = 0
    val_num = 0
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # cs-step-title
        if '<div class="cs-step-title">' in line and 'data-i18n' not in line:
            step_num += 1
            line = line.replace('<div class="cs-step-title">', f'<div class="cs-step-title" data-i18n="{prefix}.step{step_num}.title">')
        # cs-step-desc
        elif '<div class="cs-step-desc">' in line and 'data-i18n' not in line:
            line = line.replace('<div class="cs-step-desc">', f'<div class="cs-step-desc" data-i18n="{prefix}.step{step_num}.desc">')
        # cs-val-title
        elif '<div class="cs-val-title">' in line and 'data-i18n' not in line:
            val_num += 1
            line = line.replace('<div class="cs-val-title">', f'<div class="cs-val-title" data-i18n="{prefix}.val{val_num}.title">')
        # cs-val-desc
        elif '<div class="cs-val-desc">' in line and 'data-i18n' not in line:
            line = line.replace('<div class="cs-val-desc">', f'<div class="cs-val-desc" data-i18n="{prefix}.val{val_num}.desc">')
        # cs-quote-text
        elif '<div class="cs-quote-text">' in line and 'data-i18n' not in line:
            line = line.replace('<div class="cs-quote-text">', f'<div class="cs-quote-text" data-i18n="{prefix}.quote">')
        # cs-cta-title (has inner span, use data-i18n-html with aileden shared key)
        elif '<div class="cs-cta-title">' in line and 'data-i18n' not in line:
            line = line.replace('<div class="cs-cta-title">', '<div class="cs-cta-title" data-i18n-html="danis.aileden.cta.title2">')
        # cs-cta-desc
        elif '<p class="cs-cta-desc">' in line and 'data-i18n' not in line:
            line = line.replace('<p class="cs-cta-desc">', '<p class="cs-cta-desc" data-i18n="danis.aileden.cta.desc2">')
        
        result.append(line)
        i += 1
    
    # Now handle the cs-cta-actions buttons (they come after cs-cta-actions div)
    # Look for the buttons inside cs-cta-actions
    output = '\n'.join(result)
    
    # Fix CTA action buttons if they don't have data-i18n
    # Pattern: btn-primary inside cs-cta-actions
    output = re.sub(
        r'(<div class="cs-cta-actions">[\s\S]*?)'
        r'(<button onclick="openTeklifModal\(\)" class="btn btn-primary btn-lg")(?![^>]*data-i18n)',
        r'\1\2 data-i18n="shared.btn.bilgial"',
        output, count=1
    )
    output = re.sub(
        r'(<div class="cs-cta-actions">[\s\S]*?)'
        r'(<a href="https://wa\.me/[^"]*" target="_blank" class="btn btn-ghost btn-lg")(?![^>]*data-i18n)',
        r'\1\2 data-i18n="shared.btn.whatsapp2"',
        output, count=1
    )
    
    return output

for page_slug, prefix in PAGES.items():
    path = os.path.join(BASE, 'danismanliklar', f'{page_slug}.html')
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    original = html
    html = process_page(path, f'danis.{prefix}', html)
    
    if html != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'✅ Updated: {page_slug}.html')
    else:
        print(f'⚠️  No changes: {page_slug}.html')

print('\nDone!')
