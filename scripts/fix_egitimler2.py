#!/usr/bin/env python3
"""
Fix remaining hardcoded Turkish text in all 10 egitimler pages:
1. CTA title TR values → add <span class="gradient-text"> HTML
2. CTA title EN values → add <span class="gradient-text"> HTML
3. Breadcrumb last span → add data-i18n per page
4. Footer newsletter <p> → add data-i18n="shared.footer.bulten.desc"
5. Modal h2 → add data-i18n-html="shared.modal.title.html"
6. Modal desc <p> → add data-i18n="shared.modal.desc"
"""
import json, os, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Page config: file → (prefix, breadcrumb_tr, breadcrumb_en)
PAGES = [
    ("yeni-nesil-liderlik.html",    "liderlik",  "Yeni Nesil Liderlik",           "New Generation Leadership"),
    ("haddini-bildirme.html",       "haddini",   "Etkin Geri Bildirim",            "Effective Feedback"),
    ("kapsayan-kazanir.html",       "kapsayan",  "Kapsayıcı Liderlik",             "Inclusive Leadership"),
    ("mulakat-becerileri.html",     "mulakat",   "Mülakat Becerileri 5.0",         "Interview Skills 5.0"),
    ("performans-360.html",         "perf360",   "Performans 360",                 "Performance 360"),
    ("stratejik-ik-yonetimi.html",  "stratejik", "Stratejik İK Yönetimi",          "Strategic HR Management"),
    ("ucretin-otesi.html",          "ucret",     "Ücretin Ötesi",                  "Beyond Pay"),
    ("veriye-donusen-insan.html",   "veri",      "Veri Odaklı İK Yönetimi",        "Data-Driven HR Management"),
    ("yapay-zeka-ikda.html",        "yz",        "Yapay Zekâ İK'da",               "AI in HR"),
    ("aidiyet-tasarimi.html",       "aidiyet",   "Aidiyet Tasarımı",               "Belonging Design"),
]

# EN gradient-text "suffix" for each cta.title (what goes inside the span)
CTA_EN_MAIN = {
    "liderlik":  "Let's Tailor the New Generation Leadership Training",
    "haddini":   "Let's Tailor the Effective Feedback Training",
    "kapsayan":  "Let's Tailor the Inclusive Leadership Training",
    "mulakat":   "Let's Tailor the Interview Skills 5.0 Training",
    "perf360":   "Let's Tailor the Performance 360 Training",
    "stratejik": "Let's Tailor the Strategic HR Management Training",
    "ucret":     "Let's Tailor the Strategic Compensation & Reward Management Training",
    "veri":      "Let's Tailor the Data-Driven HR Management Training",
    "yz":        "Let's Tailor the AI in HR Training",
    "aidiyet":   "Let's Tailor the Employee Experience & Belonging Design Training",
}

CTA_TR_MAIN = {
    "liderlik":  "Yeni Nesil Liderlik Eğitimini",
    "haddini":   "Etkin Geri Bildirim Eğitimini",
    "kapsayan":  "Kapsayıcı Liderlik Eğitimini",
    "mulakat":   "Mülakat Becerileri 5.0 Eğitimini",
    "perf360":   "Performans 360 Eğitimini",
    "stratejik": "Stratejik İK Yönetimi Eğitimini",
    "ucret":     "Stratejik Ücret ve Ödül Yönetimi Eğitimini",
    "veri":      "Veri Odaklı İK Yönetimi Eğitimini",
    "yz":        "Yapay Zekâ İK'da Eğitimini",
    "aidiyet":   "Çalışan Deneyimi ve Aidiyet Tasarımı Eğitimini",
}
GRADIENT_SUFFIX_TR = '<span class="gradient-text">Kurumunuza Uyarlayalım</span>'
GRADIENT_SUFFIX_EN = '<span class="gradient-text">to Your Institution</span>'


def main():
    tr_path = os.path.join(BASE, 'locales', 'tr.json')
    en_path = os.path.join(BASE, 'locales', 'en.json')

    with open(tr_path, encoding='utf-8') as f: tr_json = json.load(f)
    with open(en_path, encoding='utf-8') as f: en_json = json.load(f)

    # ── 1. Update cta.title JSON values to include gradient-text span ────────
    for _, prefix, breadcrumb_tr, breadcrumb_en in PAGES:
        key = f"egitim.{prefix}.cta.title"
        tr_json[key] = f'{CTA_TR_MAIN[prefix]} {GRADIENT_SUFFIX_TR}'
        en_json[key] = f'{CTA_EN_MAIN[prefix]} {GRADIENT_SUFFIX_EN}'

    # ── 2. Add breadcrumb keys ────────────────────────────────────────────────
    for _, prefix, breadcrumb_tr, breadcrumb_en in PAGES:
        key = f"egitim.{prefix}.breadcrumb"
        tr_json[key] = breadcrumb_tr
        en_json[key] = breadcrumb_en

    # ── 3. Add modal title HTML key ───────────────────────────────────────────
    tr_json["shared.modal.title.html"] = 'Hemen <span class="gradient-text">Teklif Alın</span>'
    en_json["shared.modal.title.html"] = 'Get a <span class="gradient-text">Quote Now</span>'

    with open(tr_path, 'w', encoding='utf-8') as f:
        json.dump(tr_json, f, ensure_ascii=False, indent=2)
    with open(en_path, 'w', encoding='utf-8') as f:
        json.dump(en_json, f, ensure_ascii=False, indent=2)
    print("✅ JSON updated (cta.title HTML spans, breadcrumbs, modal title)")

    # ── 4. Update HTML in all 10 training pages ───────────────────────────────
    for filename, prefix, breadcrumb_tr, _ in PAGES:
        path = os.path.join(BASE, 'egitimler', filename)
        with open(path, encoding='utf-8') as f:
            html = f.read()
        original = html

        # 4a. Breadcrumb last span
        html = html.replace(
            f'<span>{breadcrumb_tr}</span>\n</nav>',
            f'<span data-i18n="egitim.{prefix}.breadcrumb">{breadcrumb_tr}</span>\n</nav>',
            1
        )

        # 4b. Footer newsletter <p>
        html = html.replace(
            '<p>İK gündemindeki gelişmelerden ve eğitimlerimizden haberdar ol.</p>',
            '<p data-i18n="shared.footer.bulten.desc">İK gündemindeki gelişmelerden ve eğitimlerimizden haberdar ol.</p>',
            1
        )

        # 4c. Modal h2 with span
        html = html.replace(
            '<h2 style="font-family:\'Montserrat\',sans-serif;font-size:24px;font-weight:900;line-height:1.2;margin-bottom:8px;">Hemen <span class="gradient-text">Teklif Alın</span></h2>',
            '<h2 data-i18n-html="shared.modal.title.html" style="font-family:\'Montserrat\',sans-serif;font-size:24px;font-weight:900;line-height:1.2;margin-bottom:8px;">Hemen <span class="gradient-text">Teklif Alın</span></h2>',
            1
        )

        # 4d. Modal desc <p>
        html = html.replace(
            '<p style="color:var(--silver);font-size:13px;line-height:1.75;margin-bottom:28px;">İhtiyaçlarınızı paylaşın, size özel program ve teklif oluşturalım.</p>',
            '<p data-i18n="shared.modal.desc" style="color:var(--silver);font-size:13px;line-height:1.75;margin-bottom:28px;">İhtiyaçlarınızı paylaşın, size özel program ve teklif oluşturalım.</p>',
            1
        )

        if html != original:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"✅ Updated: {filename}")
        else:
            print(f"⚠️  No changes: {filename}")

    # ── 5. Also fix the modal desc TR JSON value to match page text ──────────
    with open(tr_path, encoding='utf-8') as f: tr_json = json.load(f)
    with open(en_path, encoding='utf-8') as f: en_json = json.load(f)
    # Update shared.modal.desc to match simpler text (without "Eğitim" prefix)
    tr_json["shared.modal.desc"] = "İhtiyaçlarınızı paylaşın, size özel program ve teklif oluşturalım."
    en_json["shared.modal.desc"] = "Share your needs and we'll create a customized program and quote for you."
    with open(tr_path, 'w', encoding='utf-8') as f:
        json.dump(tr_json, f, ensure_ascii=False, indent=2)
    with open(en_path, 'w', encoding='utf-8') as f:
        json.dump(en_json, f, ensure_ascii=False, indent=2)
    print("✅ shared.modal.desc JSON value updated")


if __name__ == '__main__':
    main()
