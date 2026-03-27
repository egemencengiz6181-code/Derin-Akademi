#!/usr/bin/env python3
"""
Add data-i18n attributes to all 10 egitimler (training) pages.
Also adds English translations to both tr.json and en.json.
"""
import json, os, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ─── TRANSLATIONS ──────────────────────────────────────────────────────────────
# (TR, EN) tuples

SHARED = {
    "shared.egitim.h3.icerik":   ("Eğitim İçeriği",   "Training Content"),
    "shared.egitim.h3.icerik2":  ("Eğitimin İçeriği", "Training Content"),
    "shared.egitim.h3.problems": (
        "Kurumlar Bu Eğitimle Hangi Sorunları Çözüyor?",
        "What Problems Does This Training Solve for Organizations?",
    ),
    "shared.egitim.h3.gains": (
        "Kurumlar Bu Eğitim Sonrasında Ne Kazanıyor?",
        "What Do Organizations Gain After This Training?",
    ),
    "shared.egitim.cta.tag": ("Kurumunuza Özel", "Tailored for Your Organization"),
}

# Per-page key data. Format:  key_suffix -> (TR, EN)
# HTML replacements are derived from these.
PAGES = [
    # ── 1. YENİ NESİL LİDERLİK ──────────────────────────────────────────────
    {
        "file": "yeni-nesil-liderlik.html",
        "p": "liderlik",
        "desc1": (
            "Günümüz organizasyonlarında liderlerden yalnızca operasyonları yönetmeleri değil, ekiplerini motive eden, gelişimlerini destekleyen ve organizasyon kültürünü güçlendiren bir liderlik yaklaşımı beklenmektedir. Bu eğitim, yöneticilerin klasik yönetim anlayışından çıkarak güven, gelişim ve performans odaklı bir liderlik yaklaşımı geliştirmelerini amaçlar.",
            "Today's organizations expect leaders not only to manage operations, but to motivate their teams, support development, and strengthen organizational culture. This training helps managers move beyond traditional management thinking and develop a trust-, growth-, and performance-focused leadership approach.",
        ),
        "h3_content": "shared.egitim.h3.icerik",
        "content1": (
            "Günümüz organizasyonlarında liderliğin değişen rolü, güven ve psikolojik güven ortamı oluşturmak, koçvari liderlik yaklaşımı, yetkilendirme ve sorumluluk devri, liderin kurum kültürü ve performans üzerindeki etkisi.",
            "The evolving role of leadership in today's organizations, building trust and psychological safety, coaching-style leadership, empowerment and delegation, the leader's impact on organizational culture and performance.",
        ),
        "h3_problems": "shared.egitim.h3.problems",
        "problems1": (
            "Yöneticilerin ekip motivasyonunu artırmakta zorlanması, çalışan bağlılığının düşük olması, yönetim tarzının fazla kontrol ve talimat odaklı olması, ekip içinde güven ortamının zayıf olması, yöneticilerin ekip gelişimini desteklemekte zorlanması.",
            "Managers struggling to boost team motivation, low employee engagement, overly control-and-instruction-oriented management, weak trust environments within teams, managers struggling to support team development.",
        ),
        "h3_gains": "shared.egitim.h3.gains",
        "gains1": (
            "Güven temelli ekip kültürü, daha yüksek çalışan bağlılığı, yetkilendirme ve sorumluluk devri, gelişim odaklı liderlik yaklaşımı.",
            "A trust-based team culture, higher employee engagement, empowerment and delegation, a development-focused leadership approach.",
        ),
        "outcomes": [
            ("Ekip performansını artıran liderlik davranışları", "Leadership behaviors that improve team performance"),
            ("Güven temelli ekip kültürü oluşturma", "Building a trust-based team culture"),
            ("Çalışan bağlılığını destekleyen liderlik yaklaşımı", "A leadership approach that supports employee engagement"),
            ("Yetkilendirme ve sorumluluk devri", "Empowerment and delegation"),
            ("Gelişim odaklı liderlik anlayışı", "A development-focused leadership mindset"),
            ("Koçvari liderlik yaklaşımı", "Coaching-style leadership approach"),
        ],
        "targets": [
            ("Orta ve Üst Düzey Yöneticiler", "Middle and Senior Managers"),
            ("Takım Liderleri", "Team Leaders"),
            ("Yönetici Adayları", "Future Leaders"),
        ],
    },
    # ── 2. ETKİN GERİ BİLDİRİM (HADDİNİ BİLDİRME) ──────────────────────────
    {
        "file": "haddini-bildirme.html",
        "p": "haddini",
        "desc1": (
            "Birçok organizasyonda performans sorunları zamanında ele alınmadığı için büyür ve ekip içinde iletişim sorunları ortaya çıkar. Bu eğitim, yöneticilerin açık ve yapıcı geri bildirim verme becerilerini geliştirmeyi ve zor konuşmaları sağlıklı şekilde yönetmelerini amaçlar.",
            "In many organizations, performance issues grow because they are not addressed in time, creating communication problems within teams. This training helps managers develop the skills to deliver open and constructive feedback and handle difficult conversations effectively.",
        ),
        "h3_content": "shared.egitim.h3.icerik",
        "content1": (
            "Geri bildirim kültürünün önemi, yapıcı geri bildirim teknikleri, zor konuşmaların yönetimi, performans görüşmeleri, davranış odaklı iletişim yaklaşımı.",
            "The importance of a feedback culture, constructive feedback techniques, managing difficult conversations, performance interviews, behavior-based communication.",
        ),
        "h3_problems": "shared.egitim.h3.problems",
        "problems1": (
            "Performans sorunlarının zamanında konuşulmaması, yöneticilerin geri bildirim vermekten kaçınması, zor konuşmaların ertelenmesi, ekip içinde iletişim sorunlarının büyümesi.",
            "Performance issues not being addressed in time, managers avoiding feedback, difficult conversations being postponed, communication problems within teams growing.",
        ),
        "h3_gains": "shared.egitim.h3.gains",
        "gains1": (
            "Açık ve güvene dayalı iletişim ortamı, yapıcı geri bildirim kültürü, performans sorunlarını erken yönetebilme, daha güçlü yönetici–çalışan ilişkileri.",
            "An open and trust-based communication environment, a constructive feedback culture, the ability to manage performance issues early, stronger manager–employee relationships.",
        ),
        "outcomes": [
            ("Açık ve güvene dayalı iletişim ortamı", "An open and trust-based communication environment"),
            ("Yapıcı geri bildirim kültürü", "A constructive feedback culture"),
            ("Performans sorunlarını erken yönetebilme", "The ability to manage performance issues early"),
            ("Daha güçlü yönetici–çalışan ilişkileri", "Stronger manager–employee relationships"),
            ("Davranış odaklı iletişim yaklaşımı", "Behavior-based communication approach"),
            ("Zor konuşmaları yönetme becerisi", "Skills for managing difficult conversations"),
        ],
        "targets": [
            ("Yöneticiler", "Managers"),
            ("Takım Liderleri", "Team Leaders"),
            ("İK Profesyonelleri", "HR Professionals"),
        ],
    },
    # ── 3. KAPSAYICI LİDERLİK ────────────────────────────────────────────────
    {
        "file": "kapsayan-kazanir.html",
        "p": "kapsayan",
        "desc1": (
            "Farklı bakış açılarını ve çeşitliliği etkin şekilde yöneten organizasyonlar daha yüksek inovasyon ve performans elde eder. Bu eğitim, yöneticilerin kapsayıcı liderlik yaklaşımını benimsemelerini ve ekiplerde farklılıkları avantaja dönüştürmelerini destekler.",
            "Organizations that effectively manage diverse perspectives and diversity achieve higher innovation and performance. This training supports managers in adopting an inclusive leadership approach and turning differences within teams into advantages.",
        ),
        "h3_content": "shared.egitim.h3.icerik",
        "content1": (
            "Çeşitlilik ve kapsayıcılık kavramı, bilinçsiz önyargılar, farklı ekipleri yönetmek, dahil edici karar alma süreçleri, kurum kültürü ve kapsayıcı liderlik.",
            "The concept of diversity and inclusion, unconscious biases, managing diverse teams, inclusive decision-making processes, organizational culture and inclusive leadership.",
        ),
        "h3_problems": "shared.egitim.h3.problems",
        "problems1": (
            "Farklı bakış açılarının yeterince değerlendirilmemesi, ekipler arasında iletişim ve iş birliği sorunları, çeşitliliğin organizasyon içinde yeterince değerlendirilememesi, kurum kültüründe kapsayıcılık eksikliği.",
            "Diverse perspectives not being fully valued, communication and collaboration issues between teams, diversity not being fully leveraged within the organization, a lack of inclusivity in organizational culture.",
        ),
        "h3_gains": "shared.egitim.h3.gains",
        "gains1": (
            "Farklı bakış açılarını değerlendiren ekip kültürü, daha güçlü ekip iş birliği, kapsayıcı kurum kültürü, daha yüksek yaratıcılık ve inovasyon ortamı.",
            "A team culture that values diverse perspectives, stronger team collaboration, an inclusive organizational culture, a higher creativity and innovation environment.",
        ),
        "outcomes": [
            ("Ekipler arasında güçlü iş birliği oluşturma", "Building strong collaboration across teams"),
            ("Farklı bakış açılarını kurumsal avantaja dönüştürme", "Turning diverse perspectives into organizational advantages"),
            ("Kapsayıcı kurum kültürü oluşturma", "Building an inclusive organizational culture"),
            ("Daha yüksek yaratıcılık ve inovasyon", "Higher creativity and innovation"),
            ("Bilinçsiz önyargıların farkındalığı", "Awareness of unconscious biases"),
            ("Dahil edici karar alma süreçleri", "Inclusive decision-making processes"),
        ],
        "targets": [
            ("Orta ve Üst Düzey Yöneticiler", "Middle and Senior Managers"),
            ("İnsan Kaynakları Yöneticileri", "HR Managers"),
            ("Organizasyon Gelişimi Ekipleri", "Organizational Development Teams"),
        ],
    },
    # ── 4. MÜLAKAT BECERİLERİ ────────────────────────────────────────────────
    {
        "file": "mulakat-becerileri.html",
        "p": "mulakat",
        "desc1": (
            "Yanlış işe alımlar organizasyonlar için yüksek maliyetler yaratır. Bu eğitim, davranış odaklı mülakat teknikleri ile adayların yetkinliklerini daha doğru değerlendirmeyi ve işe alım süreçlerini sistematik hale getirmeyi amaçlar.",
            "Wrong hiring decisions create high costs for organizations. This training aims to more accurately assess candidate competencies through behavior-based interview techniques and to systematize recruitment processes.",
        ),
        "h3_content": "shared.egitim.h3.icerik",
        "content1": (
            "Yetkinlik bazlı mülakat yaklaşımı, davranışsal soru teknikleri, STAR yöntemi, mülakat hataları ve önyargılar, aday değerlendirme teknikleri konuları ele alınır.",
            "Competency-based interview approach, behavioral questioning techniques, the STAR method, interview errors and biases, and candidate evaluation techniques are covered.",
        ),
        "h3_problems": "shared.egitim.h3.problems",
        "problems_ul_tr": (
            '<li style="margin-bottom:8px;">✗ Yanlış işe alım kararları</li>'
            '<li style="margin-bottom:8px;">✗ Mülakatların kişisel yorumlara dayanması</li>'
            '<li style="margin-bottom:8px;">✗ Aday değerlendirme sürecinde standardizasyon eksikliği</li>'
            '<li style="margin-bottom:8px;">✗ Yetkinliklerin doğru ölçülememesi</li>'
        ),
        "problems_ul_en": (
            '<li style="margin-bottom:8px;">✗ Wrong hiring decisions</li>'
            '<li style="margin-bottom:8px;">✗ Interviews based on personal interpretations</li>'
            '<li style="margin-bottom:8px;">✗ Lack of standardization in the candidate evaluation process</li>'
            '<li style="margin-bottom:8px;">✗ Inability to accurately measure competencies</li>'
        ),
        "h3_gains": "shared.egitim.h3.gains",
        "gains_ul_tr": (
            '<li style="margin-bottom:8px;">✓ Yetkinlik bazlı mülakat yaklaşımı</li>'
            '<li style="margin-bottom:8px;">✓ Daha doğru işe alım kararları</li>'
            '<li style="margin-bottom:8px;">✓ Mülakat süreçlerinde standardizasyon</li>'
            '<li style="margin-bottom:8px;">✓ Aday deneyiminin iyileştirilmesi</li>'
        ),
        "gains_ul_en": (
            '<li style="margin-bottom:8px;">✓ Competency-based interview approach</li>'
            '<li style="margin-bottom:8px;">✓ More accurate hiring decisions</li>'
            '<li style="margin-bottom:8px;">✓ Standardization in interview processes</li>'
            '<li style="margin-bottom:8px;">✓ Improved candidate experience</li>'
        ),
        "outcomes": [
            ("Daha doğru işe alım kararları", "More accurate hiring decisions"),
            ("Mülakat süreçlerinde standardizasyon", "Standardization in interview processes"),
            ("Aday deneyimini geliştirme", "Improving candidate experience"),
        ],
        "targets": [
            ("Yöneticiler", "Managers"),
            ("İK Uzmanları", "HR Specialists"),
            ("İşe Alım Ekipleri", "Recruitment Teams"),
        ],
    },
    # ── 5. PERFORMANS 360 ────────────────────────────────────────────────────
    {
        "file": "performans-360.html",
        "p": "perf360",
        "desc1": (
            "Performans yönetimi yalnızca yıl sonu değerlendirmelerinden ibaret değildir. Bu eğitim, kurumlarda sürdürülebilir ve gelişim odaklı bir performans yönetim sistemi kurulmasını amaçlar.",
            "Performance management is not limited to year-end evaluations. This training aims to establish a sustainable and development-focused performance management system in organizations.",
        ),
        "h3_content": "shared.egitim.h3.icerik",
        "content1": (
            "Performans sistemi tasarımı, hedeflerle yönetim ve OKR yaklaşımı, 360 derece geri bildirim sistemi, performans görüşmeleri ve gelişim planlarının oluşturulması konuları ele alınır.",
            "Performance system design, management by objectives and OKR approach, 360-degree feedback system, performance reviews and the creation of development plans are covered.",
        ),
        "h3_problems": "shared.egitim.h3.problems",
        "problems_ul_tr": (
            '<li style="margin-bottom:8px;">✗ Performans değerlendirmelerinin formaliteye dönüşmesi</li>'
            '<li style="margin-bottom:8px;">✗ Hedeflerin net olmaması</li>'
            '<li style="margin-bottom:8px;">✗ Performans görüşmelerinin yapılmaması veya yüzeysel kalması</li>'
            '<li style="margin-bottom:8px;">✗ Performans sonuçlarının gelişime dönüşmemesi</li>'
        ),
        "problems_ul_en": (
            '<li style="margin-bottom:8px;">✗ Performance reviews becoming a formality</li>'
            '<li style="margin-bottom:8px;">✗ Unclear goals</li>'
            '<li style="margin-bottom:8px;">✗ Performance discussions not happening or remaining superficial</li>'
            '<li style="margin-bottom:8px;">✗ Performance outcomes not translating into development</li>'
        ),
        "h3_gains": "shared.egitim.h3.gains",
        "gains_ul_tr": (
            '<li style="margin-bottom:8px;">✓ Net hedeflerle performans yönetimi</li>'
            '<li style="margin-bottom:8px;">✓ Şeffaf ve adil değerlendirme sistemi</li>'
            '<li style="margin-bottom:8px;">✓ Gelişim odaklı performans görüşmeleri</li>'
            '<li style="margin-bottom:8px;">✓ Kurumsal performans kültürü</li>'
        ),
        "gains_ul_en": (
            '<li style="margin-bottom:8px;">✓ Performance management with clear goals</li>'
            '<li style="margin-bottom:8px;">✓ A transparent and fair evaluation system</li>'
            '<li style="margin-bottom:8px;">✓ Development-focused performance reviews</li>'
            '<li style="margin-bottom:8px;">✓ An organizational performance culture</li>'
        ),
        "outcomes": [
            ("Net hedeflerle performans takibi", "Performance tracking with clear goals"),
            ("Adil ve şeffaf değerlendirme sistemi", "A fair and transparent evaluation system"),
            ("Performans kültürü oluşturma", "Building a performance culture"),
        ],
        "targets": [
            ("İK Ekipleri", "HR Teams"),
            ("Yöneticiler", "Managers"),
            ("Organizasyon Gelişimi Ekipleri", "Organizational Development Teams"),
        ],
    },
    # ── 6. STRATEJİK İK YÖNETİMİ ────────────────────────────────────────────
    {
        "file": "stratejik-ik-yonetimi.html",
        "p": "stratejik",
        "desc1": (
            "İnsan kaynaklarının organizasyon stratejisine gerçek katkı sağlayabilmesi için stratejik bakış açısı ve doğru araçların kullanılması gerekir. Bu eğitim, İK profesyonellerinin organizasyon içinde stratejik bir iş ortağı olarak konumlanmalarını destekler.",
            "For HR to make a real contribution to organizational strategy, a strategic perspective and the right tools are needed. This training supports HR professionals in positioning themselves as strategic business partners within the organization.",
        ),
        "h3_content": "shared.egitim.h3.icerik",
        "content1": (
            "İnsan kaynaklarının stratejik rolü, HRBP yaklaşımı, stratejik işgücü planlaması, İK metrikleri ve dashboard tasarımı, İK'nın iş sonuçlarına katkısını ölçmek.",
            "The strategic role of HR, the HRBP approach, strategic workforce planning, HR metrics and dashboard design, measuring HR's contribution to business outcomes.",
        ),
        "h3_problems": "shared.egitim.h3.problems",
        "problems1": (
            "İK'nın operasyonel işlerle sınırlı kalması, İK süreçlerinin kurum stratejisiyle yeterince bağlantılı olmaması, İK'nın yönetime değerini anlatmakta zorlanması, insan kaynakları kararlarının veri yerine sezgiye dayanması.",
            "HR remaining limited to operational tasks, HR processes not sufficiently linked to organizational strategy, HR struggling to communicate its value to management, HR decisions based on intuition rather than data.",
        ),
        "h3_gains": "shared.egitim.h3.gains",
        "gains1": (
            "Stratejik İK yaklaşımı, kurum stratejisiyle uyumlu İK uygulamaları, veri destekli İK kararları, yönetimle daha güçlü iş ortaklığı.",
            "A strategic HR approach, HR practices aligned with organizational strategy, data-supported HR decisions, a stronger business partnership with management.",
        ),
        "outcomes": [
            ("İK stratejisini kurum stratejisiyle hizalama", "Aligning HR strategy with organizational strategy"),
            ("Veri destekli İK kararları alma", "Making data-driven HR decisions"),
            ("İK fonksiyonunun etkisini artırma", "Increasing the impact of the HR function"),
            ("HRBP yaklaşımını benimseme", "Adopting the HRBP approach"),
            ("Stratejik işgücü planlaması", "Strategic workforce planning"),
            ("İK metrikleri ve dashboard kullanımı", "Using HR metrics and dashboards"),
        ],
        "targets": [
            ("İK Yöneticileri", "HR Managers"),
            ("HRBP'ler", "HRBPs"),
            ("İK Uzmanları", "HR Specialists"),
        ],
    },
    # ── 7. ÜCRETİN ÖTESİ ────────────────────────────────────────────────────
    {
        "file": "ucretin-otesi.html",
        "p": "ucret",
        "desc1": (
            "Çalışanlar neden işten ayrılır? Araştırmalar gösteriyor ki ücret çoğunlukla birincil neden değildir. Takdir görmemek, büyüme fırsatının olmaması, anlamsızlık hissi ve yöneticiyle ilişki sorunları çok daha belirleyici etkenlerdir.",
            "Why do employees leave? Research shows that pay is often not the primary reason. Lack of recognition, absence of growth opportunities, a sense of meaninglessness, and relationship problems with managers are far more decisive factors.",
        ),
        # desc2 has <strong> → use data-i18n-html
        "desc2_tr": '<strong>Ücretin Ötesi</strong> eğitimi, "Total Rewards" (Bütünsel Ödüllendirme) kavramını merkeze alarak çalışan bağlılığını para dışındaki faktörlerle nasıl inşa edeceğinizi öğretir. Bu, maliyeti düşük ama etkisi yüksek bir liderlik ve İK becerisidir.',
        "desc2_en": '<strong>Beyond Pay</strong> training centers the "Total Rewards" concept to teach you how to build employee engagement through non-monetary factors. This is a high-impact, low-cost leadership and HR skill.',
        "h3_content": "shared.egitim.h3.icerik2",
        "content1": (
            "Çalışan bağlılığı araştırmaları ve nedensellik analizi, Total Rewards çerçevesi ve bileşenleri, anlam ve amaç yönetimi, kariyer gelişimi ve büyüme yolakları tasarımı, takdir ve ödüllendirme sistemleri, esnek çalışma ve iş-yaşam dengesi uygulamaları ve tükenmişliği önleme stratejileri ele alınır.",
            "Employee engagement research and causality analysis, the Total Rewards framework and its components, meaning and purpose management, career development and growth path design, recognition and reward systems, flexible work and work-life balance practices, and burnout prevention strategies are covered.",
        ),
        "h3_content2_key": "egitim.ucret.h3.touch",
        "h3_content2_tr": "Kurum Kültürüne Dokunuş",
        "h3_content2_en": "Impact on Organizational Culture",
        "content2": (
            'Bu eğitim yalnızca İK için değil, tüm yöneticiler için tasarlanmıştır. Çünkü çalışan bağlılığı, yöneticilerin günlük davranış ve kararlarının bir sonucudur. Eğitim sonunda katılımcılar ekiplerine özel bir "Bağlılık Eylem Planı" oluşturur.',
            'This training is designed not only for HR, but for all managers. Because employee engagement is a result of managers\' daily behaviors and decisions. At the end of the training, participants create a customized "Engagement Action Plan" for their teams.',
        ),
        "outcomes": [
            ("Total Rewards yaklaşımını kuruma uyarlamak", "Adapting the Total Rewards approach to the organization"),
            ("Maddi olmayan motivasyon araçlarını etkin kullanmak", "Effectively using non-monetary motivation tools"),
            ("Takdir kültürü oluşturmak", "Building a recognition culture"),
            ("Kariyer yolakları ve gelişim fırsatları sunmak", "Offering career paths and development opportunities"),
            ("Çalışan bağlılığını düzenli ölçmek", "Regularly measuring employee engagement"),
            ("Tükenmişliği önceden tespit etmek ve önlemek", "Early detection and prevention of burnout"),
        ],
        "targets": [
            ("Tüm Yöneticiler", "All Managers"),
            ("İK Uzmanları", "HR Specialists"),
            ("Çalışan Deneyimi Ekipleri", "Employee Experience Teams"),
            ("Kurucu/CEO", "Founder/CEO"),
        ],
    },
    # ── 8. VERİYE DÖNÜŞEN İNSAN ─────────────────────────────────────────────
    {
        "file": "veriye-donusen-insan.html",
        "p": "veri",
        "desc1": (
            "Modern İK'nın en güçlü silahlarından biri veriye dayalı karar alma (People Analytics) yetkinliğidir. Hangi faktörler çalışan ayrılmasını tetikler? Hangi eğitimlerin iş sonuçlarına gerçek katkısı var? Bu soruları yanıtlamak artık mümkün — veri ile.",
            "One of modern HR's most powerful tools is the competency of data-driven decision-making (People Analytics). What factors trigger employee turnover? Which training programs truly contribute to business outcomes? These questions can now be answered — with data.",
        ),
        # desc2 has <strong>
        "desc2_tr": '<strong>Veriye Dönüşen İnsan</strong>, İK profesyonellerini temel veri analizi ve İnsan Analitiği (People Analytics) konusunda yetkin hale getiren pratik odaklı bir eğitimdir. Teknik uzmanlık gerektirmez; İK\'nın veriyi anlayıp kullanmasına odaklanır.',
        "desc2_en": '<strong>HR Driven by Data</strong> is a practice-oriented training that equips HR professionals with essential data analysis and People Analytics skills. No technical expertise is required; it focuses on HR\'s ability to understand and use data.',
        "h3_content": "shared.egitim.h3.icerik2",
        "content1": (
            "İnsan Analitiği'ne giriş ve olgunluk modeli, İK metrikleri ve KPI'lar (devir hızı, devamsızlık, maliyet-per-hire vb.), betimsel, tanısal, öngörücü ve reçeteci analitik düzeyleri, Excel/Google Sheets ile temel İK analizi uygulamaları, İK dashboardı tasarımı, analiz sonuçlarını yönetime sunma ve veriden karar almaya hikâye anlatıcılığı ele alınır.",
            "Introduction to People Analytics and the maturity model, HR metrics and KPIs (turnover rate, absenteeism, cost-per-hire, etc.), descriptive, diagnostic, predictive, and prescriptive analytics levels, basic HR analysis applications with Excel/Google Sheets, HR dashboard design, presenting analysis results to management, and storytelling from data to decision are covered.",
        ),
        "h3_content2_key": "egitim.veri.h3.practical",
        "h3_content2_tr": "Uygulamalı Çalışmalar",
        "h3_content2_en": "Hands-On Practice",
        "content2": (
            "Eğitim boyunca katılımcılar gerçek veri setleriyle (anonim) çalışır. Program sonunda her katılımcı kendi departmanı için temel bir İK analitik raporu şablonu hazırlar.",
            "Throughout the training, participants work with real (anonymized) data sets. At the end of the program, each participant prepares a basic HR analytics report template for their department.",
        ),
        "outcomes": [
            ("Veri destekli İK kararları", "Data-driven HR decisions"),
            ("Organizasyonel içgörü üretme", "Generating organizational insights"),
            ("İK'nın iş sonuçlarına katkısını gösterebilme", "Demonstrating HR's contribution to business outcomes"),
        ],
        "targets": [
            ("İK Yöneticileri", "HR Managers"),
            ("HRBP'ler", "HRBPs"),
            ("İK Analitiği Ekipleri", "HR Analytics Teams"),
        ],
    },
    # ── 9. YAPAY ZEKÂ İK'DA ──────────────────────────────────────────────────
    {
        "file": "yapay-zeka-ikda.html",
        "p": "yz",
        "desc1": (
            "Yapay zekâ artık İK'nın kapısını çalıyor. Özgeçmiş tarama, mülakat değerlendirme, çalışan mobbingi tespiti, öneri sistemleri, chatbotlar ve daha fazlası... YZ, İK süreçlerini kökten dönüştürme potansiyeline sahip.",
            "Artificial intelligence is now knocking on HR's door. Resume screening, interview evaluation, employee well-being monitoring, recommendation systems, chatbots, and more... AI has the potential to fundamentally transform HR processes.",
        ),
        # desc2 has <strong>
        "desc2_tr": "<strong>Yapay Zekâ İK'da</strong> eğitimi, İK profesyonellerini bu dönüşümün pasif izleyicisi olmaktan çıkarıp aktif bir şekillendirici konumuna taşır. Teknik kodlama bilgisi gerekmez; ancak YZ araçlarını bilinçli, etik ve stratejik kullanmak öğrenilebilir.",
        "desc2_en": "<strong>AI in HR</strong> training moves HR professionals from being passive observers of this transformation to active shapers. No technical coding knowledge is required; but using AI tools consciously, ethically, and strategically can be learned.",
        "h3_content": "shared.egitim.h3.icerik2",
        "content1": (
            "YZ'nin İK'ya genel etkisi ve olgunluk modeli, işe alımda YZ: ATS, özgeçmiş tarama, ön mülakat araçları, eğitim ve gelişimde kişiselleştirilmiş öğrenme sistemleri, çalışan deneyiminde chatbotlar ve self-servis İK, analitik ve tahminsel modeller, YZ etiği ve önyargı riski, mevcut İK teknoloji yığınınızı değerlendirme ve ChatGPT/AI asistanlarını İK iş akışlarına entegre etme ele alınır.",
            "The general impact of AI on HR and the maturity model, AI in recruitment: ATS, resume screening, pre-interview tools, personalized learning systems in training and development, chatbots and self-service HR in employee experience, analytics and predictive models, AI ethics and bias risk, evaluating your current HR technology stack, and integrating ChatGPT/AI assistants into HR workflows are covered.",
        ),
        "h3_content2_key": "egitim.yz.h3.tools",
        "h3_content2_tr": "Araç Odaklı Öğrenme",
        "h3_content2_en": "Tool-Focused Learning",
        "content2": (
            "Eğitim boyunca gerçek YZ araçları deneyimlenir. Katılımcılar program sonunda kendi kurumları için bir \"YZ Entegrasyon Yol Haritası\" çıkarır.",
            'Throughout the training, real AI tools are experienced. At the end of the program, participants produce an "AI Integration Roadmap" for their own organizations.',
        ),
        "outcomes": [
            ("İşe alımda YZ araçlarını etkin kullanmak", "Effectively using AI tools in recruitment"),
            ("Kişiselleştirilmiş öğrenme sistemleri kurmak", "Setting up personalized learning systems"),
            ("Chatbot ve self-servis İK modellerini uygulamak", "Implementing chatbot and self-service HR models"),
            ("YZ etiği ve önyargı risklerini yönetmek", "Managing AI ethics and bias risks"),
            ("ChatGPT'yi İK iş akışlarına entegre etmek", "Integrating ChatGPT into HR workflows"),
            ("Kurumun YZ olgunluğunu değerlendirmek", "Assessing the organization's AI maturity"),
        ],
        "targets": [
            ("İK Direktörleri", "HR Directors"),
            ("İK Uzmanları", "HR Specialists"),
            ("HRBP'ler", "HRBPs"),
            ("Dijital dönüşüm meraklısı İK profesyonelleri", "HR professionals interested in digital transformation"),
        ],
    },
    # ── 10. AİDİYET TASARIMI ────────────────────────────────────────────────
    {
        "file": "aidiyet-tasarimi.html",
        "p": "aidiyet",
        "desc1": (
            "Çalışan bağlılığı yalnızca motivasyon faaliyetleriyle değil, doğru tasarlanmış sistemlerle oluşur. Bu eğitim, çalışan deneyimini bütünsel şekilde tasarlamayı ve yönetmeyi amaçlar.",
            "Employee engagement is built not just through motivation activities, but through well-designed systems. This training aims to holistically design and manage the employee experience.",
        ),
        "h3_content": "shared.egitim.h3.icerik",
        "content1": (
            "Çalışan deneyimi kavramı, çalışan yolculuğu haritalama, bağlılık faktörleri, kurum kültürü ve deneyim tasarımı, geri bildirim mekanizmaları konuları ele alınır.",
            "The concept of employee experience, employee journey mapping, engagement factors, organizational culture and experience design, and feedback mechanisms are covered.",
        ),
        "h3_problems": "shared.egitim.h3.problems",
        "problems_ul_tr": (
            '<li style="margin-bottom:8px;">✗ Çalışan bağlılığının düşük olması</li>'
            '<li style="margin-bottom:8px;">✗ Kurum kültürünün çalışan deneyimine yeterince yansımaması</li>'
            '<li style="margin-bottom:8px;">✗ Çalışan geri bildirimlerinin sistematik şekilde değerlendirilmemesi</li>'
            '<li style="margin-bottom:8px;">✗ Yüksek çalışan devir oranı</li>'
        ),
        "problems_ul_en": (
            '<li style="margin-bottom:8px;">✗ Low employee engagement</li>'
            '<li style="margin-bottom:8px;">✗ Organizational culture not sufficiently reflected in employee experience</li>'
            '<li style="margin-bottom:8px;">✗ Employee feedback not being evaluated systematically</li>'
            '<li style="margin-bottom:8px;">✗ High employee turnover rate</li>'
        ),
        "h3_gains": "shared.egitim.h3.gains",
        "gains_ul_tr": (
            '<li style="margin-bottom:8px;">✓ Güçlü çalışan deneyimi yaklaşımı</li>'
            '<li style="margin-bottom:8px;">✓ Artan çalışan bağlılığı</li>'
            '<li style="margin-bottom:8px;">✓ Kurum kültürünün güçlenmesi</li>'
            '<li style="margin-bottom:8px;">✓ Çalışan memnuniyetinin artması</li>'
        ),
        "gains_ul_en": (
            '<li style="margin-bottom:8px;">✓ A strong employee experience approach</li>'
            '<li style="margin-bottom:8px;">✓ Increased employee engagement</li>'
            '<li style="margin-bottom:8px;">✓ Strengthened organizational culture</li>'
            '<li style="margin-bottom:8px;">✓ Increased employee satisfaction</li>'
        ),
        "outcomes": [
            ("Çalışan bağlılığını artıran sistemler", "Systems that increase employee engagement"),
            ("Güçlü kurum kültürü", "A strong organizational culture"),
            ("Sürdürülebilir çalışan deneyimi tasarımı", "Sustainable employee experience design"),
        ],
        "targets": [
            ("İK Ekipleri", "HR Teams"),
            ("Organizasyon Gelişimi Ekipleri", "Organizational Development Teams"),
            ("Yöneticiler", "Managers"),
        ],
    },
]

# ─── BUILD JSON KEYS ───────────────────────────────────────────────────────────
def collect_keys(pages_data):
    keys = dict(SHARED)
    for pg in pages_data:
        p = pg["p"]
        for field in ("desc1", "content1", "problems1", "gains1", "content2"):
            if field in pg:
                keys[f"egitim.{p}.{field}"] = pg[field]
        # desc2 with html
        if "desc2_tr" in pg:
            keys[f"egitim.{p}.desc2"] = (pg["desc2_tr"], pg["desc2_en"])
        # unique h3s
        if "h3_content2_key" in pg:
            keys[pg["h3_content2_key"]] = (pg["h3_content2_tr"], pg["h3_content2_en"])
        # ul-based problems/gains keys
        if "problems_ul_tr" in pg:
            keys[f"egitim.{p}.problems.html"] = (pg["problems_ul_tr"], pg["problems_ul_en"])
        if "gains_ul_tr" in pg:
            keys[f"egitim.{p}.gains.html"] = (pg["gains_ul_tr"], pg["gains_ul_en"])
        # outcomes
        for i, (tr, en) in enumerate(pg.get("outcomes", []), 1):
            keys[f"egitim.{p}.outcome{i}"] = (tr, en)
        # targets
        for i, (tr, en) in enumerate(pg.get("targets", []), 1):
            keys[f"egitim.{p}.target{i}"] = (tr, en)
    return keys


# ─── APPLY HTML CHANGES ────────────────────────────────────────────────────────
def process_html(html, pg):
    p = pg["p"]

    # Helper: add data-i18n to opening <p> tag with specific text content
    def tag_p(text, key, html_attr=False):
        attr = "data-i18n-html" if html_attr else "data-i18n"
        # Replace the <p> opening that directly precedes this text
        old = f"<p>{text}"
        new = f'<p {attr}="egitim.{p}.{key}">{text}'
        return html.replace(old, new, 1)

    def tag_p_with_strong(text_start, key):
        """Tag a <p> that starts with <strong>"""
        old = f"<p><strong>{text_start}"
        new = f'<p data-i18n-html="egitim.{p}.{key}"><strong>{text_start}'
        return html.replace(old, new, 1)

    def tag_h3(text, shared_key=None, page_key=None):
        attr_key = shared_key if shared_key else f"egitim.{p}.{page_key}"
        old = f"<h3>{text}</h3>"
        new = f'<h3 data-i18n="{attr_key}">{text}</h3>'
        return html.replace(old, new, 1)

    def tag_ul(tr_content_flat, key):
        """Add data-i18n-html to <ul> element. tr_content_flat has no newlines between li items
        but the actual file has each <li> on its own line."""
        # Insert newlines between </li><li> to match actual file format
        with_newlines = re.sub(r'(</li>)(<li)', r'\1\n\2', tr_content_flat)
        old = f'<ul style="list-style:none;padding:0;">\n{with_newlines}\n</ul>'
        new = f'<ul data-i18n-html="egitim.{p}.{key}" style="list-style:none;padding:0;">\n{with_newlines}\n</ul>'
        if old not in html:
            # Try flat (no newlines)
            old = f'<ul style="list-style:none;padding:0;">{tr_content_flat}</ul>'
            new = f'<ul data-i18n-html="egitim.{p}.{key}" style="list-style:none;padding:0;">{tr_content_flat}</ul>'
        return html.replace(old, new, 1)

    def tag_outcome_span(text, key):
        old = f"<span>{text}</span>"
        new = f'<span data-i18n="egitim.{p}.{key}">{text}</span>'
        return html.replace(old, new, 1)

    def tag_target(text, key):
        old = f'<div class="target-tag">{text}</div>'
        new = f'<div class="target-tag" data-i18n="egitim.{p}.{key}">{text}</div>'
        return html.replace(old, new, 1)

    # ── desc1 ──
    html = tag_p(pg["desc1"][0], "desc1")

    # ── desc2 (if exists) ──
    if "desc2_tr" in pg:
        # Has <strong> tag
        strong_start = pg["desc2_tr"].split("</strong>")[0].replace("<strong>", "")
        html = tag_p_with_strong(strong_start, "desc2")

    # ── h3: training content ──
    h3_content_key = pg.get("h3_content", "shared.egitim.h3.icerik")
    h3_text = "Eğitimin İçeriği" if h3_content_key.endswith("2") else "Eğitim İçeriği"
    if h3_content_key.startswith("shared."):
        html = tag_h3(h3_text, shared_key=h3_content_key)
    else:
        html = tag_h3(h3_text, page_key=h3_content_key)

    # ── content1 ──
    html = tag_p(pg["content1"][0], "content1")

    # ── h3: problems (shared or none) ──
    if "h3_problems" in pg:
        html = tag_h3("Kurumlar Bu Eğitimle Hangi Sorunları Çözüyor?",
                       shared_key=pg["h3_problems"])

    # ── problems ──
    if "problems1" in pg:
        html = tag_p(pg["problems1"][0], "problems1")
    elif "problems_ul_tr" in pg:
        html = tag_ul(pg["problems_ul_tr"], "problems.html")

    # ── h3: gains (shared or none) ──
    if "h3_gains" in pg:
        html = tag_h3("Kurumlar Bu Eğitim Sonrasında Ne Kazanıyor?",
                       shared_key=pg["h3_gains"])

    # ── gains ──
    if "gains1" in pg:
        html = tag_p(pg["gains1"][0], "gains1")
    elif "gains_ul_tr" in pg:
        html = tag_ul(pg["gains_ul_tr"], "gains.html")

    # ── unique h3_content2 ──
    if "h3_content2_tr" in pg:
        html = tag_h3(pg["h3_content2_tr"], shared_key=pg["h3_content2_key"])

    # ── content2 ──
    if "content2" in pg:
        html = tag_p(pg["content2"][0], "content2")

    # ── outcome items ──
    for i, (tr, _) in enumerate(pg.get("outcomes", []), 1):
        html = tag_outcome_span(tr, f"outcome{i}")

    # ── target tags ──
    for i, (tr, _) in enumerate(pg.get("targets", []), 1):
        html = tag_target(tr, f"target{i}")

    # ── CTA section-tag "Kurumunuza Özel" ──
    old_cta_tag = '<div class="section-tag" style="justify-content:center;margin-bottom:16px;">Kurumunuza Özel</div>'
    new_cta_tag = '<div class="section-tag" data-i18n="shared.egitim.cta.tag" style="justify-content:center;margin-bottom:16px;">Kurumunuza Özel</div>'
    html = html.replace(old_cta_tag, new_cta_tag, 1)

    # ── Hero "Bilgi Al →" button ──
    old_bilgi = '<button class="btn btn-primary btn-lg" onclick="openTeklifModal()">Bilgi Al →</button>'
    new_bilgi = '<button class="btn btn-primary btn-lg" onclick="openTeklifModal()" data-i18n="shared.btn.bilgial">Bilgi Al →</button>'
    html = html.replace(old_bilgi, new_bilgi, 1)

    # ── Hero "💬 WhatsApp" link (hero area) ──
    old_wp_hero = '<a class="btn btn-ghost btn-lg" href="https://wa.me/905330193134" target="_blank">💬 WhatsApp</a>'
    new_wp_hero = '<a class="btn btn-ghost btn-lg" href="https://wa.me/905330193134" target="_blank" data-i18n="shared.btn.whatsapp2">💬 WhatsApp</a>'
    html = html.replace(old_wp_hero, new_wp_hero, 1)

    # ── CTA "💬 WhatsApp'tan Ulaş" link ──
    old_wp_cta = "<a class=\"btn btn-ghost btn-lg\" href=\"https://wa.me/905330193134\" target=\"_blank\">💬 WhatsApp'tan Ulaş</a>"
    new_wp_cta = "<a class=\"btn btn-ghost btn-lg\" href=\"https://wa.me/905330193134\" target=\"_blank\" data-i18n=\"kurs.cta.whatsapp\">💬 WhatsApp'tan Ulaş</a>"
    html = html.replace(old_wp_cta, new_wp_cta, 1)

    return html


# ─── MAIN ──────────────────────────────────────────────────────────────────────
def main():
    tr_path = os.path.join(BASE, 'locales', 'tr.json')
    en_path = os.path.join(BASE, 'locales', 'en.json')

    with open(tr_path, encoding='utf-8') as f: tr_json = json.load(f)
    with open(en_path, encoding='utf-8') as f: en_json = json.load(f)

    keys = collect_keys(PAGES)
    added = 0
    for k, (tr_val, en_val) in keys.items():
        if k not in tr_json:
            tr_json[k] = tr_val
            added += 1
        if k not in en_json:
            en_json[k] = en_val

    with open(tr_path, 'w', encoding='utf-8') as f:
        json.dump(tr_json, f, ensure_ascii=False, indent=2)
    with open(en_path, 'w', encoding='utf-8') as f:
        json.dump(en_json, f, ensure_ascii=False, indent=2)
    print(f"✅ JSON: added {added} new keys.")

    for pg in PAGES:
        path = os.path.join(BASE, 'egitimler', pg["file"])
        with open(path, encoding='utf-8') as f:
            html = f.read()
        original = html
        html = process_html(html, pg)
        if html != original:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"✅ Updated: {pg['file']}")
        else:
            print(f"⚠️  No changes: {pg['file']}")


if __name__ == '__main__':
    main()
