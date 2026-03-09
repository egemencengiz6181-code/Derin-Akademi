/* ═══════════════════════════════════════════════════════════════
   DERIN AKADEMİ — SHARED JAVASCRIPT
   ═══════════════════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {

  /* ── 1. STICKY NAV ──────────────────────────────────────────── */
  const navbar = document.getElementById('navbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      navbar.classList.toggle('scrolled', window.scrollY > 50);
    }, { passive: true });
  }

  /* ── 2. ACTIVE NAV LINK ─────────────────────────────────────── */
  const currentPage = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('#navbar .nav-links a, .mobile-nav a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  /* ── 3. SCROLL REVEAL ───────────────────────────────────────── */
  const revealObs = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
  document.querySelectorAll('.reveal').forEach(el => revealObs.observe(el));

  /* ── 4. COUNTER ANIMATION ───────────────────────────────────── */
  const counterObs = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      const suffix = el.querySelector('em') ? el.querySelector('em').textContent : '';
      const rawText = el.textContent.replace(suffix, '').trim();
      const target = parseFloat(rawText);
      if (isNaN(target)) return;
      let current = 0;
      const increment = target / 70;
      const timer = setInterval(() => {
        current = Math.min(current + increment, target);
        const val = target % 1 !== 0 ? current.toFixed(1) : Math.round(current);
        el.innerHTML = val + (suffix ? `<em>${suffix}</em>` : '');
        if (current >= target) clearInterval(timer);
      }, 14);
      counterObs.unobserve(el);
    });
  }, { threshold: 0.5 });
  document.querySelectorAll('.stat-num').forEach(el => counterObs.observe(el));

  /* ── 5. MOBILE MENU ─────────────────────────────────────────── */
  const menuToggle = document.querySelector('.menu-toggle');
  const mobileNav  = document.querySelector('.mobile-nav');
  const mobileClose= document.querySelector('.mobile-nav-close');
  if (menuToggle && mobileNav) {
    menuToggle.addEventListener('click', () => mobileNav.classList.add('open'));
    mobileClose?.addEventListener('click', () => mobileNav.classList.remove('open'));
    mobileNav.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => mobileNav.classList.remove('open'));
    });
  }

  /* ── 6. CARD TILT EFFECT ────────────────────────────────────── */
  document.querySelectorAll('.course-card[data-tilt]').forEach(card => {
    card.addEventListener('mousemove', e => {
      const r = card.getBoundingClientRect();
      const dx = (e.clientX - r.left - r.width / 2) / (r.width / 2);
      const dy = (e.clientY - r.top - r.height / 2) / (r.height / 2);
      card.style.transform = `translateY(-7px) rotateX(${-dy * 4}deg) rotateY(${dx * 4}deg)`;
    });
    card.addEventListener('mouseleave', () => { card.style.transform = ''; });
  });

  /* ── 7. SMOOTH ANCHOR SCROLL ────────────────────────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const target = document.querySelector(a.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  /* ── 8. FILTER BUTTONS ──────────────────────────────────────── */
  document.querySelectorAll('.filter-group').forEach(group => {
    group.querySelectorAll('.filter-btn').forEach(btn => {
      btn.addEventListener('click', function () {
        group.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        const filter = this.dataset.filter;
        const cards = document.querySelectorAll('[data-category]');
        cards.forEach(card => {
          if (filter === 'all' || card.dataset.category === filter) {
            card.style.display = '';
            card.style.opacity = '1';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  });

  /* ── 9. TOAST NOTIFICATION ──────────────────────────────────── */
  window.showToast = (msg, type = 'success') => {
    const toast = document.createElement('div');
    toast.style.cssText = `
      position:fixed;bottom:28px;right:28px;z-index:9999;
      background:rgba(7,20,40,0.97);border:1px solid ${type==='success'?'rgba(0,200,180,0.4)':'rgba(255,77,77,0.4)'};
      color:${type==='success'?'var(--teal)':'#ff6b6b'};padding:14px 22px;
      border-radius:12px;font-size:14px;font-weight:500;backdrop-filter:blur(16px);
      box-shadow:0 8px 32px rgba(0,0,0,0.5);animation:toastIn 0.3s ease;
    `;
    toast.textContent = msg;
    document.body.appendChild(toast);
    setTimeout(() => { toast.style.opacity='0'; toast.style.transition='opacity 0.4s'; setTimeout(()=>toast.remove(),400); }, 3000);
  };

  const style = document.createElement('style');
  style.textContent = `@keyframes toastIn { from{opacity:0;transform:translateY(16px)} to{opacity:1;transform:translateY(0)} }`;
  document.head.appendChild(style);

  /* ── 10. BACK TO TOP ────────────────────────────────────────── */
  const btt = document.getElementById('back-to-top');
  if (btt) {
    window.addEventListener('scroll', () => {
      btt.style.opacity = window.scrollY > 500 ? '1' : '0';
      btt.style.pointerEvents = window.scrollY > 500 ? 'all' : 'none';
    }, { passive: true });
    btt.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  }
});

/* ── TEKLIF MODAL ───────────────────────────────────────────── */
window.openTeklifModal = function() {
  const m = document.getElementById('teklif-modal');
  if (m) { m.classList.add('open'); document.body.style.overflow = 'hidden'; }
};
window.closeTeklifModal = function() {
  const m = document.getElementById('teklif-modal');
  if (m) { m.classList.remove('open'); document.body.style.overflow = ''; }
};
document.addEventListener('click', function(e) {
  if (e.target && e.target.id === 'teklif-modal') window.closeTeklifModal();
});
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') window.closeTeklifModal();
});
