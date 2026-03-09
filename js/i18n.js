/* ═══════════════════════════════════════════════════
   Derin Akademi — TR / EN Language System
   Usage: daToggleLang() called from lang button
   Stores preference in localStorage as 'da-lang'
═══════════════════════════════════════════════════ */

const DA_TRANSLATIONS = {
  // ── NAV ────────────────────────────────────────
  'nav.egitimler':          { tr: 'Eğitimlerimiz',       en: 'Training Programs' },
  'nav.danismanlik':        { tr: 'Danışmanlıklarımız',  en: 'Consulting' },
  'nav.hakkimizda':         { tr: 'Hakkımızda',          en: 'About Us' },
  'nav.blog':               { tr: 'Blog',                en: 'Blog' },
  'nav.iletisim':           { tr: 'İletişim',            en: 'Contact' },
  'nav.teklif':             { tr: 'Özel Teklif Al',      en: 'Get a Quote' },

  // ── SECTORS DOCK ───────────────────────────────
  'sector.finans':          { tr: 'Finans',       en: 'Finance' },
  'sector.uretim':          { tr: 'Üretim',       en: 'Manufacturing' },
  'sector.sanayi':          { tr: 'Sanayi',       en: 'Industry' },
  'sector.tarim':           { tr: 'Tarım',        en: 'Agriculture' },
  'sector.saglik':          { tr: 'Sağlık',       en: 'Healthcare' },
  'sector.perakende':       { tr: 'Perakende',    en: 'Retail' },
  'sector.egitim':          { tr: 'Eğitim',       en: 'Education' },
  'sector.holding':         { tr: 'Holding',      en: 'Holding' },
  'sector.insaat':          { tr: 'İnşaat',       en: 'Construction' },

  // ── HERO ───────────────────────────────────────
  'hero.tag':               { tr: 'İnsan Kaynakları Danışmanlığı',  en: 'Human Resources Consulting' },
  'hero.title1':            { tr: 'Kurumunuzu',           en: 'Transform' },
  'hero.title2':            { tr: 'Dönüştürüyoruz',       en: 'Your Organization' },
  'hero.desc':              { tr: 'Stratejik İK yönetimi, liderlik gelişimi ve kurumsallaşma danışmanlığıyla kurumunuzun gerçek potansiyelini ortaya çıkarıyoruz.', en: 'We unlock your organization\'s true potential through strategic HR management, leadership development and institutionalization consulting.' },
  'hero.cta1':              { tr: 'Danışmanlık Süreçleri', en: 'Consulting Services' },
  'hero.cta2':              { tr: 'Eğitim Programları',   en: 'Training Programs' },

  // ── STATS ──────────────────────────────────────
  'stat.kurum':             { tr: 'Hizmet Verilen Kurum', en: 'Institutions Served' },
  'stat.tecrube':           { tr: 'Yıllık Tecrübe',       en: 'Years of Experience' },
  'stat.egitim':            { tr: 'Eğitim Programı',      en: 'Training Programs' },
  'stat.sektor':            { tr: 'Farklı Sektör',         en: 'Different Sectors' },

  // ── FEATURES ───────────────────────────────────
  'feat.tag':               { tr: 'Neden Derin Akademi?',  en: 'Why Derin Akademi?' },
  'feat.title':             { tr: 'Biz Eğitim Satmıyoruz', en: 'We Don\'t Just Teach' },
  'feat.desc':              { tr: 'Kurumla birlikte dönüşümün sorumluluğunu alıyoruz. Anlatan değil, çalışan sistemler kurarız.', en: 'We take ownership of transformation alongside the institution. We build systems that work, not just teach.' },
  'feat.01.title':          { tr: 'Sahadaki Uygulama Deneyimi', en: 'Real-World Application' },
  'feat.01.desc':           { tr: 'Akademik bilgiyi gerçek iş yaşamından beslenen içgörülerle buluşturarak, klasik kalıpların ötesinde uygulanabilir ve sürdürülebilir çözümler sunuyoruz.', en: 'We combine academic knowledge with real business insights to deliver practical, sustainable solutions beyond conventional models.' },
  'feat.02.title':          { tr: 'Kuruma Özel Tasarım',    en: 'Custom-Built Design' },
  'feat.02.desc':           { tr: 'Çözümler hazır modellerle değil; kurumun hedefleri, kültürü ve mevcut olgunluk seviyesi dikkate alınarak özel olarak tasarlanır.', en: 'Solutions are not off-the-shelf; they are designed specifically around the institution\'s goals, culture and maturity level.' },
  'feat.03.title':          { tr: 'Davranış Dönüşümü',      en: 'Behavioral Transformation' },
  'feat.03.desc':           { tr: 'Yalnızca bilgi aktarmıyoruz; yönetme, karar alma ve iletişim biçimlerini köklü biçimde dönüştürmeyi hedefliyoruz.', en: 'We don\'t just transfer knowledge; we aim to fundamentally transform management, decision-making and communication styles.' },
  'feat.04.title':          { tr: 'YZ Destekli Öğrenme',    en: 'AI-Powered Learning' },
  'feat.04.desc':           { tr: 'Yapay zekâ destekli, kuruma özel içerikler ve 7/24 erişilebilir dijital avatar desteği ile sürekli öğrenme imkânı.', en: 'AI-powered, institution-specific content and 24/7 accessible digital avatar support for continuous learning.' },
  'feat.05.title':          { tr: 'Esnek Eğitim Formatları', en: 'Flexible Training Formats' },
  'feat.05.desc':           { tr: 'Yüz yüze sınıf eğitimlerinden online interaktif programlara kadar kurumunuzun ihtiyacına en uygun formatta.', en: 'From in-person classroom training to online interactive programs — the format that fits your institution best.' },
  'feat.06.title':          { tr: 'Stratejik Ortaklık',      en: 'Strategic Partnership' },
  'feat.06.desc':           { tr: '"Ne yapılmalı?" değil, "nasıl yapılacak?" sorusunun sorumluluğunu alıyoruz. Dönüşümü birlikte yönetiyoruz.', en: 'We take responsibility not for "what should be done" but "how it will be done." We manage the transformation together.' },

  // ── SECTORS SECTION ────────────────────────────
  'sectors.tag':            { tr: 'Çalıştığımız Sektörler', en: 'Sectors We Serve' },
  'sectors.title':          { tr: 'Farklı Sektörlerde',     en: 'Shared Transformation' },
  'sectors.title2':         { tr: 'Ortak Dönüşüm',         en: 'Across Different Sectors' },
  'sectors.desc':           { tr: 'Finans\'tan tarıma, sağlıktan perakendeye — 40\'tan fazla kurum ile dönüşümün sorumluluğunu birlikte taşıdık.', en: 'From finance to agriculture, healthcare to retail — we have carried the responsibility of transformation with more than 40 institutions.' },

  // ── TRAINING ───────────────────────────────────
  'train.tag':              { tr: 'Eğitimlerimiz',           en: 'Training Programs' },
  'train.title':            { tr: 'Davranış ve Karar Biçimi Dönüşümü', en: 'Behavioral & Decision-Making Transformation' },
  'train.desc':             { tr: 'Liderlikten veriye, performanstan aidiyete — kurumunuzun ihtiyacına özel eğitim programları.', en: 'From leadership to data, from performance to belonging — tailored training programs for your institution.' },
  'train.tümü':             { tr: 'Tümü',         en: 'All' },
  'train.liderlik':         { tr: 'Liderlik',     en: 'Leadership' },
  'train.ik':               { tr: 'İK Sistemleri', en: 'HR Systems' },
  'train.gelisim':          { tr: 'Gelişim',      en: 'Development' },
  'train.cta':              { tr: 'Tüm Programları Gör', en: 'View All Programs' },

  // ── CONSULTING ─────────────────────────────────
  'cons.tag':               { tr: 'Danışmanlık Hizmetleri', en: 'Consulting Services' },
  'cons.title':             { tr: 'Sistematik Çözümler',    en: 'Systematic Solutions' },
  'cons.desc':              { tr: 'Stratejik İK\'dan kurumsallaşmaya, ücret yönetiminden yetenek sistemlerine — her alana özel danışmanlık.', en: 'From strategic HR to institutionalization, from compensation to talent systems — specialized consulting for every area.' },

  // ── FOUNDER ────────────────────────────────────
  'founder.tag':            { tr: 'Kurucumuz',              en: 'Our Founder' },
  'founder.role':           { tr: 'İK Stratejisti · ACC Koç · Kurumsallaşma Danışmanı ve Eğitmeni', en: 'HR Strategist · ACC Coach · Institutionalization Consultant & Trainer' },

  // ── TESTIMONIALS ───────────────────────────────
  'testi.tag':              { tr: 'Başarı Hikayeleri',       en: 'Success Stories' },
  'testi.title':            { tr: 'Gerçek Sonuçlar,',        en: 'Real Results,' },
  'testi.title2':           { tr: 'Gerçek Kurumlar',         en: 'Real Institutions' },

  // ── CTA ────────────────────────────────────────
  'cta.teklif':             { tr: 'Özel Teklif Al',          en: 'Get a Quote' },
  'cta.whatsapp':           { tr: 'WhatsApp\'tan Ulaş',      en: 'Contact via WhatsApp' },

  // ── FOOTER ─────────────────────────────────────
  'footer.desc':            { tr: 'İnsan kaynakları alanında uzmanlaşmış danışmanlık ve eğitim şirketi. Anlatan değil, çalışan sistemler kurarız.', en: 'A consulting and training company specializing in human resources. We build systems that work, not just talk.' },
  'footer.links':           { tr: 'Hızlı Linkler',           en: 'Quick Links' },
  'footer.hizmetler':       { tr: 'Hizmetler',               en: 'Services' },
  'footer.iletisim':        { tr: 'İletişim',                en: 'Contact' },
  'footer.rights':          { tr: 'Tüm hakları saklıdır.',   en: 'All rights reserved.' },

  // ── KURSLAR PAGE ───────────────────────────────
  'kurslar.hero.tag':       { tr: 'Eğitim Programları',       en: 'Training Programs' },
  'kurslar.hero.title':     { tr: 'Eğitimlerimiz',            en: 'Our Training' },
  'kurslar.hero.desc':      { tr: 'Davranış ve karar biçimi dönüşümü için tasarlanmış kurumsal eğitim programları. Her program kurumunuza özel uyarlanır.', en: 'Corporate training programs designed for behavioral and decision-making transformation. Every program is tailored to your institution.' },

  // ── DANISMANLIK PAGE ───────────────────────────
  'danis.hero.tag':         { tr: 'Danışmanlık Hizmetleri',   en: 'Consulting Services' },
  'danis.hero.title':       { tr: 'Danışmanlıklarımız',       en: 'Our Consulting' },

  // ── HAKKIMIZDA PAGE ────────────────────────────
  'hkm.tag':                { tr: 'Hakkımızda',               en: 'About Us' },
  'hkm.title':              { tr: 'Derin Akademi',            en: 'Derin Akademi' },

  // ── ILETISIM PAGE ──────────────────────────────
  'ilet.title':             { tr: 'İletişim',                 en: 'Contact' },
  'ilet.tag':               { tr: 'Bize Ulaşın',             en: 'Get In Touch' },

  // ── KARIYER PAGE ───────────────────────────────
  'kariyer.title':          { tr: 'Kariyer',                  en: 'Careers' },
  'kariyer.tag':            { tr: 'Kariyer Fırsatları',       en: 'Career Opportunities' },

  // ── BLOG PAGE ──────────────────────────────────
  'blog.title':             { tr: 'Blog',                     en: 'Blog' },
  'blog.tag':               { tr: 'Makaleler & Görüşler',     en: 'Articles & Insights' },
};

/* ── Core toggle logic ──────────────────────────── */
function daToggleLang() {
  const current = localStorage.getItem('da-lang') || 'tr';
  const next = current === 'tr' ? 'en' : 'tr';
  daSetLang(next);
}

function daSetLang(lang) {
  localStorage.setItem('da-lang', lang);
  document.documentElement.lang = lang === 'en' ? 'en' : 'tr';

  // Update toggle button text
  const btn = document.getElementById('langToggle');
  if (btn) btn.textContent = lang === 'tr' ? 'EN' : 'TR';

  // Translate all elements with data-i18n attribute
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (DA_TRANSLATIONS[key]) {
      el.textContent = DA_TRANSLATIONS[key][lang] || el.textContent;
    }
  });

  // Translate placeholder attributes
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    const key = el.getAttribute('data-i18n-placeholder');
    if (DA_TRANSLATIONS[key]) {
      el.placeholder = DA_TRANSLATIONS[key][lang] || el.placeholder;
    }
  });

  // Translate page <title> if it has data-i18n-title
  const titleEl = document.querySelector('title[data-i18n-title]');
  if (titleEl) {
    const key = titleEl.getAttribute('data-i18n-title');
    if (DA_TRANSLATIONS[key]) titleEl.textContent = DA_TRANSLATIONS[key][lang];
  }

  // Fire a custom event so other scripts can react
  window.dispatchEvent(new CustomEvent('da-lang-changed', { detail: { lang } }));
}

/* ── Init on page load ──────────────────────────── */
(function() {
  const saved = localStorage.getItem('da-lang') || 'tr';
  // Don't swap if already TR (default)
  if (saved === 'en') daSetLang('en');
  else {
    const btn = document.getElementById('langToggle');
    if (btn) btn.textContent = 'EN';
  }
})();
