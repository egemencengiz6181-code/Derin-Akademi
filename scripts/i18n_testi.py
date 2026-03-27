#!/usr/bin/env python3
"""Add data-i18n attributes to testimonial cards in index.html and referanslar.html,
and add translation keys to locales/tr.json and locales/en.json."""
import json, re

# ─── Translation data ──────────────────────────────────────────────────────────
CARDS = {
    "tamay": {
        "text_tr": "Verimli birliktelik i\u00e7in te\u015fekk\u00fcrler Derin Akademi &amp; Hakan Selahi \U0001f64f D\u00fc\u015f\u00fcnd\u00fcr\u00fcc\u00fc bir yaz\u0131, tebrikler \U0001f44f\U0001f3fb",
        "text_en": "Thank you for the fruitful collaboration, Derin Akademi &amp; Hakan Selahi \U0001f64f A thought-provoking piece, congratulations \U0001f44f\U0001f3fb",
        "role_tr": "Y\u00f6netim Kurulu \u00dcyesi",
        "role_en": "Board Member",
    },
    "nilay": {
        "text_tr": "Hakan Bey, kolayl\u0131klar dilerim. Sizinle \u00e7al\u0131\u015fan \u0130K uzmanlar\u0131 \u00e7ok \u015fansl\u0131, sizden \u00f6\u011frenecek \u00e7ok \u015fey var.",
        "text_en": "Hakan Bey, best of luck. The HR professionals who work with you are very fortunate \u2014 there is so much to learn from you.",
        "role_tr": "\u0130nsan Kaynaklar\u0131 Y\u00f6netimi",
        "role_en": "Human Resources Management",
    },
    "burak": {
        "text_tr": "Hakan Beyler ile Bayer Cropscience stratejik partneri olarak iki farkl\u0131 projede \u00e7al\u0131\u015fma imkan\u0131m\u0131z oldu. Alan\u0131nda uzmanl\u0131\u011f\u0131 ve \u00e7\u00f6z\u00fcm odakl\u0131 yakla\u015f\u0131m\u0131yla her zaman fark yaratt\u0131. Dan\u0131\u015fmanl\u0131k s\u00fcrecinde sundu\u011fu de\u011ferli bak\u0131\u015f a\u00e7\u0131lar\u0131 ger\u00e7ekten ilham verici idi. Ba\u015far\u0131lar\u0131n\u0131n devam\u0131n\u0131 dilerim.",
        "text_en": "We had the opportunity to work with Hakan and team as a strategic partner of Bayer Cropscience on two different projects. With their expertise and solution-oriented approach, they always made a difference. The valuable perspectives shared during the consulting process were truly inspiring. Wishing them continued success.",
        "role_tr": "Ziraat M\u00fchendisi",
        "role_en": "Agricultural Engineer",
    },
    "neslihan": {
        "text_tr": "Kesinlikle kat\u0131l\u0131yorum. Hakan Bey \u00e7ok iyi bir \u00f6\u011freticidir.",
        "text_en": "I absolutely agree. Hakan Bey is an excellent instructor.",
        "role_tr": "BMI \u0130stanbul Sales &amp; Business",
        "role_en": "BMI \u0130stanbul Sales &amp; Business",
    },
    "onur": {
        "text_tr": "Harika bir program! Kriz zamanlar\u0131nda g\u00fc\u00e7l\u00fc kalmak i\u00e7in stratejik \u0130nsan Kaynaklar\u0131 yakla\u015f\u0131m\u0131n\u0131n \u00f6nemini vurgulayan bu e\u011fitimin ve Derin Akademi\u2019nin di\u011fer programlar\u0131n\u0131n, Hakan Bey\u2019in uzmanl\u0131\u011f\u0131 ile i\u015f d\u00fcnyas\u0131 \u00e7al\u0131\u015fanlar\u0131n\u0131 ve organizasyonlar\u0131 geli\u015ftirdi\u011fini bizzat deneyimledim. De\u011fi\u015fen ekonomik ko\u015fullara adaptasyon ve do\u011fru yetenekleri konumland\u0131rma konusundaki s\u00fcre\u00e7leri \u00e7ok \u00f6nemseyen bir lider olarak, kat\u0131l\u0131mc\u0131lar i\u00e7in bu tarz programlar\u0131n \u00e7ok faydal\u0131 olaca\u011f\u0131na inan\u0131yorum. Hakan Selahi sizi tebrik ederim \U0001f44f\U0001f3fb",
        "text_en": "What a great program! I have personally experienced how this training \u2014 which emphasizes the importance of a strategic HR approach in staying strong during difficult times \u2014 and Derin Akademi\u2019s other programs develop business professionals and organizations through Hakan Bey\u2019s expertise. As a leader who greatly values adapting to changing economic conditions and positioning the right talent, I believe programs like this are extremely beneficial for participants. Congratulations, Hakan Selahi \U0001f44f\U0001f3fb",
        "role_tr": "Bayer Crop Science East Mediterranean",
        "role_en": "Bayer Crop Science East Mediterranean",
    },
}

# ─── Update JSON files ─────────────────────────────────────────────────────────
for lang in ("tr", "en"):
    path = f"locales/{lang}.json"
    data = json.loads(open(path, encoding="utf-8").read())
    for key, vals in CARDS.items():
        data[f"tsc.{key}.text"] = vals[f"text_{lang}"]
        data[f"tsc.{key}.role"] = vals[f"role_{lang}"]
    open(path, "w", encoding="utf-8").write(
        json.dumps(data, ensure_ascii=False, indent=2)
    )
    print(f"Updated {path}")

# ─── Patch HTML files ──────────────────────────────────────────────────────────
def patch_html(filepath):
    content = open(filepath, encoding="utf-8").read()

    for key, vals in CARDS.items():
        tr_text = vals["text_tr"]
        tr_role = vals["role_tr"]

        # Add data-i18n to <p class="tsc-text">
        old_p = f'<p class="tsc-text">{tr_text}</p>'
        new_p = f'<p class="tsc-text" data-i18n="tsc.{key}.text">{tr_text}</p>'
        count_p = content.count(old_p)

        # Add data-i18n to <div class="tsc-role">
        old_r = f'<div class="tsc-role">{tr_role}</div>'
        new_r = f'<div class="tsc-role" data-i18n="tsc.{key}.role">{tr_role}</div>'
        count_r = content.count(old_r)

        if count_p == 0 and content.count(new_p) > 0:
            print(f"  {key} text: already has data-i18n")
        elif count_p == 0:
            print(f"  WARNING: {key} text not found in {filepath}")
        else:
            content = content.replace(old_p, new_p)
            print(f"  {key} text: patched {count_p} occurrence(s)")

        if count_r == 0 and content.count(new_r) > 0:
            print(f"  {key} role: already has data-i18n")
        elif count_r == 0:
            print(f"  WARNING: {key} role not found in {filepath}")
        else:
            content = content.replace(old_r, new_r)
            print(f"  {key} role: patched {count_r} occurrence(s)")

    open(filepath, "w", encoding="utf-8").write(content)
    print(f"Saved {filepath}\n")

print("\nPatching index.html...")
patch_html("index.html")
print("Patching referanslar.html...")
patch_html("referanslar.html")
print("All done!")
