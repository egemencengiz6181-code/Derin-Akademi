#!/usr/bin/env python3
"""
Derin Akademi - Comprehensive i18n Processing Script
=====================================================
This script:
1. Adds data-i18n attributes to all HTML files
2. Generates comprehensive tr.json and en.json
3. Fixes Turkish character issues
4. Normalizes nav/footer/modal across all pages
"""

import os
import re
import json
import glob

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ============================================================
# COMPREHENSIVE TRANSLATION DICTIONARY
# ============================================================

translations = {
    # ═══════════════════ NAVIGATION ═══════════════════
    "nav.egitimler": {"tr": "Eğitimlerimiz", "en": "Training Programs"},
    "nav.danismanlik": {"tr": "Danışmanlıklarımız", "en": "Consulting"},
    "nav.hakkimizda": {"tr": "Kurumsal", "en": "About Us"},
    "nav.blog": {"tr": "Deneyimlerimiz", "en": "Insights"},
    "nav.iletisim": {"tr": "İletişim", "en": "Contact"},
    "nav.teklif": {"tr": "Özel Teklif Al", "en": "Get a Quote"},
    "nav.anasayfa": {"tr": "Ana Sayfa", "en": "Home"},
    "nav.referanslar": {"tr": "Referanslarımız", "en": "References"},

    # ═══════════════════ SHARED BUTTONS ═══════════════════
    "shared.btn.teklif": {"tr": "Teklif Al →", "en": "Get a Quote →"},
    "shared.btn.bilgial": {"tr": "Bilgi Al →", "en": "Find Out More →"},
    "shared.btn.bilgial2": {"tr": "Bilgi Al", "en": "Find Out More"},
    "shared.btn.whatsapp": {"tr": "WhatsApp ile Yaz", "en": "Message on WhatsApp"},
    "shared.btn.whatsapp2": {"tr": "💬 WhatsApp", "en": "💬 WhatsApp"},
    "shared.btn.ozelteklif": {"tr": "Özel Teklif Al", "en": "Get a Custom Quote"},
    "shared.btn.hementeklif": {"tr": "Hemen Teklif Al", "en": "Request a Quote Now"},
    "shared.btn.iletisimgec": {"tr": "İletişime Geç", "en": "Get in Touch"},
    "shared.btn.teklifiste": {"tr": "Teklif İste →", "en": "Request a Quote →"},
    "shared.btn.anasayfa": {"tr": "Ana Sayfa", "en": "Home"},
    "shared.btn.allposts": {"tr": "← Tüm Yazılar", "en": "← All Articles"},
    "shared.btn.consulting": {"tr": "Danışmanlık Al →", "en": "Get Consulting →"},
    "shared.btn.aboneol": {"tr": "Abone Ol", "en": "Subscribe"},
    "shared.btn.gonder": {"tr": "Gönder →", "en": "Send →"},

    # ═══════════════════ SHARED BREADCRUMB ═══════════════════
    "shared.breadcrumb.egitimler": {"tr": "Eğitimlerimiz", "en": "Training Programs"},
    "shared.breadcrumb.danismanlik": {"tr": "Danışmanlıklarımız", "en": "Consulting"},

    # ═══════════════════ SHARED CTA ═══════════════════
    "shared.cta.tag": {"tr": "Kurumunuza Özel", "en": "Tailored for You"},
    "shared.cta.desc": {"tr": "İhtiyaçlarınızı ve hedeflerinizi paylaşın, size özel program ve teklif hazırlayalım.", "en": "Share your needs and goals, and we will prepare a custom program and quote for you."},
    "shared.cta.banner.note": {"tr": "✓ 24 Saat İçinde Yanıt   ✓ Kuruma Özel Çözüm   ✓ 30+ Yıl Deneyim", "en": "✓ Response Within 24 Hours   ✓ Tailored Solution   ✓ 30+ Years of Experience"},

    # ═══════════════════ SHARED FOOTER ═══════════════════
    "shared.footer.brandesc": {"tr": "İnsan kaynakları alanında uzmanlaşmış danışmanlık ve eğitim şirketi. Anlatan değil, çalışan sistemler kurarız.", "en": "A consulting and training company specializing in human resources. We build systems that work, not just talk."},
    "shared.footer.hizmetler": {"tr": "Hizmetler", "en": "Services"},
    "shared.footer.sirket": {"tr": "Şirket", "en": "Company"},
    "shared.footer.iletisim": {"tr": "İletişim", "en": "Contact"},
    "shared.footer.bulten": {"tr": "Bülten", "en": "Newsletter"},
    "shared.footer.bulten.desc": {"tr": "İK gündemindeki gelişmelerden ve eğitimlerimizden haberdar ol.", "en": "Stay updated on HR trends and our training programs."},
    "shared.footer.copy": {"tr": "© 2026 Derin Akademi. Tüm hakları saklıdır.", "en": "© 2026 Derin Akademi. All rights reserved."},
    "shared.footer.gizlilik": {"tr": "Gizlilik Politikası", "en": "Privacy Policy"},
    "shared.footer.kullanim": {"tr": "Kullanım Koşulları", "en": "Terms of Use"},
    "shared.footer.kvkk": {"tr": "KVKK", "en": "KVKK"},
    "shared.footer.cerezler": {"tr": "Çerezler", "en": "Cookies"},
    "shared.footer.kurumsal.egitim": {"tr": "Kurumsal Eğitim", "en": "Corporate Training"},
    "shared.footer.kurumsallasma": {"tr": "Kurumsallaşma", "en": "Institutionalization"},
    "shared.footer.kariyer": {"tr": "Kariyer", "en": "Careers"},

    # ═══════════════════ SHARED MODAL ═══════════════════
    "shared.modal.contact": {"tr": "İletişim Bilgileri", "en": "Contact Information"},
    "shared.modal.title": {"tr": "Hemen", "en": "Get a"},
    "shared.modal.title2": {"tr": "Teklif Alın", "en": "Quote Now"},
    "shared.modal.desc": {"tr": "Eğitim ihtiyaçlarınızı paylaşın, size özel program ve teklif oluşturalım.", "en": "Share your training needs, and we will create a custom program and quote for you."},
    "shared.modal.desc.danis": {"tr": "Danışmanlık ihtiyaçlarınızı paylaşın, size özel program ve teklif oluşturalım.", "en": "Share your consulting needs, and we will create a custom program and quote for you."},
    "shared.modal.phone": {"tr": "Telefon", "en": "Phone"},
    "shared.modal.email": {"tr": "E-posta", "en": "Email"},
    "shared.modal.adres": {"tr": "Adres", "en": "Address"},
    "shared.modal.adres.val": {"tr": "İçerenköy Mah. Topçu İbrahim Sokak Quick Tower Sitesi No:8-10D Ataşehir, İstanbul 34752", "en": "İçerenköy Mah. Topçu İbrahim Sokak Quick Tower Sitesi No:8-10D Ataşehir, Istanbul 34752"},
    "shared.modal.fullname": {"tr": "Ad Soyad *", "en": "Full Name *"},
    "shared.modal.emailfield": {"tr": "E-posta *", "en": "Email *"},
    "shared.modal.phonefield": {"tr": "Telefon *", "en": "Phone *"},
    "shared.modal.company": {"tr": "Kurum / Şirket (İsteğe Bağlı)", "en": "Company (Optional)"},
    "shared.modal.request": {"tr": "Talebiniz *", "en": "Your Request *"},
    "shared.modal.submit": {"tr": "Teklif İste →", "en": "Request a Quote →"},
    "shared.modal.placeholder.name": {"tr": "Adınız Soyadınız", "en": "Your Full Name"},
    "shared.modal.placeholder.email": {"tr": "ornek@mail.com", "en": "example@mail.com"},
    "shared.modal.placeholder.phone": {"tr": "0 5XX XXX XX XX", "en": "0 5XX XXX XX XX"},
    "shared.modal.placeholder.company": {"tr": "Şirketinizin adı", "en": "Your company name"},
    "shared.modal.placeholder.request": {"tr": "İhtiyacınızı ve beklentilerinizi yazın...", "en": "Describe your needs and expectations..."},
    "shared.modal.toast": {"tr": "Talebiniz iletildi! 🎉", "en": "Your request has been submitted! 🎉"},
    "shared.toast.abone": {"tr": "Abone oldunuz! 🎉", "en": "You have subscribed! 🎉"},
    "shared.backtotop": {"tr": "Yukarı dön", "en": "Back to top"},

    # ═══════════════════ SHARED DETAIL PAGES ═══════════════════
    "shared.outcomes.title": {"tr": "Neler Kazanacaksınız?", "en": "What You Will Gain"},
    "shared.targets.label": {"tr": "Kimler İçin?", "en": "Who Is This For?"},
    "shared.process.label": {"tr": "Süreç", "en": "Process"},
    "shared.process.title": {"tr": "Nasıl Çalışıyoruz?", "en": "How Do We Work?"},
    "shared.scope.label": {"tr": "Kapsam", "en": "Scope"},
    "shared.scope.title": {"tr": "Ne Kazanırsınız?", "en": "What Will You Gain?"},
    "shared.for.label": {"tr": "Kimler için", "en": "Who It's For"},
    "shared.for.title": {"tr": "Bu program kime hitap ediyor?", "en": "Who Is This Program For?"},
    "shared.challenge.title": {"tr": "Sorun: Dönemin Gerçekleri", "en": "Challenge: Current Realities"},
    "shared.solution.title": {"tr": "Çözüm: Derin Akademi Yaklaşımı", "en": "Solution: The Derin Akademi Approach"},
    "shared.author.role": {"tr": "30+ Yıllık İK Uzmanı · Kurucu, Derin Akademi · ACC Koç · TEGEP & ICF Üyesi", "en": "30+ Years HR Expert · Founder, Derin Akademi · ACC Coach · TEGEP & ICF Member"},

    # ═══════════════════ SHARED SIDEBAR (BLOG) ═══════════════════
    "shared.sidebar.author": {"tr": "✍️ Yazar Hakkında", "en": "✍️ About the Author"},
    "shared.sidebar.related": {"tr": "📚 İlgili İçerik", "en": "📚 Related Content"},
    "shared.sidebar.consulting": {"tr": "Danışmanlık Alın", "en": "Get Consulting"},
    "shared.sidebar.cta.desc": {"tr": "İK süreçlerinizi stratejik avantaja dönüştürmek için konuşalım.", "en": "Let's talk about turning your HR processes into a strategic advantage."},
    "shared.sidebar.author.bio": {"tr": "Hakan Selahi, 30+ yıllık İK yönetimi ve danışmanlık deneyimiyle Derin Akademi'nin kurucusudur. TEGEP ve ICF üyesidir.", "en": "Hakan Selahi is the founder of Derin Akademi with 30+ years of HR management and consulting experience. He is a member of TEGEP and ICF."},
    "shared.sidebar.author.link": {"tr": "Kurumsal Hakkında →", "en": "About the Company →"},
    "shared.newsletter.title": {"tr": "📬 Bülten", "en": "📬 Newsletter"},
    "shared.newsletter.desc": {"tr": "Yeni yazılardan haberdar olmak için abone olun.", "en": "Subscribe to be notified of new articles."},
    "shared.newsletter.sub": {"tr": "Abone Ol", "en": "Subscribe"},
    "shared.newsletter.placeholder": {"tr": "E-posta", "en": "Email"},

    # ═══════════════════ SECTOR LABELS ═══════════════════
    "sector.finans": {"tr": "Finans", "en": "Finance"},
    "sector.uretim": {"tr": "Üretim", "en": "Manufacturing"},
    "sector.sanayi": {"tr": "Sanayi", "en": "Industry"},
    "sector.tarim": {"tr": "Tarım", "en": "Agriculture"},
    "sector.saglik": {"tr": "Sağlık", "en": "Healthcare"},
    "sector.perakende": {"tr": "Perakende", "en": "Retail"},
    "sector.egitim": {"tr": "Eğitim", "en": "Education"},
    "sector.holding": {"tr": "Holding", "en": "Holding"},
    "sector.insaat": {"tr": "İnşaat", "en": "Construction"},

    # ═══════════════════ INDEX PAGE ═══════════════════
    "idx.hero.tag": {"tr": "İK Danışmanlığı & Kurumsal Eğitim", "en": "HR Consulting & Corporate Training"},
    "idx.hero.line1": {"tr": "Kurumlar", "en": "Organizations"},
    "idx.hero.line2": {"tr": "Değişmez.", "en": "Don't Change."},
    "idx.hero.line3": {"tr": "Sistemler Değişir.", "en": "Systems Do."},
    "idx.hero.desc": {"tr": "İnsan kaynaklarını operasyonel bir destek fonksiyonundan, iş sonuçlarını etkileyen stratejik bir kaldıraca dönüştürüyoruz. Anlatan değil, çalışan sistemler kurarız.", "en": "We transform human resources from an operational support function into a strategic lever that impacts business results. We build systems that work, not just talk."},
    "idx.hero.cta1": {"tr": "Eğitimlerimizi İncele", "en": "Explore Training"},
    "idx.hero.cta2": {"tr": "Danışmanlık", "en": "Consulting"},
    "idx.stat.kurum": {"tr": "Hizmet Verilen Kurum", "en": "Institutions Served"},
    "idx.stat.deneyim": {"tr": "Yıllık Deneyim", "en": "Years of Experience"},
    "idx.stat.egitim": {"tr": "Eğitim Programı", "en": "Training Programs"},
    "idx.stat.sektor": {"tr": "Farklı Sektör", "en": "Different Sectors"},
    "idx.stat.memnuniyet": {"tr": "Müşteri Memnuniyeti", "en": "Client Satisfaction"},
    "idx.ref.scroll": {"tr": "Güvenilen Kurumlar & Referanslar", "en": "Trusted Institutions & References"},
    "idx.feat.tag": {"tr": "Fark Yaratan Unsurlar", "en": "Differentiating Factors"},
    "idx.feat.title": {"tr": "Neden Derin Akademi?", "en": "Why Derin Akademi?"},
    "idx.feat.desc": {"tr": "Hazır paket eğitimler değil; kurumunuza özel, ölçülebilir ve sürdürülebilir çözümler.", "en": "Not off-the-shelf training packages; measurable and sustainable solutions tailored to your institution."},
    "idx.feat.01.title": {"tr": "Sonuç Odaklı Yaklaşım", "en": "Results-Oriented Approach"},
    "idx.feat.01.desc": {"tr": "Her proje, somut iş çıktılarına ve ölçülebilir dönüşüme bağlı hedeflerle başlar. Eğitim veya danışmanlık değil, gerçek değişim.", "en": "Every project starts with goals tied to concrete business outcomes and measurable transformation. Not just training or consulting, but real change."},
    "idx.feat.02.title": {"tr": "Kuruma Özel Tasarım", "en": "Custom-Built Design"},
    "idx.feat.02.desc": {"tr": "Çözümler hazır modellerle değil; kurumun hedefleri, kültürü ve mevcut olgunluk seviyesi dikkate alınarak özel olarak tasarlanır.", "en": "Solutions are not off-the-shelf; they are designed specifically around the institution's goals, culture and maturity level."},
    "idx.feat.03.title": {"tr": "Davranış Dönüşümü", "en": "Behavioral Transformation"},
    "idx.feat.03.desc": {"tr": "Yalnızca bilgi aktarmıyoruz; yönetme, karar alma ve iletişim biçimlerini köklü biçimde dönüştürmeyi hedefliyoruz.", "en": "We don't just transfer knowledge; we aim to fundamentally transform management, decision-making and communication styles."},
    "idx.feat.04.title": {"tr": "YZ Destekli Öğrenme", "en": "AI-Powered Learning"},
    "idx.feat.04.desc": {"tr": "Yapay zekâ destekli, kuruma özel içerikler ve 7/24 erişilebilir dijital avatar desteği ile sürekli öğrenme imkânı.", "en": "AI-powered, institution-specific content and 24/7 accessible digital avatar support for continuous learning."},
    "idx.feat.05.title": {"tr": "Esnek Eğitim Formatları", "en": "Flexible Training Formats"},
    "idx.feat.05.desc": {"tr": "Yüz yüze sınıf eğitimlerinden online interaktif programlara kadar kurumunuzun ihtiyacına en uygun formatta.", "en": "From in-person classroom training to online interactive programs — the format that fits your institution best."},
    "idx.feat.06.title": {"tr": "Sahadaki Uygulama Deneyimi", "en": "Real-World Application"},
    "idx.feat.06.desc": {"tr": "Akademik bilgiyi gerçek iş yaşamından beslenen içgörülerle buluşturarak, klasik kalıpların ötesinde uygulanabilir çözümler sunuyoruz.", "en": "We combine academic knowledge with real business insights to deliver practical solutions beyond conventional models."},
    "idx.feat.07.title": {"tr": "Ölçülebilen Eğitim Çıktıları", "en": "Measurable Training Outcomes"},
    "idx.feat.07.desc": {"tr": "Somut metriklere dayalı başarı takibi, performans dönüşümü ve iş çıktılarına doğrudan etki eden sonuçlar hedefleriz.", "en": "We target measurable success tracking, performance transformation and results that directly impact business outcomes."},
    "idx.train.tag": {"tr": "Eğitimlerimiz", "en": "Training Programs"},
    "idx.train.title": {"tr": "Davranış ve Karar Biçimi", "en": "Behavioral & Decision-Making"},
    "idx.train.title2": {"tr": "Dönüşümü", "en": "Transformation"},
    "idx.train.desc": {"tr": "Liderlikten veriye, performanstan aidiyete — kurumunuzun ihtiyacına özel eğitim programları.", "en": "From leadership to data, from performance to belonging — tailored training programs for your institution."},
    "idx.train.cta": {"tr": "Tüm Eğitimleri Gör", "en": "View All Programs"},
    "idx.sectors.tag": {"tr": "Çalıştığımız Sektörler", "en": "Sectors We Serve"},
    "idx.sectors.title": {"tr": "Farklı Sektörlerde", "en": "Shared Transformation"},
    "idx.sectors.title2": {"tr": "Ortak Dönüşüm", "en": "Across Different Sectors"},
    "idx.sectors.desc": {"tr": "Finans'tan tarıma, sağlıktan perakendeye — 40'tan fazla kurum ile dönüşümün sorumluluğunu birlikte taşıdık.", "en": "From finance to agriculture, healthcare to retail — we have carried the responsibility of transformation with more than 40 institutions."},
    "idx.testi.tag": {"tr": "Başarı Hikayeleri", "en": "Success Stories"},
    "idx.testi.title": {"tr": "Onlar Değiştirdi, Sıra Sende", "en": "They Transformed, Now It's Your Turn"},
    "idx.testi.desc": {"tr": "Gerçek hikayeler, gerçek dönüşümler. 40'tan fazla kurumdan yüzlerce profesyonelin deneyimi.", "en": "Real stories, real transformations. Experiences from hundreds of professionals across 40+ institutions."},
    "idx.cta.title1": {"tr": "Dönüşümün", "en": "Time for"},
    "idx.cta.title2": {"tr": "Zamanı Geldi.", "en": "Transformation."},
    "idx.cta.desc": {"tr": "İnsan kaynağınızı stratejik bir değere dönüştürmek için ilk adımı atalım. Kurumunuza özel çözümler için bize ulaşın.", "en": "Let's take the first step to transform your human resources into a strategic asset. Contact us for solutions tailored to your institution."},
    "idx.cta.note": {"tr": "✓ 24 Saat İçinde Yanıt   ✓ Kuruma Özel Çözüm", "en": "✓ Response Within 24 Hours   ✓ Tailored Solutions"},

    # ═══════════════════ INDEX TESTIMONIALS ═══════════════════
    "idx.testi.1.text": {"tr": "Derin Akademi ile yürüttüğümüz Stratejik İK Yönetimi programı, İK fonksiyonumuzu tamamen dönüştürdü. Artık yönetim kurulunda stratejik ortak olarak konumlanıyoruz.", "en": "The Strategic HR Management program we conducted with Derin Akademi completely transformed our HR function. We are now positioned as a strategic partner at the board level."},
    "idx.testi.1.name": {"tr": "Ayşe Kara", "en": "Ayşe Kara"},
    "idx.testi.1.role": {"tr": "İK Direktörü", "en": "HR Director"},
    "idx.testi.1.sector": {"tr": "Finans Sektörü", "en": "Finance Sector"},
    "idx.testi.2.text": {"tr": "Kurumsallaşma sürecimizde yanımızda olan tek gerçek rehber Derin Akademi oldu. 3. nesle geçiş artık bir kriz değil, planlı bir yolculuk.", "en": "Derin Akademi was the only real guide by our side during our institutionalization process. The transition to the 3rd generation is no longer a crisis, but a planned journey."},
    "idx.testi.2.name": {"tr": "Ali Yalçın", "en": "Ali Yalçın"},
    "idx.testi.2.role": {"tr": "CEO & Kurucu Ortak", "en": "CEO & Co-Founder"},
    "idx.testi.2.sector": {"tr": "Aile Şirketi", "en": "Family Business"},
    "idx.testi.3.text": {"tr": "Performans 360 programı sayesinde yıllık değerlendirmeden sürekli geri bildirim sistemine geçtik. Çalışan memnuniyetimiz %34 arttı.", "en": "Thanks to the Performance 360 program, we moved from annual evaluations to a continuous feedback system. Our employee satisfaction increased by 34%."},
    "idx.testi.3.name": {"tr": "Elif Demir", "en": "Elif Demir"},
    "idx.testi.3.role": {"tr": "İK Müdürü", "en": "HR Manager"},
    "idx.testi.3.sector": {"tr": "Üretim Sektörü", "en": "Manufacturing Sector"},
    "idx.testi.4.text": {"tr": "Mülakat Becerileri 5.0 eğitimi, işe alım kalitemizi tamamen değiştirdi. Artık doğru adayı bulmak değil, kaçırmamak üzerine çalışıyoruz.", "en": "The Interview Skills 5.0 training completely changed our recruitment quality. We now focus on not losing the right candidate rather than finding them."},
    "idx.testi.4.name": {"tr": "Mehmet Öz", "en": "Mehmet Öz"},
    "idx.testi.4.role": {"tr": "Yetenek Edinim Müdürü", "en": "Talent Acquisition Manager"},
    "idx.testi.4.sector": {"tr": "Perakende", "en": "Retail"},
    "idx.testi.5.text": {"tr": "Yapay Zekâ İK'da eğitimiyle ekibimiz, ChatGPT ve AI araçlarını günlük İK süreçlerine entegre etmeyi öğrendi. Verimlilik farkı inanılmaz.", "en": "With the AI in HR training, our team learned to integrate ChatGPT and AI tools into daily HR processes. The efficiency difference is incredible."},
    "idx.testi.5.name": {"tr": "Zeynep Aras", "en": "Zeynep Aras"},
    "idx.testi.5.role": {"tr": "CHRO", "en": "CHRO"},
    "idx.testi.5.sector": {"tr": "Teknoloji", "en": "Technology"},
    "idx.testi.6.text": {"tr": "Ücret ve ödül sistemi danışmanlığıyla yapımızı piyasa verisine dayalı, şeffaf bir modele dönüştürdük. İç adaletsizlik artık gündemde değil.", "en": "With compensation and reward system consulting, we transformed our structure into a transparent, market data-driven model. Internal inequity is no longer on the agenda."},
    "idx.testi.6.name": {"tr": "Burak Eren", "en": "Burak Eren"},
    "idx.testi.6.role": {"tr": "CFO", "en": "CFO"},
    "idx.testi.6.sector": {"tr": "Holding", "en": "Holding"},
    "idx.testi.7.text": {"tr": "Çalışan Deneyimi ve Aidiyet Tasarımı programı tüm çalışan yolculuğunu yeniden tasarlamamızı sağladı. Devir oranımız ilk yılda %28 düştü.", "en": "The Employee Experience and Belonging Design program enabled us to redesign the entire employee journey. Our turnover rate dropped 28% in the first year."},
    "idx.testi.7.name": {"tr": "Selin Aksoy", "en": "Selin Aksoy"},
    "idx.testi.7.role": {"tr": "İK Direktörü", "en": "HR Director"},
    "idx.testi.7.sector": {"tr": "Üretim", "en": "Manufacturing"},
    "idx.testi.8.text": {"tr": "Yeni Nesil Liderlik programıyla orta kademe yöneticilerimiz koçvari bir liderlik anlayışını benimsedi. Ekip performansında gözle görülür artış.", "en": "With the New Generation Leadership program, our mid-level managers adopted a coaching leadership approach. Visible improvement in team performance."},
    "idx.testi.8.name": {"tr": "Can Yıldız", "en": "Can Yıldız"},
    "idx.testi.8.role": {"tr": "CEO", "en": "CEO"},
    "idx.testi.8.sector": {"tr": "İnşaat & GYO", "en": "Construction & REIT"},
    "idx.testi.9.text": {"tr": "Veri Odaklı İK Yönetimi eğitimiyle İK dashboardlarımızı kurarak yönetim kurulu raporlama kalitemizi tamamen dönüştürdük.", "en": "With the Data-Driven HR Management training, we built our HR dashboards and completely transformed our board-level reporting quality."},
    "idx.testi.9.name": {"tr": "Deniz Koç", "en": "Deniz Koç"},
    "idx.testi.9.role": {"tr": "İK Analitiği Yöneticisi", "en": "HR Analytics Manager"},
    "idx.testi.9.sector": {"tr": "Finans", "en": "Finance"},

    # ═══════════════════ INDEX COURSE CARDS ═══════════════════
    "idx.course.liderlik.cat": {"tr": "Liderlik & İletişim", "en": "Leadership & Communication"},
    "idx.course.liderlik.title": {"tr": "Yeni Nesil Liderlik", "en": "New Generation Leadership"},
    "idx.course.liderlik.desc": {"tr": "Klasik yönetim anlayışından çıkarak güven, gelişim ve performans odaklı bir liderlik yaklaşımı geliştirin.", "en": "Move beyond classical management to develop a leadership approach focused on trust, growth and performance."},
    "idx.course.stratejik.cat": {"tr": "Sistem & Yönetim", "en": "Systems & Management"},
    "idx.course.stratejik.title": {"tr": "Stratejik İK Yönetimi", "en": "Strategic HR Management"},
    "idx.course.stratejik.desc": {"tr": "İK profesyonellerinin organizasyon içinde stratejik bir iş ortağı olarak konumlanmasını destekleyin.", "en": "Support HR professionals in positioning themselves as strategic business partners within the organization."},
    "idx.course.yz.cat": {"tr": "Yapay Zekâ ve Geleceğin İK'sı", "en": "AI & the Future of HR"},
    "idx.course.yz.title": {"tr": "Yapay Zekâ İK'da", "en": "AI in HR"},
    "idx.course.yz.desc": {"tr": "AI araçlarını İK süreçlerine entegre ederek verimlilik ve karar kalitesini artırın.", "en": "Integrate AI tools into HR processes to increase efficiency and decision quality."},

    # ═══════════════════ KURSLAR PAGE ═══════════════════
    "kurs.hero.tag": {"tr": "İK Dönüşüm Akademisi", "en": "HR Transformation Academy"},
    "kurs.hero.title1": {"tr": "İK Dönüşüm", "en": "HR Transformation"},
    "kurs.hero.title2": {"tr": "Akademisi", "en": "Academy"},
    "kurs.hero.desc": {"tr": "İnsan Kaynaklarını stratejik bir iş ortağına dönüştüren gelişim alanları. Liderlik, İK sistemleri, veri kullanımı ve yapay zekâ uygulamalarını kapsayan dört ana yetkinlik alanı.", "en": "Development areas that transform Human Resources into a strategic business partner. Four core competency areas covering leadership, HR systems, data utilization and AI applications."},
    "kurs.stat.egitim": {"tr": "Eğitim Programı", "en": "Training Programs"},
    "kurs.stat.kategori": {"tr": "Kategori", "en": "Categories"},
    "kurs.stat.kurum": {"tr": "Hizmet Verilen Kurum", "en": "Institutions Served"},
    "kurs.stat.memnuniyet": {"tr": "Memnuniyet", "en": "Satisfaction"},
    "kurs.stat.sektor": {"tr": "Farklı Sektör", "en": "Different Sectors"},
    "kurs.cat.liderlik": {"tr": "Liderlik & İletişim", "en": "Leadership & Communication"},
    "kurs.cat.sistem": {"tr": "Sistem & Yönetim", "en": "Systems & Management"},
    "kurs.cat.veri": {"tr": "Veri Odaklı İK", "en": "Data-Driven HR"},
    "kurs.cat.yz": {"tr": "Yapay Zekâ ve Geleceğin İK'sı", "en": "AI & the Future of HR"},
    "kurs.cta.tag": {"tr": "Kurumunuza Özel", "en": "Tailored for You"},
    "kurs.cta.title": {"tr": "Hangi Eğitim Kurumunuza Uygun?", "en": "Which Training Fits Your Institution?"},
    "kurs.cta.desc": {"tr": "Eğitim ihtiyacınızı paylaşın, kurumunuza özel program ve yaklaşım önerelim.", "en": "Share your training needs, and we'll recommend a program and approach tailored to your institution."},
    "kurs.cta.whatsapp": {"tr": "💬 WhatsApp'tan Ulaş", "en": "💬 Contact via WhatsApp"},

    # ═══════════════════ KURSLAR COURSE CARDS ═══════════════════
    "kurs.liderlik.title": {"tr": "Yeni Nesil Liderlik", "en": "New Generation Leadership"},
    "kurs.liderlik.desc": {"tr": "Klasik yönetim anlayışından çıkarak güven, gelişim ve performans odaklı bir liderlik yaklaşımı geliştirin.", "en": "Move beyond classical management to develop a leadership approach focused on trust, growth and performance."},
    "kurs.geribildirim.title": {"tr": "Etkin Geri Bildirim ve Zor Konuşmalar", "en": "Effective Feedback & Difficult Conversations"},
    "kurs.geribildirim.desc": {"tr": "Açık ve yapıcı geri bildirim verme becerilerini geliştirin, zor konuşmaları sağlıklı şekilde yönetin.", "en": "Develop skills for giving open, constructive feedback and managing difficult conversations in a healthy way."},
    "kurs.kapsayici.title": {"tr": "Kapsayıcı Liderlik", "en": "Inclusive Leadership"},
    "kurs.kapsayici.desc": {"tr": "Kapsayıcı liderlik yaklaşımını benimseyin, ekiplerde farklılıkları avantaja dönüştürün.", "en": "Adopt an inclusive leadership approach and turn diversity in teams into a competitive advantage."},
    "kurs.mulakat.title": {"tr": "Mülakat Becerileri 5.0", "en": "Interview Skills 5.0"},
    "kurs.mulakat.desc": {"tr": "Davranış odaklı mülakat teknikleri ile adayların yetkinliklerini daha doğru değerlendirin ve işe alım süreçlerini sistematik hale getirin.", "en": "Evaluate candidates more accurately using behavioral interview techniques and systematize recruitment processes."},
    "kurs.stratejik.title": {"tr": "Stratejik İK Yönetimi", "en": "Strategic HR Management"},
    "kurs.stratejik.desc": {"tr": "İK profesyonellerinin organizasyon içinde stratejik bir iş ortağı olarak konumlanmasını destekleyin.", "en": "Support HR professionals in positioning themselves as strategic business partners within the organization."},
    "kurs.perf360.title": {"tr": "Performans 360", "en": "Performance 360"},
    "kurs.perf360.desc": {"tr": "Kurumlarda sürdürülebilir ve gelişim odaklı bir performans yönetim sistemi kurun.", "en": "Build a sustainable, development-oriented performance management system in organizations."},
    "kurs.ucret.title": {"tr": "Stratejik Ücret ve Ödül Yönetimi", "en": "Strategic Compensation & Reward Management"},
    "kurs.ucret.desc": {"tr": "Stratejik ve sürdürülebilir ücret politikalarıyla çalışan bağlılığını ve performansı destekleyin.", "en": "Support employee engagement and performance with strategic and sustainable compensation policies."},
    "kurs.aidiyet.title": {"tr": "Çalışan Deneyimi ve Aidiyet Tasarımı", "en": "Employee Experience & Belonging Design"},
    "kurs.aidiyet.desc": {"tr": "Çalışan deneyimini bütünsel şekilde tasarlayarak bağlılık ve kurum kültürünü güçlendirin.", "en": "Strengthen engagement and organizational culture by designing the employee experience holistically."},
    "kurs.veri.title": {"tr": "Veri Odaklı İK Yönetimi", "en": "Data-Driven HR Management"},
    "kurs.veri.desc": {"tr": "İK profesyonellerinin veri analizi ve metrikleri kullanarak daha güçlü kararlar almasını sağlayın.", "en": "Enable HR professionals to make stronger decisions using data analysis and metrics."},
    "kurs.yz.title": {"tr": "Yapay Zekâ İK'da", "en": "AI in HR"},
    "kurs.yz.desc": {"tr": "AI araçlarını İK süreçlerine entegre ederek verimlilik ve karar kalitesini artırın.", "en": "Integrate AI tools into HR processes to increase efficiency and decision quality."},

    # ═══════════════════ DANISMANLIK PAGE ═══════════════════
    "danis.hero.tag": {"tr": "İK Danışmanlığı", "en": "HR Consulting"},
    "danis.hero.title1": {"tr": "İK ve Yönetim", "en": "HR & Management"},
    "danis.hero.title2": {"tr": "Değişimi Danışmanlığı", "en": "Transformation Consulting"},
    "danis.hero.desc": {"tr": "İnsan kaynakları sistemlerini stratejik ve sürdürülebilir hale getiren danışmanlık alanları. Kurumların ihtiyaçlarına göre farklı başlıklarda planlanabilir.", "en": "Consulting areas that make human resources systems strategic and sustainable. Can be planned under different headings according to institutional needs."},
    "danis.stat.alan": {"tr": "Danışmanlık Alanı", "en": "Consulting Areas"},
    "danis.stat.kurum": {"tr": "Hizmet Verilen Kurum", "en": "Institutions Served"},
    "danis.stat.deneyim": {"tr": "Yıllık Deneyim", "en": "Years of Experience"},
    "danis.stat.sektor": {"tr": "Farklı Sektör", "en": "Different Sectors"},
    "danis.stat.memnuniyet": {"tr": "Müşteri Memnuniyeti", "en": "Client Satisfaction"},
    "danis.section.tag": {"tr": "8 Danışmanlık Programı", "en": "8 Consulting Programs"},
    "danis.section.title1": {"tr": "Kurumunuza Özel", "en": "Custom Solutions"},
    "danis.section.title2": {"tr": "Çözüm Alanları", "en": "For Your Institution"},
    "danis.section.desc": {"tr": "Her danışmanlık çalışması, kurumunuzun ihtiyaçlarına göre farklı başlıklarda planlanabilir.", "en": "Each consulting engagement can be planned under different headings based on your institution's needs."},
    "danis.cat.liderlik": {"tr": "Liderlik & Organizasyon Gelişimi", "en": "Leadership & Organizational Development"},
    "danis.cat.sistem": {"tr": "Sistem & Yönetim", "en": "Systems & Management"},
    "danis.cat.veri": {"tr": "Veri Odaklı İK", "en": "Data-Driven HR"},
    "danis.cat.yz": {"tr": "Yapay Zekâ ve Geleceğin İK'sı", "en": "AI & the Future of HR"},

    # Danışmanlık items
    "danis.strateji.num": {"tr": "01 — Liderlik & Organizasyon Gelişimi", "en": "01 — Leadership & Organizational Development"},
    "danis.strateji.title": {"tr": "Vizyon, Misyon ve Strateji Tasarımı", "en": "Vision, Mission & Strategy Design"},
    "danis.strateji.sub": {"tr": "Kurumsal Yönü Netleştirmek", "en": "Clarifying Corporate Direction"},
    "danis.strateji.desc": {"tr": "Kurumların uzun vadeli yönünü netleştiren vizyon ve misyonun oluşturulması, stratejik hedeflerin belirlenmesi ve operasyonel hedeflere dönüştürülmesi.", "en": "Establishing the vision and mission that clarifies the long-term direction, defining strategic goals and translating them into operational objectives."},
    "danis.aileden.num": {"tr": "02 — Liderlik & Organizasyon Gelişimi", "en": "02 — Leadership & Organizational Development"},
    "danis.aileden.title": {"tr": "Aile Şirketlerinden Kurumsal Yönetime Geçiş", "en": "From Family Business to Corporate Governance"},
    "danis.aileden.sub": {"tr": "Sürdürülebilir Büyümenin Yol Haritası", "en": "Roadmap for Sustainable Growth"},
    "danis.aileden.desc": {"tr": "Aile şirketlerinde sürdürülebilir büyümeyi destekleyen kurumsal yönetim yapısının oluşturulması ve profesyonel yönetim sistemlerinin kurulması.", "en": "Establishing a corporate governance structure that supports sustainable growth in family businesses and building professional management systems."},
    "danis.kadro.num": {"tr": "03 — Sistem & Yönetim", "en": "03 — Systems & Management"},
    "danis.kadro.title": {"tr": "İK Planlama ve Organizasyon Tasarımı", "en": "HR Planning & Organizational Design"},
    "danis.kadro.sub": {"tr": "Büyümeye Uygun Yapı Tasarımı", "en": "Designing Structures for Growth"},
    "danis.kadro.desc": {"tr": "Kurumların büyüme hedeflerini destekleyen organizasyon yapısının ve insan kaynağı planlamasının oluşturulması.", "en": "Establishing the organizational structure and human resource planning that supports the institution's growth objectives."},
    "danis.olc.num": {"tr": "04 — Sistem & Yönetim", "en": "04 — Systems & Management"},
    "danis.olc.title": {"tr": "Performans Yönetim Sistemi Kurulumu", "en": "Performance Management System Setup"},
    "danis.olc.sub": {"tr": "Strateji ile Uyumlu Performans", "en": "Performance Aligned with Strategy"},
    "danis.olc.desc": {"tr": "Bireysel ve ekip performansını kurum stratejisiyle uyumlu şekilde ölçen ve geliştiren sürdürülebilir bir performans yönetim sistemi kurmak.", "en": "Building a sustainable performance management system that measures and develops individual and team performance in alignment with institutional strategy."},
    "danis.ucret.num": {"tr": "05 — Sistem & Yönetim", "en": "05 — Systems & Management"},
    "danis.ucret.title": {"tr": "Ücret ve Yan Haklar Sistemi Tasarımı", "en": "Compensation & Benefits System Design"},
    "danis.ucret.sub": {"tr": "Adil ve Rekabetçi Ücret Yapısı", "en": "Fair and Competitive Compensation"},
    "danis.ucret.desc": {"tr": "Kurumlarda sürdürülebilir, adil ve rekabetçi bir ücret ve yan haklar sistemi oluşturarak çalışan bağlılığını ve performansı desteklemek.", "en": "Building a sustainable, fair and competitive compensation and benefits system that supports employee engagement and performance."},
    "danis.yetenek.num": {"tr": "06 — Sistem & Yönetim", "en": "06 — Systems & Management"},
    "danis.yetenek.title": {"tr": "İşe Alım ve Yetenek Yönetimi Sistemi", "en": "Recruitment & Talent Management System"},
    "danis.yetenek.sub": {"tr": "Doğru Yetenekleri Çekmek ve Geliştirmek", "en": "Attracting and Developing the Right Talent"},
    "danis.yetenek.desc": {"tr": "Kurumların doğru yetenekleri çekmesini, geliştirmesini ve elde tutmasını sağlayan sistematik bir yetenek yönetimi yaklaşımı kurmak.", "en": "Building a systematic talent management approach that enables institutions to attract, develop and retain the right talent."},
    "danis.guclen.num": {"tr": "07 — Veri Odaklı İK", "en": "07 — Data-Driven HR"},
    "danis.guclen.title": {"tr": "İK Analitiği Altyapısı Kurulumu", "en": "HR Analytics Infrastructure Setup"},
    "danis.guclen.sub": {"tr": "Veri Destekli İK Kararları", "en": "Data-Driven HR Decisions"},
    "danis.guclen.desc": {"tr": "İnsan kaynakları kararlarının veri ile desteklenmesini sağlayan analitik altyapıyı kurmak.", "en": "Building the analytics infrastructure that enables data-driven human resources decisions."},
    "danis.hoshin.num": {"tr": "08 — Yapay Zekâ ve Geleceğin İK'sı", "en": "08 — AI & the Future of HR"},
    "danis.hoshin.title": {"tr": "İK Süreçlerinde Yapay Zekâ Uygulamaları", "en": "AI Applications in HR Processes"},
    "danis.hoshin.sub": {"tr": "Geleceğe Hazır İK Fonksiyonu", "en": "Future-Ready HR Function"},
    "danis.hoshin.desc": {"tr": "Yapay zekâ araçlarının insan kaynakları süreçlerine entegre edilmesini sağlayarak verimlilik ve karar kalitesini artırmak.", "en": "Integrating AI tools into human resources processes to increase efficiency and decision quality."},

    # Danışmanlık page - Approach section
    "danis.approach.tag": {"tr": "Danışmanlık Felsefemiz", "en": "Our Consulting Philosophy"},
    "danis.approach.title1": {"tr": "Stratejiyi Sunumdan", "en": "From Presentations to"},
    "danis.approach.title2": {"tr": "Sahaya İndiriyoruz", "en": "Real-World Execution"},
    "danis.approach.desc": {"tr": "Güzel sunumlar, kalın raporlar ve teorik öneriler üretmiyoruz. Kurumunuzun gerçeklerine dokunan, uygulanabilir ve ölçülebilir sistemler kuruyoruz.", "en": "We don't produce pretty presentations, thick reports and theoretical recommendations. We build practical and measurable systems that address your institution's realities."},
    "danis.approach.1.title": {"tr": "Tanı Önce, Çözüm Sonra", "en": "Diagnose First, Solve Second"},
    "danis.approach.1.desc": {"tr": "Probleminizi derinlemesine analiz etmeden çözüm önermiyoruz. Her danışmanlık süreci, kurumunuzu anlamakla başlar.", "en": "We don't propose solutions without in-depth analysis of the problem. Every consulting process starts with understanding your institution."},
    "danis.approach.2.title": {"tr": "Seninle İnşa Ederiz", "en": "We Build With You"},
    "danis.approach.2.desc": {"tr": "Çözümleri dışarıdan dayatmıyor, kurumunuzun içindeki insanlarla birlikte tasarlıyoruz. Sahiplenme kalıcılığı getirir.", "en": "We don't impose solutions from outside; we design them together with your people. Ownership brings sustainability."},
    "danis.approach.3.title": {"tr": "Kuruma Özel Her Zaman", "en": "Always Custom-Built"},
    "danis.approach.3.desc": {"tr": "Hazır şablon çözümler sunmuyoruz. Her müdahale, kurumunuzun kültürü, büyüklüğü ve sektörüne göre özelleştirilir.", "en": "We don't offer template solutions. Every intervention is customized based on your institution's culture, size and industry."},
    "danis.approach.4.title": {"tr": "Ölçülemeyen Değişmez", "en": "What Can't Be Measured Can't Change"},
    "danis.approach.4.desc": {"tr": "Her danışmanlık sürecinde başarı kriterleri ve ölçüm mekanizmalarını baştan tanımlarız. Sonuçları birlikte izleriz.", "en": "We define success criteria and measurement mechanisms from the start in every consulting process. We monitor results together."},
    "danis.approach.5.title": {"tr": "Sürekli Öğrenen Sistem", "en": "Continuously Learning System"},
    "danis.approach.5.desc": {"tr": "Danışmanlık bittiğinde kurumu terk etmiyoruz. Kurumunuzun kendi kendine öğrenen ve adapte olan bir yapıya kavuşmasını sağlarız.", "en": "We don't leave when consulting ends. We ensure your institution becomes a self-learning, self-adapting structure."},
    "danis.approach.6.title": {"tr": "Sahadaki 30 Yıl", "en": "30 Years in the Field"},
    "danis.approach.6.desc": {"tr": "Önerilerimiz akademik değil, sahadaki deneyimden beslenir. Kurucumuz Hakan Selahi'nin 30+ yıllık pratik bilgisi her projede aktif rol oynar.", "en": "Our recommendations are not academic; they are fed by field experience. Our founder Hakan Selahi's 30+ years of practical knowledge plays an active role in every project."},

    # Danışmanlık page - Sector section
    "danis.sectors.tag": {"tr": "Çalıştığımız Sektörler", "en": "Sectors We Serve"},
    "danis.sectors.title1": {"tr": "Farklı Sektörlerde", "en": "Shared Transformation"},
    "danis.sectors.title2": {"tr": "Ortak Dönüşüm", "en": "Across Sectors"},
    "danis.sectors.desc": {"tr": "Finans, üretim, sanayi, tarım, sağlık, perakende ve eğitim başta olmak üzere birbirinden farklı pek çok sektörde kurumlarla çalıştık.", "en": "We have worked with institutions across many different sectors, including finance, manufacturing, industry, agriculture, healthcare, retail and education."},

    # Danışmanlık page - CTA
    "danis.cta.tag": {"tr": "Ücretsiz Ön Görüşme", "en": "Free Initial Consultation"},
    "danis.cta.title1": {"tr": "Dönüşümünüzü", "en": "Let's Design Your"},
    "danis.cta.title2": {"tr": "Birlikte Tasarlayalım", "en": "Transformation Together"},
    "danis.cta.desc": {"tr": "Hangi alandan ihtiyacınız olduğunu paylaşın, size özel danışmanlık programı ve yaklaşım önerelim. İlk görüşme ücretsizdir.", "en": "Share which area you need, and we'll recommend a consulting program and approach. The first consultation is free."},
    "danis.cta.btn1": {"tr": "Hemen Başlayalım →", "en": "Let's Start →"},
    "danis.cta.btn2": {"tr": "💬 WhatsApp'tan Yazın", "en": "💬 Message on WhatsApp"},
    "danis.cta.note1": {"tr": "Kuruma Özel Çözüm", "en": "Custom Solution"},
    "danis.cta.note2": {"tr": "Ücretsiz Ön Görüşme", "en": "Free Consultation"},
    "danis.cta.note3": {"tr": "40+ Kurum Deneyimi", "en": "40+ Institutions"},
    "danis.cta.note4": {"tr": "Uygulanabilir Sistemler", "en": "Implementable Systems"},

    # ═══════════════════ HAKKIMIZDA PAGE ═══════════════════
    "hkm.hero.tag": {"tr": "Hakkımızda", "en": "About Us"},
    "hkm.hero.title": {"tr": "Eğitim ve İK Danışmanlığında Yılların Tecrübesi", "en": "Years of Experience in Training & HR Consulting"},
    "hkm.hero.desc": {"tr": "Derin Akademi, insan kaynakları alanında uzmanlaşmış bir danışmanlık ve eğitim şirketidir. İK'yı operasyonel bir destek fonksiyonundan, iş sonuçlarını etkileyen stratejik bir kaldıraca dönüştürüyoruz.", "en": "Derin Akademi is a consulting and training company specializing in human resources. We transform HR from an operational support function into a strategic lever that impacts business results."},
    "hkm.stat.kurum": {"tr": "Hizmet Verilen Kurum", "en": "Institutions Served"},
    "hkm.stat.tecrube": {"tr": "Yıllık Tecrübe", "en": "Years of Experience"},
    "hkm.stat.memnuniyet": {"tr": "Memnuniyet", "en": "Satisfaction"},
    "hkm.stat.sektor": {"tr": "Farklı Sektör", "en": "Different Sectors"},
    "hkm.felsefe.tag": {"tr": "Dönüşüm Felsefemiz", "en": "Our Philosophy"},
    "hkm.felsefe.title": {"tr": "Anlatan Değil, Çalışan Sistemler Kurarız", "en": "We Build Systems That Work, Not Just Talk"},
    "hkm.felsefe.desc1": {"tr": "Derin Akademi, insan kaynakları alanında kurumlarla birlikte dönüşümü yöneten bir danışmanlık ve eğitim şirketidir. Klasik eğitim satışı ya da yüzeysel danışmanlık sunmak yerine, her kurumun ihtiyacına göre özelleştirilmiş, uygulanabilir ve sürdürülebilir çözümler tasarlıyoruz.", "en": "Derin Akademi is a consulting and training company that manages transformation together with institutions in the human resources field. Instead of selling conventional training or offering superficial consulting, we design customized, applicable and sustainable solutions tailored to each institution's needs."},
    "hkm.felsefe.desc2": {"tr": "Bugüne kadar 40'tan fazla kurumla yürütülen çalışmalar tek bir ilkeye dayanır: \"Anlatan değil, çalışan sistemler kurmak.\"", "en": "Work carried out with more than 40 institutions to date is based on a single principle: \"Building systems that work, not just talk.\""},
    "hkm.felsefe.btn1": {"tr": "Eğitimlerimiz", "en": "Training Programs"},
    "hkm.felsefe.btn2": {"tr": "Danışmanlık", "en": "Consulting"},
    "hkm.felsefe.card1.label": {"tr": "Davranış Dönüşümü", "en": "Behavioral Transformation"},
    "hkm.felsefe.card1.sub": {"tr": "Karar & yönetim biçimi", "en": "Decision & management style"},
    "hkm.felsefe.card2.label": {"tr": "Stratejik İK", "en": "Strategic HR"},
    "hkm.felsefe.card2.sub": {"tr": "Operasyonelden stratejiye", "en": "From operational to strategic"},
    "hkm.felsefe.card3.label": {"tr": "Kuruma Özel", "en": "Custom-Built"},
    "hkm.felsefe.card3.sub": {"tr": "Hazır model yok", "en": "No off-the-shelf models"},
    "hkm.degerler.tag": {"tr": "Değerlerimiz", "en": "Our Values"},
    "hkm.degerler.title": {"tr": "İlkelerimiz Bizi Biz Yapar", "en": "Our Principles Define Us"},
    "hkm.deger.1.title": {"tr": "Derinlik Üzerine", "en": "Depth Over Surface"},
    "hkm.deger.1.desc": {"tr": "Yüzeysel içerik değil, konseptin özüne inen, uygulamalı, derinlemesine programlar tasarlıyoruz.", "en": "We design in-depth, hands-on programs that go to the core of the concept, not superficial content."},
    "hkm.deger.2.title": {"tr": "Topluluk Odaklı", "en": "Community-Focused"},
    "hkm.deger.2.desc": {"tr": "Öğrenciler, eğitmenler ve sektör profesyonelleriyle güçlü bir topluluk ekosistemi oluşturuyoruz.", "en": "We build a strong community ecosystem with students, trainers and industry professionals."},
    "hkm.deger.3.title": {"tr": "Sürekli Yenilik", "en": "Continuous Innovation"},
    "hkm.deger.3.desc": {"tr": "Teknoloji hızla değişiyor. İçeriklerimizi, sektörün en güncel ihtiyaçlarını yansıtacak şekilde güncelliyoruz.", "en": "Technology is changing rapidly. We update our content to reflect the most current industry needs."},
    "hkm.deger.4.title": {"tr": "Netice Odaklılık", "en": "Results-Driven"},
    "hkm.deger.4.desc": {"tr": "Hedefimiz diploma değil, gerçek kariyer başarısı. Her program somut çıktılar üzerine tasarlanmış.", "en": "Our goal is not diplomas, but real career success. Every program is designed around concrete outcomes."},
    "hkm.deger.5.title": {"tr": "Erişilebilirlik", "en": "Accessibility"},
    "hkm.deger.5.desc": {"tr": "Kaliteli eğitim bir ayrıcalık değil hak. Burs ve indirim programlarıyla herkese ulaşıyoruz.", "en": "Quality education is a right, not a privilege. We reach everyone with scholarship and discount programs."},
    "hkm.deger.6.title": {"tr": "Şeffaflık", "en": "Transparency"},
    "hkm.deger.6.desc": {"tr": "Öğrenci geri bildirimleri herkese açık. İyileştirme süreçlerimiz toplulukla birlikte yürütülüyor.", "en": "Student feedback is open to everyone. Our improvement processes are carried out with the community."},
    "hkm.kurucu.tag": {"tr": "Kurucumuz", "en": "Our Founder"},
    "hkm.kurucu.name": {"tr": "Hakan Selahi", "en": "Hakan Selahi"},
    "hkm.kurucu.role": {"tr": "İK Stratejisti · ACC Koç · Kurumsallaşma Danışmanı ve Eğitmeni", "en": "HR Strategist · ACC Coach · Institutionalization Consultant & Trainer"},
    "hkm.kurucu.bio1": {"tr": "30+ yıllık tecrübeyle Derin Akademi'nin kurucusu Hakan Selahi, kurumsal dönüşümün sahada nasıl yapıldığını bilen nadir profesyonellerden biridir. CHRO deneyimi, onlarca sektörde danışmanlık geçmişi ve yüzlerce eğitim programıyla Türkiye'nin İK dönüşüm ekosisteminde öncü bir isimdir.", "en": "With 30+ years of experience, Hakan Selahi, founder of Derin Akademi, is one of the rare professionals who knows how corporate transformation is done in the field. With CHRO experience, consulting background across dozens of sectors and hundreds of training programs, he is a pioneer in Turkey's HR transformation ecosystem."},
    "hkm.kurucu.bio2": {"tr": "Uzmanlık alanları: Kurumsallaşma tasarımı, performans ve yetenek yönetimi, liderlik gelişimi, stratejik İK danışmanlığı.", "en": "Areas of expertise: Institutionalization design, performance and talent management, leadership development, strategic HR consulting."},
    "hkm.kurucu.chip": {"tr": "CHRO Deneyimi", "en": "CHRO Experience"},
    "hkm.kurucu.memberships": {"tr": "Adler ACC Sertifikalı Koç · NLP Uygulayıcısı · TEGEP Üyesi · ICF Üyesi", "en": "Adler ACC Certified Coach · NLP Practitioner · TEGEP Member · ICF Member"},
    "hkm.kurucu.btn1": {"tr": "Teklif Al", "en": "Get a Quote"},
    "hkm.kurucu.btn2": {"tr": "Bize Ulaş", "en": "Contact Us"},
    "hkm.cta.tag": {"tr": "Katıl", "en": "Join Us"},
    "hkm.cta.title": {"tr": "Dönüşümün Bir Parçası Ol", "en": "Be Part of the Transformation"},
    "hkm.cta.desc": {"tr": "İK'nızı stratejik bir değere dönüştürmek için kurumunuza özel program hazırlayalım. Hemen ulaşın.", "en": "Let us prepare a custom program for your institution to transform your HR into a strategic asset. Contact us now."},
    "hkm.cta.btn1": {"tr": "Özel Teklif Al", "en": "Get a Custom Quote"},
    "hkm.cta.btn2": {"tr": "Eğitimlerimiz", "en": "Training Programs"},

    # ═══════════════════ İLETİŞİM PAGE ═══════════════════
    "ilet.hero.tag": {"tr": "İletişim", "en": "Contact"},
    "ilet.hero.title": {"tr": "Yardım için Buradayız", "en": "We're Here to Help"},
    "ilet.hero.desc": {"tr": "Sorularınız, önerileriniz veya kurumsal çözüm talepleriniz için bize ulaşın — 24 saat içinde yanıt veriyoruz.", "en": "Contact us for your questions, suggestions or corporate solution requests — we respond within 24 hours."},
    "ilet.info.tag": {"tr": "Bilgilerimiz", "en": "Our Information"},
    "ilet.info.title": {"tr": "Bizimle İletişime Geçin", "en": "Get in Touch With Us"},
    "ilet.info.desc": {"tr": "Formdan mesaj gönderebilir, e-posta atabilir ya da sosyal medya üzerinden ulaşabilirsiniz.", "en": "You can send a message via the form, email us, or reach us through social media."},
    "ilet.info.adres": {"tr": "Adres", "en": "Address"},
    "ilet.info.telefon": {"tr": "Telefon", "en": "Phone"},
    "ilet.info.email": {"tr": "E-posta", "en": "Email"},
    "ilet.info.saatler": {"tr": "Çalışma Saatleri", "en": "Working Hours"},
    "ilet.info.saatler.val": {"tr": "Hafta içi 09:00 – 18:00 (TST)", "en": "Weekdays 09:00 – 18:00 (TRT)"},
    "ilet.form.title": {"tr": "Mesaj Gönderin", "en": "Send a Message"},
    "ilet.form.subtitle": {"tr": "Yanıt süresi en fazla 24 saattir.", "en": "Response time is at most 24 hours."},
    "ilet.form.ad": {"tr": "Ad", "en": "First Name"},
    "ilet.form.soyad": {"tr": "Soyad", "en": "Last Name"},
    "ilet.form.email": {"tr": "E-posta", "en": "Email"},
    "ilet.form.telefon": {"tr": "Telefon (İsteğe Bağlı)", "en": "Phone (Optional)"},
    "ilet.form.konu": {"tr": "Konu", "en": "Subject"},
    "ilet.form.konu.sec": {"tr": "Konu seçin…", "en": "Select a subject…"},
    "ilet.form.konu.kurs": {"tr": "Kurs & İçerik", "en": "Course & Content"},
    "ilet.form.konu.destek": {"tr": "Teknik Destek", "en": "Technical Support"},
    "ilet.form.konu.fatura": {"tr": "Fatura & Ödeme", "en": "Invoice & Payment"},
    "ilet.form.konu.sertifika": {"tr": "Sertifika", "en": "Certificate"},
    "ilet.form.konu.kurumsal": {"tr": "Kurumsal Çözümler", "en": "Corporate Solutions"},
    "ilet.form.konu.egitmen": {"tr": "Eğitmen Olmak İstiyorum", "en": "I Want to Be a Trainer"},
    "ilet.form.konu.basin": {"tr": "Basın & Medya", "en": "Press & Media"},
    "ilet.form.konu.diger": {"tr": "Diğer", "en": "Other"},
    "ilet.form.mesaj": {"tr": "Mesajınız", "en": "Your Message"},
    "ilet.form.kvkk": {"tr": "KVKK Aydınlatma Metni'ni okudum, onaylıyorum.", "en": "I have read and accept the KVKK Disclosure Text."},
    "ilet.form.submit": {"tr": "Gönder →", "en": "Send →"},
    "ilet.form.toast": {"tr": "Mesajınız iletildi! 🎉 En kısa sürede yanıt vereceğiz.", "en": "Your message has been sent! 🎉 We will respond as soon as possible."},
    "ilet.form.placeholder.ad": {"tr": "Adınız", "en": "Your first name"},
    "ilet.form.placeholder.soyad": {"tr": "Soyadınız", "en": "Your last name"},
    "ilet.form.placeholder.email": {"tr": "ornek@mail.com", "en": "example@mail.com"},
    "ilet.form.placeholder.tel": {"tr": "+90 5XX XXX XX XX", "en": "+90 5XX XXX XX XX"},
    "ilet.form.placeholder.mesaj": {"tr": "Mesajınızı buraya yazın…", "en": "Write your message here…"},

    # ═══════════════════ KARİYER PAGE ═══════════════════
    "kar.hero.tag": {"tr": "İş Fırsatları", "en": "Job Opportunities"},
    "kar.hero.title": {"tr": "Geleceği Birlikte İnşa Edelim", "en": "Let's Build the Future Together"},
    "kar.hero.desc": {"tr": "Derin Akademi'de çalışmak, Türkiye'nin teknoloji eğitim ekosistemini şekillendirmeye ortak olmaktır. Yetenekli, tutkulu ekibimize katıl.", "en": "Working at Derin Akademi means partnering in shaping Turkey's technology education ecosystem. Join our talented, passionate team."},
    "kar.form.tag": {"tr": "Başvuru", "en": "Application"},
    "kar.form.title": {"tr": "Başvurunu Yap", "en": "Submit Your Application"},
    "kar.form.desc": {"tr": "Başvurunu bırak, ekibimiz en kısa sürede seninle iletişime geçecek.", "en": "Submit your application, and our team will get in touch with you as soon as possible."},
    "kar.form.ad": {"tr": "Ad *", "en": "First Name *"},
    "kar.form.soyad": {"tr": "Soyad *", "en": "Last Name *"},
    "kar.form.email": {"tr": "E-posta *", "en": "Email *"},
    "kar.form.telefon": {"tr": "Telefon *", "en": "Phone *"},
    "kar.form.linkedin": {"tr": "LinkedIn Profili", "en": "LinkedIn Profile"},
    "kar.form.portfolio": {"tr": "Portfolio / GitHub / Web Sitesi", "en": "Portfolio / GitHub / Website"},
    "kar.form.tanitim": {"tr": "Kendinizi Tanıtın *", "en": "Tell Us About Yourself *"},
    "kar.form.cv": {"tr": "Özgeçmiş (CV) *", "en": "Resume (CV) *"},
    "kar.form.cv.desc": {"tr": "📎 CV dosyanızı seçin veya sürükleyin (PDF, DOCX — max 5MB)", "en": "📎 Select or drag your CV file (PDF, DOCX — max 5MB)"},
    "kar.form.kvkk": {"tr": "KVKK Aydınlatma Metni'ni okudum. Kişisel verilerimin işlenmesine, başvuru sürecinde kullanılmasına ve Derin Akademi tarafından 6 ay süreyle saklanmasına onay veriyorum.", "en": "I have read the KVKK Disclosure Text. I consent to the processing of my personal data, its use during the application process, and its retention by Derin Akademi for 6 months."},
    "kar.form.submit": {"tr": "Başvurumu Gönder →", "en": "Submit Application →"},
    "kar.form.kvkk.toast": {"tr": "Lütfen KVKK metnini onaylayın.", "en": "Please accept the KVKK text."},
    "kar.form.toast": {"tr": "Başvurunuz alındı! 🎉 En kısa sürede sizinle iletişime geçeceğiz.", "en": "Your application has been received! 🎉 We will contact you as soon as possible."},
    "kar.neden.tag": {"tr": "Neden Biz?", "en": "Why Us?"},
    "kar.neden.desc": {"tr": "Çalışanlarımız için en iyi ortamı sunmayı önceliğimiz olarak görüyoruz.", "en": "We prioritize providing the best environment for our employees."},
    "kar.neden.1.title": {"tr": "Büyüme Fırsatı", "en": "Growth Opportunity"},
    "kar.neden.1.desc": {"tr": "Sürekli öğrenmeyi destekleyen bir ortamda hızla gelişin. Tüm platformumuza ve kaynaklarımıza sınırsız erişim.", "en": "Grow rapidly in an environment that supports continuous learning. Unlimited access to all our platforms and resources."},
    "kar.neden.2.title": {"tr": "Uzaktan & Esnek", "en": "Remote & Flexible"},
    "kar.neden.2.desc": {"tr": "Tam uzaktan veya hibrit çalışma modeli. Sonuç odaklı çalışma kültürü; işin nerede yapıldığı değil, nasıl yapıldığı önemli.", "en": "Fully remote or hybrid work model. Results-oriented work culture; what matters is not where the work is done, but how."},
    "kar.neden.3.title": {"tr": "Etki & Anlam", "en": "Impact & Purpose"},
    "kar.neden.3.desc": {"tr": "42.000+ öğrencinin kariyer dönüşümüne doğrudan katkı sağlayın. Yaptığınız işin fark yarattığını her gün hissedin.", "en": "Directly contribute to the career transformation of 42,000+ students. Feel the difference your work makes every day."},
    "kar.neden.4.title": {"tr": "Güçlü Ekip", "en": "Strong Team"},
    "kar.neden.4.desc": {"tr": "Alanında uzman, birbirini destekleyen ve sürekli öğrenen bir ekiple çalışın. Açık iletişim ve psikolojik güvenlik önceliğimiz.", "en": "Work with a team of experts who support each other and continuously learn. Open communication and psychological safety are our priorities."},
    "kar.neden.5.title": {"tr": "Rekabetçi Ücret", "en": "Competitive Pay"},
    "kar.neden.5.desc": {"tr": "Piyasa ortalamasının üzerinde maaş, performans primi ve öz sermaye programı ile çalışanlarımızı değerinin üstünde tutuyoruz.", "en": "We value our employees above market with above-average salary, performance bonuses and equity programs."},
    "kar.neden.6.title": {"tr": "Eğitim Desteği", "en": "Training Support"},
    "kar.neden.6.desc": {"tr": "Tüm Derin Akademi kurslarına sınırsız erişim, yıllık eğitim bütçesi, konferans ve sertifika desteği.", "en": "Unlimited access to all Derin Akademi courses, annual training budget, conference and certification support."},

    # ═══════════════════ BLOG PAGE ═══════════════════
    "blog.hero.tag": {"tr": "Deneyimlerimiz", "en": "Insights"},
    "blog.hero.title": {"tr": "İK ve Liderlik Üzerine Derin Düşünceler", "en": "Deep Thoughts on HR and Leadership"},
    "blog.hero.desc": {"tr": "Sahadan gelen gözlemler, araştırmaya dayalı çıkarımlar ve kurumsal dönüşüm üzerine gerçek içgörüler.", "en": "Observations from the field, research-based insights and real perspectives on corporate transformation."},
    "blog.kurucu.tag": {"tr": "Kurucumuz", "en": "Our Founder"},
    "blog.kurucu.name": {"tr": "Hakan Selahi", "en": "Hakan Selahi"},
    "blog.kurucu.role": {"tr": "İK Stratejisti · ACC Koç · Kurumsallaşma Danışmanı", "en": "HR Strategist · ACC Coach · Institutionalization Consultant"},
    "blog.kurucu.bio": {"tr": "30+ yıllık tecrübe ile insan kaynakları alanında yüzlerce kurumu stratejik dönüşüm sürecinde yönetmiştir. Bu yazılar da ona ait derinlemesine düşünceler, sahadan gelen gözlemler ve kurumsal yaşamın gerçek içgörüleridir.", "en": "Having managed hundreds of institutions through strategic transformation in the HR field with 30+ years of experience. These articles are his in-depth thoughts, field observations and real insights from corporate life."},
    "blog.kurucu.link": {"tr": "Hakkında Daha Fazla →", "en": "Learn More →"},
    "blog.yazilar.title": {"tr": "Yazılarımız", "en": "Our Articles"},
    "blog.filter.tumu": {"tr": "Tümü", "en": "All"},
    "blog.filter.liderlik": {"tr": "Liderlik", "en": "Leadership"},
    "blog.filter.isealim": {"tr": "İşe Alım", "en": "Recruitment"},
    "blog.filter.performans": {"tr": "Performans", "en": "Performance"},
    "blog.filter.stratejik": {"tr": "Stratejik İK", "en": "Strategic HR"},
    "blog.filter.yz": {"tr": "YZ & İK", "en": "AI & HR"},
    "blog.filter.kurumsal": {"tr": "Kurumsal", "en": "Corporate"},
    "blog.featured.badge": {"tr": "Öne Çıkan", "en": "Featured"},
    "blog.feat.cat": {"tr": "Liderlik", "en": "Leadership"},
    "blog.feat.date": {"tr": "Haziran 2025", "en": "June 2025"},
    "blog.feat.read": {"tr": "7 dk okuma", "en": "7 min read"},
    "blog.feat.title": {"tr": "Geri Bildirim Kültürü Nasıl İnşa Edilir?", "en": "How to Build a Feedback Culture?"},
    "blog.feat.excerpt": {"tr": "Kurumda gerçek bir geri bildirim kültürü kurmak yalnızca anket göndermekten ibaret değil; psikolojik güvenlik, lider tutarlılığı ve ritüellerle örülmüş bir sistem gerektiriyor.", "en": "Building a real feedback culture in an organization is not just about sending surveys; it requires a system woven with psychological safety, leader consistency and rituals."},
    "blog.feat.btn": {"tr": "Yazıyı Oku →", "en": "Read Article →"},
    "blog.post.yz.cat": {"tr": "YZ & İK", "en": "AI & HR"},
    "blog.post.yz.title": {"tr": "Yapay Zekâ İşe Alımı Nasıl Değiştiriyor?", "en": "How Is AI Transforming Recruitment?"},
    "blog.post.yz.excerpt": {"tr": "CV taramasından yetkinlik değerlendirmesine kadar yapay zekanın İK süreçlerine etkisi ve dikkat edilmesi gereken tuzaklar.", "en": "The impact of AI on HR processes from CV screening to competency assessment, and the pitfalls to watch out for."},
    "blog.post.yz.meta": {"tr": "Mayıs 2025 · 6 dk", "en": "May 2025 · 6 min"},
    "blog.post.perf.cat": {"tr": "Performans", "en": "Performance"},
    "blog.post.perf.title": {"tr": "Performans Yönetiminde Yapılan 5 Kritik Hata", "en": "5 Critical Mistakes in Performance Management"},
    "blog.post.perf.excerpt": {"tr": "Yıllık değerlendirme döngüsünden hedef belirsizliğine kadar kurumların tekrarladığı performans hataları.", "en": "Performance mistakes that institutions repeat, from annual evaluation cycles to goal ambiguity."},
    "blog.post.perf.meta": {"tr": "Nisan 2025 · 8 dk", "en": "April 2025 · 8 min"},
    "blog.post.aile.cat": {"tr": "Kurumsal", "en": "Corporate"},
    "blog.post.aile.title": {"tr": "Aile Şirketi Kurumsallaşırken Neden Başarısız Olur?", "en": "Why Do Family Businesses Fail During Institutionalization?"},
    "blog.post.aile.excerpt": {"tr": "Aile şirketinin kurumsal bir yapıya geçiş sürecinde karşılaştığı en yaygın tuzaklar ve çözüm önerileri.", "en": "The most common pitfalls family businesses face during corporate transition and solution recommendations."},
    "blog.post.aile.meta": {"tr": "Mart 2025 · 9 dk", "en": "March 2025 · 9 min"},
    "blog.post.isguc.cat": {"tr": "Stratejik İK", "en": "Strategic HR"},
    "blog.post.isguc.title": {"tr": "İşgücü Planlaması 2026: Neden Şimdi Başlamalısınız?", "en": "Workforce Planning 2026: Why Start Now?"},
    "blog.post.isguc.excerpt": {"tr": "Demografik dalgalanmalar, teknoloji yetkinlik boşlukları ve belirsiz ekonomik tabloda proaktif kadro planlamasının önemi.", "en": "The importance of proactive workforce planning amid demographic fluctuations, technology skill gaps and uncertain economic conditions."},
    "blog.post.isguc.meta": {"tr": "Şubat 2025 · 7 dk", "en": "February 2025 · 7 min"},
    "blog.btn.oku": {"tr": "Oku →", "en": "Read →"},
    "blog.video.title": {"tr": "Video İçerikleri", "en": "Video Content"},
    "blog.video.placeholder": {"tr": "Yükleme bekleniyor", "en": "Loading..."},
    "blog.sidebar.bulten.title": {"tr": "Bültene Abone Ol", "en": "Subscribe to Newsletter"},
    "blog.sidebar.bulten.desc": {"tr": "İK gündemindeki gelişmeler ve yeni yazılarımız için haftada bir e-posta.", "en": "A weekly email about HR trends and our new articles."},
    "blog.sidebar.populer": {"tr": "Popüler Yazılar", "en": "Popular Articles"},
    "blog.sidebar.populer.1": {"tr": "Geri Bildirim Kültürü Nasıl İnşa Edilir?", "en": "How to Build a Feedback Culture?"},
    "blog.sidebar.populer.2": {"tr": "Performansta 5 Kritik Hata", "en": "5 Critical Mistakes in Performance"},
    "blog.sidebar.populer.3": {"tr": "Aile Şirketi Kurumsallaşmasından Başarısızlık", "en": "Failure in Family Business Institutionalization"},
    "blog.sidebar.populer.4": {"tr": "YZ ve İşe Alım", "en": "AI and Recruitment"},
    "blog.sidebar.populer.5": {"tr": "İşgücü Planlaması 2026", "en": "Workforce Planning 2026"},
    "blog.sidebar.etiketler": {"tr": "Etiketler", "en": "Tags"},
    "blog.tag.liderlik": {"tr": "Liderlik", "en": "Leadership"},
    "blog.tag.isealim": {"tr": "İşe Alım", "en": "Recruitment"},
    "blog.tag.performans": {"tr": "Performans", "en": "Performance"},
    "blog.tag.yetenek": {"tr": "Yetenek", "en": "Talent"},
    "blog.tag.kurumsallasma": {"tr": "Kurumsallaşma", "en": "Institutionalization"},
    "blog.tag.okr": {"tr": "OKR", "en": "OKR"},
    "blog.tag.yz": {"tr": "Yapay Zekâ", "en": "Artificial Intelligence"},
    "blog.tag.geribildirim": {"tr": "Geri Bildirim", "en": "Feedback"},
    "blog.tag.kocluk": {"tr": "Koçluk", "en": "Coaching"},
    "blog.tag.ucret": {"tr": "Ücret", "en": "Compensation"},
    "blog.sidebar.danismanlik.title": {"tr": "Kurumunuza Özel Danışmanlık", "en": "Custom Consulting for Your Institution"},
    "blog.sidebar.danismanlik.desc": {"tr": "İK süreçlerinizi stratejik bir rekabet avantajına dönüştürmek için konuşalım.", "en": "Let's talk about turning your HR processes into a strategic competitive advantage."},

    # ═══════════════════ REFERANSLAR PAGE ═══════════════════
    "ref.hero.tag": {"tr": "Referanslarımız", "en": "Our References"},
    "ref.hero.title": {"tr": "40+ Kurumun Güveni", "en": "Trusted by 40+ Institutions"},
    "ref.hero.desc": {"tr": "Finans, sağlık, üretim, perakende ve daha birçok sektörde kurumlarla çalıştık ve değer yaratmaya devam ediyoruz.", "en": "We have worked with institutions across finance, healthcare, manufacturing, retail and many more sectors, and continue to create value."},
    "ref.kurumlar.title": {"tr": "Hizmet Verdiğimiz Kurumlar", "en": "Institutions We Serve"},
    "ref.testi.tag": {"tr": "Başarı Hikayeleri", "en": "Success Stories"},
    "ref.testi.title": {"tr": "Onlar Değiştirdi, Sıra Sende", "en": "They Transformed, Now It's Your Turn"},
    "ref.testi.desc": {"tr": "Gerçek hikayeler, gerçek dönüşümler. 40'tan fazla kurumdan yüzlerce profesyonelin deneyimi.", "en": "Real stories, real transformations. Experiences from hundreds of professionals across 40+ institutions."},

    # ═══════════════════ LEGAL PAGES ═══════════════════
    "legal.yasal": {"tr": "Yasal Bilgiler", "en": "Legal Information"},
    "legal.guncelleme": {"tr": "Son Güncelleme:", "en": "Last Updated:"},
    "legal.yururluk": {"tr": "Yürürlük:", "en": "Effective:"},
    "legal.versiyon": {"tr": "Versiyon:", "en": "Version:"},

    # Çerez
    "legal.cerez.title": {"tr": "Çerez Politikası", "en": "Cookie Policy"},
    # Gizlilik
    "legal.gizlilik.title": {"tr": "Gizlilik Politikası", "en": "Privacy Policy"},
    # Kullanım Koşulları
    "legal.kullanim.title": {"tr": "Kullanım Koşulları", "en": "Terms of Use"},
    # KVKK
    "legal.kvkk.title": {"tr": "KVKK Aydınlatma Metni", "en": "KVKK Disclosure Text"},

    # ═══════════════════ EĞİTİM SUBPAGES (existing + extended) ═══════════════════
    "egitim.liderlik.category": {"tr": "Liderlik & İletişim", "en": "Leadership & Communication"},
    "egitim.liderlik.title": {"tr": "🎯 Yeni Nesil Liderlik", "en": "🎯 New Generation Leadership"},
    "egitim.liderlik.subtitle": {"tr": "Klasik yönetim anlayışından çıkarak güven, gelişim ve performans odaklı bir liderlik yaklaşımı geliştirin.", "en": "Move beyond classical management to develop a leadership approach focused on trust, growth and performance."},
    "egitim.liderlik.cta.title": {"tr": "Yeni Nesil Liderlik Eğitimini Kurumunuza Uyarlayalım", "en": "Let's Tailor the New Generation Leadership Training to Your Institution"},
    "egitim.stratejik.category": {"tr": "Sistem & Yönetim", "en": "Systems & Management"},
    "egitim.stratejik.title": {"tr": "🎯 Stratejik İK Yönetimi", "en": "🎯 Strategic HR Management"},
    "egitim.stratejik.subtitle": {"tr": "İK profesyonellerinin organizasyon içinde stratejik bir iş ortağı olarak konumlanmasını destekleyin.", "en": "Support HR professionals in positioning themselves as strategic business partners within the organization."},
    "egitim.stratejik.cta.title": {"tr": "Stratejik İK Yönetimi Eğitimini Kurumunuza Uyarlayalım", "en": "Let's Tailor the Strategic HR Management Training to Your Institution"},
    "egitim.yz.category": {"tr": "Veri & Gelecek", "en": "Data & Future"},
    "egitim.yz.title": {"tr": "🤖 Yapay Zekâ İK'da", "en": "🤖 AI in HR"},
    "egitim.yz.subtitle": {"tr": "İnsan gücüne dijital dokunuş. YZ araçlarını İK süreçlerine entegre ederek geleceğe hazır İK ekipleri oluşturun.", "en": "A digital touch to human capital. Build future-ready HR teams by integrating AI tools into HR processes."},
    "egitim.yz.cta.title": {"tr": "Yapay Zekâ İK'da Eğitimini Kurumunuza Uyarlayalım", "en": "Let's Tailor the AI in HR Training to Your Institution"},
    "egitim.aidiyet.category": {"tr": "Sistem & Yönetim", "en": "Systems & Management"},
    "egitim.aidiyet.title": {"tr": "👥 Çalışan Deneyimi ve Aidiyet Tasarımı", "en": "👥 Employee Experience & Belonging Design"},
    "egitim.aidiyet.subtitle": {"tr": "Çalışan bağlılığı yalnızca motivasyon faaliyetleriyle değil, doğru tasarlanmış sistemlerle oluşur. Çalışan deneyimini bütünsel şekilde tasarlamayı ve yönetmeyi amaçlar.", "en": "Employee engagement is built not only through motivation activities but through well-designed systems. This program aims to design and manage the employee experience holistically."},
    "egitim.aidiyet.cta.title": {"tr": "Çalışan Deneyimi ve Aidiyet Tasarımı Eğitimini Kurumunuza Uyarlayalım", "en": "Let's Tailor the Employee Experience & Belonging Design Training to Your Institution"},
    "egitim.haddini.category": {"tr": "Liderlik & İletişim", "en": "Leadership & Communication"},
    "egitim.haddini.title": {"tr": "🎯 Etkin Geri Bildirim ve Zor Konuşmalar", "en": "🎯 Effective Feedback & Difficult Conversations"},
    "egitim.haddini.subtitle": {"tr": "Açık ve yapıcı geri bildirim verme becerilerini geliştirin, zor konuşmaları sağlıklı şekilde yönetin.", "en": "Develop skills for giving open, constructive feedback and managing difficult conversations in a healthy way."},
    "egitim.haddini.cta.title": {"tr": "Etkin Geri Bildirim Eğitimini Kurumunuza Uyarlayalım", "en": "Let's Tailor the Effective Feedback Training to Your Institution"},
    "egitim.kapsayan.category": {"tr": "Liderlik & İletişim", "en": "Leadership & Communication"},
    "egitim.kapsayan.title": {"tr": "🎯 Kapsayıcı Liderlik", "en": "🎯 Inclusive Leadership"},
    "egitim.kapsayan.subtitle": {"tr": "Kapsayıcı liderlik yaklaşımını benimseyin, ekiplerde farklılıkları avantaja dönüştürün.", "en": "Adopt an inclusive leadership approach and turn diversity in teams into a competitive advantage."},
    "egitim.kapsayan.cta.title": {"tr": "Kapsayıcı Liderlik Eğitimini Kurumunuza Uyarlayalım", "en": "Let's Tailor the Inclusive Leadership Training to Your Institution"},
    "egitim.mulakat.category": {"tr": "Sistem & Yönetim", "en": "Systems & Management"},
    "egitim.mulakat.title": {"tr": "🎯 Mülakat Becerileri 5.0", "en": "🎯 Interview Skills 5.0"},
    "egitim.mulakat.subtitle": {"tr": "Davranış odaklı mülakat teknikleri ile adayların yetkinliklerini daha doğru değerlendirin.", "en": "Evaluate candidates' competencies more accurately using behavioral interview techniques."},
    "egitim.mulakat.cta.title": {"tr": "Mülakat Becerileri 5.0 Eğitimini Kurumunuza Uyarlayalım", "en": "Let's Tailor the Interview Skills 5.0 Training to Your Institution"},
    "egitim.perf360.category": {"tr": "Sistem & Yönetim", "en": "Systems & Management"},
    "egitim.perf360.title": {"tr": "🌟 Performans 360", "en": "🌟 Performance 360"},
    "egitim.perf360.subtitle": {"tr": "Performans yönetimi yalnızca yıl sonu değerlendirmelerinden ibaret değildir. Kurumlarda sürdürülebilir ve gelişim odaklı bir performans yönetim sistemi kurulmasını amaçlar.", "en": "Performance management is not just about year-end appraisals. This program aims to establish a sustainable, development-oriented performance management system in organizations."},
    "egitim.perf360.cta.title": {"tr": "Performans 360 Eğitimini Kurumunuza Uyarlayalım", "en": "Let's Tailor the Performance 360 Training to Your Institution"},
    "egitim.ucret.category": {"tr": "Sistem & Yönetim", "en": "Systems & Management"},
    "egitim.ucret.title": {"tr": "💰 Stratejik Ücret ve Ödül Yönetimi", "en": "💰 Strategic Compensation & Reward Management"},
    "egitim.ucret.subtitle": {"tr": "Ücret ve ödül sistemleri çalışan bağlılığı ve organizasyon performansı üzerinde doğrudan etkilidir. Kurumlarda stratejik ve sürdürülebilir ücret politikalarının oluşturulmasını amaçlar.", "en": "Compensation and reward systems directly impact employee engagement and organizational performance. This program aims to build strategic and sustainable compensation policies in organizations."},
    "egitim.ucret.cta.title": {"tr": "Stratejik Ücret ve Ödül Yönetimi Eğitimini Kurumunuza Uyarlayalım", "en": "Let's Tailor the Strategic Compensation & Reward Management Training to Your Institution"},
    "egitim.veri.category": {"tr": "Veri Odaklı İK", "en": "Data-Driven HR"},
    "egitim.veri.title": {"tr": "📊 Veri Odaklı İK Yönetimi", "en": "📊 Data-Driven HR Management"},
    "egitim.veri.subtitle": {"tr": "Modern insan kaynakları fonksiyonu giderek daha fazla veri ile yönetilmektedir. İK profesyonellerinin veri analizi ve metrikleri kullanarak daha güçlü kararlar almasını sağlar.", "en": "The modern HR function is increasingly managed by data. This program enables HR professionals to make better decisions using data analysis and metrics."},
    "egitim.veri.cta.title": {"tr": "Veri Odaklı İK Yönetimi Eğitimini Kurumunuza Uyarlayalım", "en": "Let's Tailor the Data-Driven HR Management Training to Your Institution"},

    # ═══════════════════ DANIŞMANLIK SUBPAGES (existing + extended) ═══════════════════
    # aileden-kuruma.html (already has full i18n in existing JSON - re-include for completeness)
    "danis.aileden.category": {"tr": "Liderlik & Organizasyon Gelişimi", "en": "Leadership & Organizational Development"},
    "danis.aileden.subtitle": {"tr": "Aile şirketlerinde sürdürülebilir büyümeyi destekleyen kurumsal yönetim yapısının oluşturulması ve profesyonel yönetim sistemlerinin kurulması.", "en": "Establishing a corporate governance structure that supports sustainable growth in family businesses and building professional management systems."},
    "danis.aileden.stat1": {"tr": "Aile Şirketi Projesi", "en": "Family Business Projects"},
    "danis.aileden.stat2": {"tr": "Yıl Dönüşüm Süreci", "en": "Year Transformation Process"},
    "danis.aileden.stat3": {"tr": "Müşteri Devamlılığı", "en": "Client Retention"},
    "danis.aileden.prob1": {"tr": "Rol ve sorumlulukların net olmaması", "en": "Lack of clarity in roles and responsibilities"},
    "danis.aileden.prob2": {"tr": "Karar alma süreçlerinde belirsizlik", "en": "Ambiguity in decision-making processes"},
    "danis.aileden.prob3": {"tr": "Aile üyeleri ve profesyonel yöneticiler arasında denge kurulamaması", "en": "Inability to balance family members and professional managers"},
    "danis.aileden.sol1": {"tr": "Organizasyon yapısının yeniden tasarlanması", "en": "Redesigning the organizational structure"},
    "danis.aileden.sol2": {"tr": "Rol ve sorumlulukların netleştirilmesi", "en": "Clarifying roles and responsibilities"},
    "danis.aileden.sol3": {"tr": "Karar alma süreçlerinin tanımlanması", "en": "Defining decision-making processes"},
    "danis.aileden.sol4": {"tr": "Yönetim yapısının profesyonelleştirilmesi", "en": "Professionalizing the management structure"},
    "danis.aileden.sol5": {"tr": "Kurumsal yönetim ilkelerinin oluşturulması", "en": "Establishing corporate governance principles"},
    "danis.aileden.step1.title": {"tr": "Durum Analizi", "en": "Situation Analysis"},
    "danis.aileden.step1.desc": {"tr": "Şirketin mevcut organizasyonel yapısı, aile dinamikleri ve kritik gerilim noktaları haritalanır.", "en": "The company's current organizational structure, family dynamics and critical tension points are mapped."},
    "danis.aileden.step2.title": {"tr": "Paydaş Görüşmeleri", "en": "Stakeholder Interviews"},
    "danis.aileden.step2.desc": {"tr": "Aile üyeleri ve kilit yöneticilerle derinlemesine mülakatlar yürütülür.", "en": "In-depth interviews are conducted with family members and key managers."},
    "danis.aileden.step3.title": {"tr": "Yapı Tasarımı", "en": "Structure Design"},
    "danis.aileden.step3.desc": {"tr": "Organizasyon şeması, görev tanımları ve yetki matrisi birlikte oluşturulur.", "en": "The organizational chart, job descriptions and authority matrix are developed together."},
    "danis.aileden.step4.title": {"tr": "Aile Anayasası", "en": "Family Constitution"},
    "danis.aileden.step4.desc": {"tr": "Temettü, çalışma kuralları, nesil geçişi ve çatışma çözüm mekanizmaları yazılı hale getirilir.", "en": "Dividend policies, employment rules, generational succession and conflict resolution mechanisms are formalized."},
    "danis.aileden.step5.title": {"tr": "Uygulama Desteği", "en": "Implementation Support"},
    "danis.aileden.step5.desc": {"tr": "Değişim sürecinde yönetim kurulu toplantıları ve süreç koçluğu ile yan yana yürünür.", "en": "Board meetings and process coaching accompany the change journey throughout."},
    "danis.aileden.val1.title": {"tr": "Kurumsal Yönetim Yapısı", "en": "Corporate Governance Structure"},
    "danis.aileden.val1.desc": {"tr": "Net organizasyon yapısı ve yönetim modeli", "en": "Clear organizational structure and management model"},
    "danis.aileden.val2.title": {"tr": "Rol ve Sorumluluklar", "en": "Roles and Responsibilities"},
    "danis.aileden.val2.desc": {"tr": "Görev tanımları ve yetki matrisi", "en": "Job descriptions and authority matrix"},
    "danis.aileden.val3.title": {"tr": "Karar Alma Süreçleri", "en": "Decision-Making Processes"},
    "danis.aileden.val3.desc": {"tr": "Şeffaf ve tanımlı karar mekanizmaları", "en": "Transparent and defined decision mechanisms"},
    "danis.aileden.val4.title": {"tr": "Profesyonel Yönetim", "en": "Professional Management"},
    "danis.aileden.val4.desc": {"tr": "Aile ve profesyonel yönetim dengesi", "en": "Balance between family and professional management"},
    "danis.aileden.quote": {"tr": "Kurumsallaşmak, kurucunun vazgeçmesi değil; kurucunun mirasını koruyacak bir sistem kurmasıdır.", "en": "Institutionalization is not about the founder stepping aside — it is about building a system that preserves the founder's legacy."},
    "danis.aileden.target1": {"tr": "Büyüyen Aile Şirketleri", "en": "Growing Family Businesses"},
    "danis.aileden.target2": {"tr": "İkinci veya Üçüncü Nesle Geçiş Yapan Organizasyonlar", "en": "Organizations Transitioning to the Second or Third Generation"},
    "danis.aileden.target3": {"tr": "Kurumsallaşma İhtiyacı Duyan Şirketler", "en": "Companies in Need of Institutionalization"},
    "danis.aileden.cta.title": {"tr": "Kurumunuz için özel çözüm tasarlayalım", "en": "Let's Design a Custom Solution for Your Institution"},
    "danis.aileden.cta.desc": {"tr": "Her kurum farklıdır. Size özel yaklaşım, metodoloji ve uygulama planıyla yanınızdayız.", "en": "Every institution is different. We are with you every step of the way with a custom approach, methodology and implementation plan."},

    # ═══════════════════ BLOG SUBPAGES ═══════════════════
    "blog.yz.category": {"tr": "🤖 YZ & İK", "en": "🤖 AI & HR"},
    "blog.yz.date": {"tr": "Mayıs 2025", "en": "May 2025"},
    "blog.yz.read": {"tr": "6 dk okuma", "en": "6 min read"},
    "blog.yz.title": {"tr": "Yapay Zekâ İşe Alımı Nasıl Değiştiriyor?", "en": "How Is Artificial Intelligence Transforming Recruitment?"},
    "blog.yz.lead": {"tr": "CV taramasından yetkinlik değerlendirmesine, mülakat analizinden onboarding kişiselleştirmesine kadar yapay zekanın işe alım sürecine etkisi ve dikkat edilmesi gereken kritik tuzaklar.", "en": "From CV screening to competency assessment, from interview analysis to onboarding personalization — the impact of AI on recruitment and the critical pitfalls to watch out for."},
    "blog.aile.category": {"tr": "🏛️ Kurumsal", "en": "🏛️ Corporate"},
    "blog.aile.date": {"tr": "Mart 2025", "en": "March 2025"},
    "blog.aile.read": {"tr": "9 dk okuma", "en": "9 min read"},
    "blog.aile.title": {"tr": "Aile Şirketlerinde Kurumsallaşma: Neden Bu Kadar Zor?", "en": "Institutionalization in Family Businesses: Why Is It So Hard?"},
    "blog.aile.lead": {"tr": "Kurumsallaşma, aile şirketleri için bir lüks değil, sürdürülebilir büyümenin ön koşuludur. Ancak neden bu kadar çok aile şirketi bu süreçte başarısız oluyor?", "en": "Institutionalization is not a luxury for family businesses, but a prerequisite for sustainable growth. But why do so many family businesses fail in this process?"},
    "blog.geri.category": {"tr": "🎯 Liderlik", "en": "🎯 Leadership"},
    "blog.geri.date": {"tr": "Haziran 2025", "en": "June 2025"},
    "blog.geri.read": {"tr": "7 dk okuma", "en": "7 min read"},
    "blog.geri.title": {"tr": "Geri Bildirim Kültürü Nasıl Kurulur?", "en": "How to Build a Feedback Culture"},
    "blog.geri.lead": {"tr": "Kurumda gerçek bir geri bildirim kültürü kurmak yalnızca anket göndermekten ibaret değil; psikolojik güvenlik, lider tutarlılığı ve ritüellerle örülmüş bir sistem gerektiriyor.", "en": "Building a real feedback culture in an organization is not just about sending surveys; it requires a system woven with psychological safety, leader consistency and rituals."},
    "blog.isguc.category": {"tr": "🧬 Stratejik İK", "en": "🧬 Strategic HR"},
    "blog.isguc.date": {"tr": "Şubat 2025", "en": "February 2025"},
    "blog.isguc.read": {"tr": "7 dk okuma", "en": "7 min read"},
    "blog.isguc.title": {"tr": "2026 İçin İşgücü Planlaması", "en": "Workforce Planning for 2026"},
    "blog.isguc.lead": {"tr": "Demografik dalgalanmalar, teknoloji yetkinlik boşlukları ve belirsiz ekonomik tablo — işgücü planlamasını stratejik bir zorunluluk haline getiriyor.", "en": "Demographic fluctuations, technology skill gaps and uncertain economic conditions — making workforce planning a strategic imperative."},
    "blog.perf.category": {"tr": "📈 Performans", "en": "📈 Performance"},
    "blog.perf.date": {"tr": "Nisan 2025", "en": "April 2025"},
    "blog.perf.read": {"tr": "8 dk okuma", "en": "8 min read"},
    "blog.perf.title": {"tr": "Performans Yönetiminde En Sık Yapılan 5 Hata", "en": "The 5 Most Common Mistakes in Performance Management"},
    "blog.perf.lead": {"tr": "Yıllık değerlendirme döngüsünden hedef belirsizliğine, önyargılardan gelişim planı eksikliğine kadar kurumların tekrarladığı performans hataları ve çözüm önerileri.", "en": "Performance mistakes institutions keep repeating, from annual evaluation fixation to goal ambiguity, from biases to lack of development plans, and solution recommendations."},
}


def generate_json_files():
    """Generate comprehensive tr.json and en.json"""
    tr_dict = {}
    en_dict = {}
    for key, val in translations.items():
        tr_dict[key] = val["tr"]
        en_dict[key] = val["en"]

    # Write tr.json
    tr_path = os.path.join(BASE_DIR, "locales", "tr.json")
    with open(tr_path, "w", encoding="utf-8") as f:
        json.dump(tr_dict, f, ensure_ascii=False, indent=2)
    print(f"✓ Generated {tr_path} ({len(tr_dict)} keys)")

    # Write en.json
    en_path = os.path.join(BASE_DIR, "locales", "en.json")
    with open(en_path, "w", encoding="utf-8") as f:
        json.dump(en_dict, f, ensure_ascii=False, indent=2)
    print(f"✓ Generated {en_path} ({len(en_dict)} keys)")

    return tr_dict, en_dict


def add_data_i18n_to_files():
    """Add data-i18n attributes to all HTML files"""
    html_files = []
    for pattern in ["*.html", "egitimler/*.html", "danismanliklar/*.html", "blog/*.html"]:
        html_files.extend(glob.glob(os.path.join(BASE_DIR, pattern)))

    print(f"\n🔍 Processing {len(html_files)} HTML files...")

    # ═══════════════════════════════════════════════════════
    # SHARED REPLACEMENTS (apply to ALL files)
    # ═══════════════════════════════════════════════════════
    # These handle elements that appear in every page's nav, footer, and modal

    shared_replacements = []

    # --- NAV LINKS (desktop) ---
    # For root pages (href without ../)
    nav_links_root = [
        (r'<a href="kurslar.html"(?![^>]*data-i18n)>Eğitimlerimiz</a>', '<a data-i18n="nav.egitimler" href="kurslar.html">Eğitimlerimiz</a>'),
        (r'<a href="kurslar.html"(?![^>]*data-i18n)>Egitimlerimiz</a>', '<a data-i18n="nav.egitimler" href="kurslar.html">Eğitimlerimiz</a>'),
        (r'<a class="active" href="kurslar.html"(?![^>]*data-i18n)>Eğitimlerimiz</a>', '<a class="active" data-i18n="nav.egitimler" href="kurslar.html">Eğitimlerimiz</a>'),
        (r'<a href="danismanlik.html"(?![^>]*data-i18n)>Danışmanlıklarımız</a>', '<a data-i18n="nav.danismanlik" href="danismanlik.html">Danışmanlıklarımız</a>'),
        (r'<a href="danismanlik.html"(?![^>]*data-i18n)>Danismanliklarimiz</a>', '<a data-i18n="nav.danismanlik" href="danismanlik.html">Danışmanlıklarımız</a>'),
        (r'<a class="active" href="danismanlik.html"(?![^>]*data-i18n)>Danışmanlıklarımız</a>', '<a class="active" data-i18n="nav.danismanlik" href="danismanlik.html">Danışmanlıklarımız</a>'),
        (r'<a href="hakkimizda.html"(?![^>]*data-i18n)>Kurumsal</a>', '<a data-i18n="nav.hakkimizda" href="hakkimizda.html">Kurumsal</a>'),
        (r'<a href="hakkimizda.html"(?![^>]*data-i18n)>Hakkımızda</a>', '<a data-i18n="nav.hakkimizda" href="hakkimizda.html">Kurumsal</a>'),
        (r'<a class="active" href="hakkimizda.html"(?![^>]*data-i18n)>Kurumsal</a>', '<a class="active" data-i18n="nav.hakkimizda" href="hakkimizda.html">Kurumsal</a>'),
        (r'<a href="referanslar.html"(?![^>]*data-i18n)>Referanslarımız</a>', '<a data-i18n="nav.referanslar" href="referanslar.html">Referanslarımız</a>'),
        (r'<a class="active" href="referanslar.html"(?![^>]*data-i18n)>Referanslarımız</a>', '<a class="active" data-i18n="nav.referanslar" href="referanslar.html">Referanslarımız</a>'),
        (r'<a href="blog.html"(?![^>]*data-i18n)>Deneyimlerimiz</a>', '<a data-i18n="nav.blog" href="blog.html">Deneyimlerimiz</a>'),
        (r'<a href="blog.html"(?![^>]*data-i18n)>Blog</a>', '<a data-i18n="nav.blog" href="blog.html">Deneyimlerimiz</a>'),
        (r'<a class="active" href="blog.html"(?![^>]*data-i18n)>Deneyimlerimiz</a>', '<a class="active" data-i18n="nav.blog" href="blog.html">Deneyimlerimiz</a>'),
        (r'<a class="active" href="blog.html"(?![^>]*data-i18n)>Blog</a>', '<a class="active" data-i18n="nav.blog" href="blog.html">Deneyimlerimiz</a>'),
        (r'<a href="iletisim.html"(?![^>]*data-i18n)>İletişim</a>', '<a data-i18n="nav.iletisim" href="iletisim.html">İletişim</a>'),
        (r'<a href="iletisim.html"(?![^>]*data-i18n)>Iletisim</a>', '<a data-i18n="nav.iletisim" href="iletisim.html">İletişim</a>'),
        (r'<a class="active" href="iletisim.html"(?![^>]*data-i18n)>İletişim</a>', '<a class="active" data-i18n="nav.iletisim" href="iletisim.html">İletişim</a>'),
    ]

    # For subpages (href with ../)
    nav_links_sub = [
        (r'<a href="\.\./kurslar.html"(?![^>]*data-i18n)>Eğitimlerimiz</a>', '<a data-i18n="nav.egitimler" href="../kurslar.html">Eğitimlerimiz</a>'),
        (r'<a href="\.\./danismanlik.html"(?![^>]*data-i18n)>Danışmanlıklarımız</a>', '<a data-i18n="nav.danismanlik" href="../danismanlik.html">Danışmanlıklarımız</a>'),
        (r'<a href="\.\./hakkimizda.html"(?![^>]*data-i18n)>Kurumsal</a>', '<a data-i18n="nav.hakkimizda" href="../hakkimizda.html">Kurumsal</a>'),
        (r'<a href="\.\./hakkimizda.html"(?![^>]*data-i18n)>Hakkımızda</a>', '<a data-i18n="nav.hakkimizda" href="../hakkimizda.html">Kurumsal</a>'),
        (r'<a href="\.\./referanslar.html"(?![^>]*data-i18n)>Referanslarımız</a>', '<a data-i18n="nav.referanslar" href="../referanslar.html">Referanslarımız</a>'),
        (r'<a href="\.\./blog.html"(?![^>]*data-i18n)>Deneyimlerimiz</a>', '<a data-i18n="nav.blog" href="../blog.html">Deneyimlerimiz</a>'),
        (r'<a href="\.\./blog.html"(?![^>]*data-i18n)>Blog</a>', '<a data-i18n="nav.blog" href="../blog.html">Deneyimlerimiz</a>'),
        (r'<a class="active" href="\.\./blog.html"(?![^>]*data-i18n)>Deneyimlerimiz</a>', '<a class="active" data-i18n="nav.blog" href="../blog.html">Deneyimlerimiz</a>'),
        (r'<a class="active" href="\.\./blog.html"(?![^>]*data-i18n)>Blog</a>', '<a class="active" data-i18n="nav.blog" href="../blog.html">Deneyimlerimiz</a>'),
        (r'<a href="\.\./iletisim.html"(?![^>]*data-i18n)>İletişim</a>', '<a data-i18n="nav.iletisim" href="../iletisim.html">İletişim</a>'),
        (r'<a href="\.\./iletisim.html"(?![^>]*data-i18n)>Iletisim</a>', '<a data-i18n="nav.iletisim" href="../iletisim.html">İletişim</a>'),
    ]

    # --- MOBILE NAV ---
    mobile_nav_root = [
        (r'<a href="index.html"(?![^>]*data-i18n)>Ana Sayfa</a>', '<a data-i18n="nav.anasayfa" href="index.html">Ana Sayfa</a>'),
    ]
    mobile_nav_sub = [
        (r'<a href="\.\./index.html"(?![^>]*data-i18n)>Ana Sayfa</a>', '<a data-i18n="nav.anasayfa" href="../index.html">Ana Sayfa</a>'),
    ]

    # --- TEKLIF BUTTON (nav) ---
    teklif_btn = [
        (r'onclick="openTeklifModal\(\)"(?![^>]*data-i18n)>Özel Teklif Al</button>', 'onclick="openTeklifModal()" data-i18n="nav.teklif">Özel Teklif Al</button>'),
        (r'onclick="openTeklifModal\(\)"(?![^>]*data-i18n)>Ozel Teklif Al</button>', 'onclick="openTeklifModal()" data-i18n="nav.teklif">Özel Teklif Al</button>'),
    ]

    # --- FOOTER ---
    footer_replacements = [
        # Brand desc
        (r'class="brand-desc"(?![^>]*data-i18n)>İnsan kaynakları', 'class="brand-desc" data-i18n="shared.footer.brandesc">İnsan kaynakları'),
        (r'class="brand-desc"(?![^>]*data-i18n)>Insan kaynaklari', 'class="brand-desc" data-i18n="shared.footer.brandesc">İnsan kaynakları'),
        # Footer col titles
        (r'class="footer-col-title"(?![^>]*data-i18n)>Hizmetler</div>', 'class="footer-col-title" data-i18n="shared.footer.hizmetler">Hizmetler</div>'),
        (r'class="footer-col-title"(?![^>]*data-i18n)>Şirket</div>', 'class="footer-col-title" data-i18n="shared.footer.sirket">Şirket</div>'),
        (r'class="footer-col-title"(?![^>]*data-i18n)>Sirket</div>', 'class="footer-col-title" data-i18n="shared.footer.sirket">Şirket</div>'),
        (r'class="footer-col-title"(?![^>]*data-i18n)>Bülten</div>', 'class="footer-col-title" data-i18n="shared.footer.bulten">Bülten</div>'),
        (r'class="footer-col-title"(?![^>]*data-i18n)>Bulten</div>', 'class="footer-col-title" data-i18n="shared.footer.bulten">Bülten</div>'),
        (r'class="footer-col-title"(?![^>]*data-i18n)>İletişim</div>', 'class="footer-col-title" data-i18n="shared.footer.iletisim">İletişim</div>'),
        (r'class="footer-col-title"(?![^>]*data-i18n)>Iletisim</div>', 'class="footer-col-title" data-i18n="shared.footer.iletisim">İletişim</div>'),
        # Copyright
        (r'class="footer-copy"(?![^>]*data-i18n)>©', 'class="footer-copy" data-i18n="shared.footer.copy">©'),
        # Legal links
        (r'>Gizlilik Politikası</a>', ' data-i18n="shared.footer.gizlilik">Gizlilik Politikası</a>'),
        (r'>Gizlilik</a>', ' data-i18n="shared.footer.gizlilik">Gizlilik Politikası</a>'),
        (r'>Kullanım Koşulları</a>', ' data-i18n="shared.footer.kullanim">Kullanım Koşulları</a>'),
        (r'>KVKK</a>', ' data-i18n="shared.footer.kvkk">KVKK</a>'),
        (r'>Çerezler</a>', ' data-i18n="shared.footer.cerezler">Çerezler</a>'),
        (r'>Cerezler</a>', ' data-i18n="shared.footer.cerezler">Çerezler</a>'),
    ]

    # --- MODAL ---
    modal_replacements = [
        # Modal labels and titles (using careful patterns to avoid false positives)
        (r'>İletişim Bilgileri</div>', ' data-i18n="shared.modal.contact">İletişim Bilgileri</div>'),
        (r'>Iletisim Bilgileri</div>', ' data-i18n="shared.modal.contact">İletişim Bilgileri</div>'),
    ]

    # --- BACK TO TOP ---
    backtotop = [
        (r'aria-label="Yukarı dön"', 'aria-label="Yukarı dön" data-i18n="shared.backtotop"'),
        (r'aria-label="Yukari don"', 'aria-label="Yukarı dön" data-i18n="shared.backtotop"'),
    ]

    all_shared = nav_links_root + nav_links_sub + mobile_nav_root + mobile_nav_sub + teklif_btn + footer_replacements + modal_replacements + backtotop

    total_changes = 0
    for filepath in html_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        original = content
        changes = 0

        # Apply shared replacements
        for pattern, replacement in all_shared:
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                count = len(re.findall(pattern, content))
                changes += count
                content = new_content

        # Remove double data-i18n (safety)
        content = re.sub(r'data-i18n="[^"]*"\s+data-i18n="', 'data-i18n="', content)

        if content != original:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            rel_path = os.path.relpath(filepath, BASE_DIR)
            print(f"  ✓ {rel_path} ({changes} changes)")
            total_changes += changes

    print(f"\n📊 Total: {total_changes} data-i18n attributes added across {len(html_files)} files")


def fix_turkish_characters():
    """Fix missing Turkish characters in blog.html and other files"""
    blog_path = os.path.join(BASE_DIR, "blog.html")
    if not os.path.exists(blog_path):
        return

    with open(blog_path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # Fix all ASCII Turkish to proper Turkish in blog.html
    char_fixes = {
        "Egitimlerimiz": "Eğitimlerimiz",
        "Danismanliklarimiz": "Danışmanlıklarımız",
        "Iletisim": "İletişim",
        "Ozel Teklif Al": "Özel Teklif Al",
        "One Cikan": "Öne Çıkan",
        "Deneyimlerimiz": "Deneyimlerimiz",  # already correct
        "Geri Bildirim Kulturu Nasil Insa Edilir?": "Geri Bildirim Kültürü Nasıl İnşa Edilir?",
        "Kurumda gercek bir geri bildirim kulturu kurmak yalnizca anket gondermekten ibaret degil": "Kurumda gerçek bir geri bildirim kültürü kurmak yalnızca anket göndermekten ibaret değil",
        "Yaziyi Oku": "Yazıyı Oku",
        "Yapay Zeka Ise Alimi Nasil Degistiriyor?": "Yapay Zekâ İşe Alımı Nasıl Değiştiriyor?",
        "CV taramasindan yetkinlik degerlendirmesine kadar yapay zekanin IK sureclerine etkisi": "CV taramasından yetkinlik değerlendirmesine kadar yapay zekanın İK süreçlerine etkisi",
        "Mayis 2025": "Mayıs 2025",
        "Oku →": "Oku →",
        "Performans Yonetiminde Yapilan 5 Kritik Hata": "Performans Yönetiminde Yapılan 5 Kritik Hata",
        "Yillik degerlendirme dongusunden hedef belirsizligine kadar kurumlarin tekrarladi": "Yıllık değerlendirme döngüsünden hedef belirsizliğine kadar kurumların tekrarladı",
        "Nisan 2025": "Nisan 2025",
        "Aile Sirketi Kurumsalasirken Neden Basarisiz Olur?": "Aile Şirketi Kurumsallaşırken Neden Başarısız Olur?",
        "Aile sirketinin kurumsal bir yapiya gecis surecinde karsilastigi en yaygin tuzaklar": "Aile şirketinin kurumsal bir yapıya geçiş sürecinde karşılaştığı en yaygın tuzaklar",
        "Mart 2025": "Mart 2025",
        "Isgucku Planlamasi 2026: Neden Simdi Baslamalisiniz?": "İşgücü Planlaması 2026: Neden Şimdi Başlamalısınız?",
        "Demografik dalgalanmalar, teknoloji yetkinlik boslukları ve belirsiz ekonomik tabloda proaktif kadro planlamasinin onemi": "Demografik dalgalanmalar, teknoloji yetkinlik boşlukları ve belirsiz ekonomik tabloda proaktif kadro planlamasının önemi",
        "Subat 2025": "Şubat 2025",
        "Video Icerikleri": "Video İçerikleri",
        "Yukleme bekleniyor": "Yükleme bekleniyor",
        "Bultene Abone Ol": "Bültene Abone Ol",
        "IK gundemindeki gelismeler ve yeni yazilarimiz icin haftada bir e-posta": "İK gündemindeki gelişmeler ve yeni yazılarımız için haftada bir e-posta",
        "Abone Ol": "Abone Ol",
        "Populer Yazilar": "Popüler Yazılar",
        "Geri Bildirim Kulturu Nasil Insa Edilir?": "Geri Bildirim Kültürü Nasıl İnşa Edilir?",
        "Performansta 5 Kritik Hata": "Performansta 5 Kritik Hata",
        "Aile Sirketi Kurumsallasmasindan Basarisizlik": "Aile Şirketi Kurumsallaşmasından Başarısızlık",
        "YZ ve Ise Alim": "YZ ve İşe Alım",
        "Isgucku Planlamasi 2026": "İşgücü Planlaması 2026",
        "Etiketler": "Etiketler",
        "Liderlik": "Liderlik",
        "Ise Alim": "İşe Alım",
        "Performans": "Performans",
        "Yetenek": "Yetenek",
        "Kurumsallasma": "Kurumsallaşma",
        "Yapay Zeka": "Yapay Zekâ",
        "Geri Bildirim": "Geri Bildirim",
        "Kocluk": "Koçluk",
        "Ucret": "Ücret",
        "Kurumunuza Ozel Danismanlik": "Kurumunuza Özel Danışmanlık",
        "IK sureclerinizi stratejik bir rekabet avantajina donusturmek icin konusalim": "İK süreçlerinizi stratejik bir rekabet avantajına dönüştürmek için konuşalım",
        "Teklif Al →": "Teklif Al →",
        "Insan kaynaklari alaninda uzmanlasmis danismanlik ve egitim sirketi": "İnsan kaynakları alanında uzmanlaşmış danışmanlık ve eğitim şirketi",
        "Hizmetler": "Hizmetler",
        "Sirket": "Şirket",
        "Bulten": "Bülten",
        "IK gundeminden haberdar ol": "İK gündeminden haberdar ol",
        "Tum haklari saklidir": "Tüm hakları saklıdır",
        "Gizlilik": "Gizlilik",
        "Cerezler": "Çerezler",
        "Yukari don": "Yukarı dön",
        "Iletisim Bilgileri": "İletişim Bilgileri",
        "Hemen Teklif Alin": "Hemen Teklif Alın",
        "Egitim ihtiyaclarinizi paylasin": "Eğitim ihtiyaçlarınızı paylaşın",
        "Ad Soyad *": "Ad Soyad *",
        "E-posta *": "E-posta *",
        "Telefon *": "Telefon *",
        "Talebiniz *": "Talebiniz *",
        "Teklif Iste →": "Teklif İste →",
        "Talebiniz iletildi!": "Talebiniz iletildi!",
        "Abone oldunuz!": "Abone oldunuz!",
        "Ana Sayfa": "Ana Sayfa",
        "Tumu": "Tümü",
        "Stratejik IK": "Stratejik İK",
        "YZ & IK": "YZ & İK",
        "Haziran 2025": "Haziran 2025",
        "7 dk okuma": "7 dk okuma",
        "IK ve Liderlik Uzerine Derin Dusunceler": "İK ve Liderlik Üzerine Derin Düşünceler",
        "Sahadan gelen gozlemler": "Sahadan gelen gözlemler",
    }

    for ascii_text, proper_text in char_fixes.items():
        content = content.replace(ascii_text, proper_text)

    if content != original:
        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✓ Fixed Turkish characters in blog.html")
    else:
        print("ℹ blog.html — no character fixes needed")


def normalize_nav_text():
    """Normalize nav text across all pages to use consistent labels"""
    html_files = []
    for pattern in ["*.html", "egitimler/*.html", "danismanliklar/*.html", "blog/*.html"]:
        html_files.extend(glob.glob(os.path.join(BASE_DIR, pattern)))

    fixes = 0
    for filepath in html_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        original = content

        # Normalize "Hakkımızda" to "Kurumsal" in nav
        content = re.sub(
            r'(data-i18n="nav\.hakkimizda"[^>]*>)Hakkımızda(</a>)',
            r'\1Kurumsal\2',
            content
        )
        # Normalize "Blog" to "Deneyimlerimiz" in nav
        content = re.sub(
            r'(data-i18n="nav\.blog"[^>]*>)Blog(</a>)',
            r'\1Deneyimlerimiz\2',
            content
        )

        if content != original:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            fixes += 1

    print(f"✓ Normalized nav text in {fixes} files")


def ensure_lang_toggle():
    """Ensure language toggle button exists in all pages"""
    html_files = []
    for pattern in ["*.html", "egitimler/*.html", "danismanliklar/*.html", "blog/*.html"]:
        html_files.extend(glob.glob(os.path.join(BASE_DIR, pattern)))

    added = 0
    for filepath in html_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if 'id="langToggle"' not in content:
            # Add lang toggle before the teklif button in nav-actions
            lang_btn = '<button id="langToggle" onclick="daToggleLang()" class="btn btn-ghost btn-sm" style="font-weight:700;letter-spacing:1px;padding:7px 14px;min-width:52px;">EN</button>'

            # Try to add before the first nav button
            if 'class="nav-actions"' in content:
                content = content.replace(
                    'class="nav-actions"><button',
                    f'class="nav-actions">{lang_btn}<button'
                )
            elif 'class="nav-actions">' in content:
                content = content.replace(
                    'class="nav-actions">',
                    f'class="nav-actions">{lang_btn}'
                )

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            added += 1

    print(f"✓ Added language toggle to {added} files")


def ensure_i18n_script():
    """Ensure i18n.js is loaded in all HTML files"""
    html_files = []
    for pattern in ["*.html", "egitimler/*.html", "danismanliklar/*.html", "blog/*.html"]:
        html_files.extend(glob.glob(os.path.join(BASE_DIR, pattern)))

    added = 0
    for filepath in html_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if "i18n.js" not in content:
            # Determine correct path
            rel_path = os.path.relpath(filepath, BASE_DIR)
            if "/" in rel_path:
                script_tag = '<script src="../js/i18n.js"></script>'
            else:
                script_tag = '<script src="js/i18n.js"></script>'

            # Add before main.js or before closing body
            if "main.js" in content:
                main_js_pattern = r'<script src="[^"]*main\.js"><\/script>'
                match = re.search(main_js_pattern, content)
                if match:
                    content = content[:match.start()] + script_tag + "\n" + content[match.start():]
            elif "</body>" in content:
                content = content.replace("</body>", f"{script_tag}\n</body>")

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            added += 1

    print(f"✓ Added i18n.js to {added} files")


if __name__ == "__main__":
    print("═" * 60)
    print("  DERIN AKADEMİ — i18n Processing Script")
    print("═" * 60)

    print("\n📝 Step 1: Generating JSON files...")
    generate_json_files()

    print("\n📝 Step 2: Fixing Turkish characters...")
    fix_turkish_characters()

    print("\n📝 Step 3: Ensuring i18n.js is loaded...")
    ensure_i18n_script()

    print("\n📝 Step 4: Ensuring language toggle exists...")
    ensure_lang_toggle()

    print("\n📝 Step 5: Adding data-i18n attributes...")
    add_data_i18n_to_files()

    print("\n📝 Step 6: Normalizing nav text...")
    normalize_nav_text()

    print("\n✅ Done! i18n processing complete.")
    print("═" * 60)
