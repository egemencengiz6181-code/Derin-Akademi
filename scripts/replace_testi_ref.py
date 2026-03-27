#!/usr/bin/env python3
# Replace testimonials section in referanslar.html with real LinkedIn testimonials

LI_SVG = ('<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="white">'
          '<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 '
          '2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 '
          '5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 '
          '13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 '
          '24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>')

AVATAR = '<div class="tsc-avatar">' + LI_SVG + '</div>'


def card(text, name, role):
    return (
        '        <div class="tsc">'
        '<div class="tsc-stars">\u2605\u2605\u2605\u2605\u2605</div>'
        f'<p class="tsc-text">{text}</p>'
        '<div class="tsc-author">'
        + AVATAR +
        f'<div><div class="tsc-name">{name}</div>'
        f'<div class="tsc-role">{role}</div></div>'
        '</div></div>'
    )


tamay = card(
    "Verimli birliktelik i\u00e7in te\u015fekk\u00fcrler Derin Akademi &amp; Hakan Selahi \U0001f64f "
    "D\u00fc\u015f\u00fcnd\u00fcr\u00fcc\u00fc bir yaz\u0131, tebrikler \U0001f44f\U0001f3fb",
    "A. Fatih Tamay",
    "Y\u00f6netim Kurulu \u00dcyesi"
)

nilay = card(
    "Hakan Bey, kolayl\u0131klar dilerim. Sizinle \u00e7al\u0131\u015fan "
    "\u0130K uzmanlar\u0131 \u00e7ok \u015fansl\u0131, sizden \u00f6\u011frenecek \u00e7ok \u015fey var.",
    "Nilay A.",
    "\u0130nsan Kaynaklar\u0131 Y\u00f6netimi"
)

burak = card(
    "Hakan Beyler ile Bayer Cropscience stratejik partneri olarak iki farkl\u0131 projede "
    "\u00e7al\u0131\u015fma imkan\u0131m\u0131z oldu. Alan\u0131nda uzmanl\u0131\u011f\u0131 ve "
    "\u00e7\u00f6z\u00fcm odakl\u0131 yakla\u015f\u0131m\u0131yla her zaman fark yaratt\u0131. "
    "Dan\u0131\u015fmanl\u0131k s\u00fcrecinde sundu\u011fu de\u011ferli bak\u0131\u015f a\u00e7\u0131lar\u0131 "
    "ger\u00e7ekten ilham verici idi. Ba\u015far\u0131lar\u0131n\u0131n devam\u0131n\u0131 dilerim.",
    "Burak Esentepe",
    "Ziraat M\u00fchendisi"
)

neslihan = card(
    "Kesinlikle kat\u0131l\u0131yorum. Hakan Bey \u00e7ok iyi bir \u00f6\u011freticidir.",
    "Neslihan \u00dcrer Turan",
    "BMI \u0130stanbul Sales &amp; Business"
)

onur = card(
    "Harika bir program! Kriz zamanlar\u0131nda g\u00fc\u00e7l\u00fc kalmak i\u00e7in stratejik "
    "\u0130nsan Kaynaklar\u0131 yakla\u015f\u0131m\u0131n\u0131n \u00f6nemini vurgulayan bu e\u011fitimin "
    "ve Derin Akademi'nin di\u011fer programlar\u0131n\u0131n, Hakan Bey'in uzmanl\u0131\u011f\u0131 ile "
    "i\u015f d\u00fcnyas\u0131 \u00e7al\u0131\u015fanlar\u0131n\u0131 ve organizasyonlar\u0131 "
    "geli\u015ftirdi\u011fini bizzat deneyimledim. De\u011fi\u015fen ekonomik ko\u015fullara adaptasyon "
    "ve do\u011fru yetenekleri konumland\u0131rma konusundaki s\u00fcre\u00e7leri \u00e7ok \u00f6nemseyen "
    "bir lider olarak, kat\u0131l\u0131mc\u0131lar i\u00e7in bu tarz programlar\u0131n \u00e7ok faydal\u0131 "
    "olaca\u011f\u0131na inan\u0131yorum. Hakan Selahi sizi tebrik ederim \U0001f44f\U0001f3fb",
    "Onur \u00c7amili",
    "Bayer Crop Science East Mediterranean"
)

NEW_SECTION = """\
<!-- \u2550\u2550 TESTIMONIALS \u2550\u2550 -->
<section class="testi-scroll-section">
  <div class="container">
    <div class="section-head">
      <div class="section-tag reveal" data-i18n="ref.testi.tag">Ba\u015far\u0131 Hikayeleri</div>
      <h2 class="section-title reveal reveal-d1" data-i18n="ref.testi.title">Onlar De\u011fi\u015ftirdi, S\u0131ra Sende</h2>
      <p class="section-desc reveal reveal-d2" data-i18n="ref.testi.desc">Ger\u00e7ek hikayeler, ger\u00e7ek d\u00f6n\u00fc\u015f\u00fcmler. 40\'tan fazla kurumdan y\u00fczlerce profesyonelin deneyimi.</p>
    </div>
  </div>
  <div class="testi-cols-outer">
    <div class="testi-cols-wrap">

      <!-- S\u00fctun 1 -->
      <div class="testi-scroll-col col-1">
TAMAY
NILAY
        <!-- Duplicate for seamless loop -->
TAMAY
NILAY
      </div>

      <!-- S\u00fctun 2 -->
      <div class="testi-scroll-col col-2">
BURAK
NESLIHAN
        <!-- Duplicate -->
BURAK
NESLIHAN
      </div>

      <!-- S\u00fctun 3 -->
      <div class="testi-scroll-col col-3">
ONUR
        <!-- Duplicate -->
ONUR
      </div>

    </div>
  </div>
</section>
"""

NEW_SECTION = (NEW_SECTION
    .replace('TAMAY', tamay)
    .replace('NILAY', nilay)
    .replace('BURAK', burak)
    .replace('NESLIHAN', neslihan)
    .replace('ONUR', onur)
)

# Also update the CSS in the <style> block at top to use LinkedIn blue avatar
CSS_OLD = """.tsc-avatar{width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Montserrat',sans-serif;font-size:15px;font-weight:800;flex-shrink:0;}
    .tsc-av-a{background:linear-gradient(135deg,#0d9488,#0e7490);color:#fff;}
    .tsc-av-b{background:linear-gradient(135deg,#7c3aed,#a21caf);color:#fff;}
    .tsc-av-c{background:linear-gradient(135deg,#b45309,#d97706);color:#fff;}
    .tsc-av-d{background:linear-gradient(135deg,#0369a1,#0284c7);color:#fff;}
    .tsc-av-e{background:linear-gradient(135deg,#be123c,#e11d48);color:#fff;}
    .tsc-av-f{background:linear-gradient(135deg,#15803d,#16a34a);color:#fff;}"""
CSS_NEW = "    .tsc-avatar{width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;background:#0077B5;}"

content = open('referanslar.html', encoding='utf-8').read()
lines = content.split('\n')

start_idx = None
end_idx = None
for i, l in enumerate(lines):
    if '\u2550\u2550 TESTIMONIALS \u2550\u2550' in l and start_idx is None:
        start_idx = i
    if '\u2550\u2550 FOOTER \u2550\u2550' in l and start_idx is not None and end_idx is None:
        end_idx = i
        break

if start_idx is None or end_idx is None:
    print(f'ERROR: could not find boundaries. start={start_idx} end={end_idx}')
    exit(1)

print(f'Replacing lines {start_idx+1} to {end_idx} (keeping FOOTER onward)')
new_lines = lines[:start_idx] + NEW_SECTION.split('\n') + lines[end_idx:]
result = '\n'.join(new_lines)

# Update avatar CSS
import re
result = re.sub(
    r'\.tsc-avatar\{[^}]+\}(\s*\.tsc-av-[a-f]\{[^}]+\}\s*)+',
    '    .tsc-avatar{width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;background:#0077B5;}\n',
    result
)

open('referanslar.html', 'w', encoding='utf-8').write(result)
print('Done!')
