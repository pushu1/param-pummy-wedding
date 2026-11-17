/**
 * KULDEEP & TEENA — ROYAL DIGITAL WEDDING INVITATION
 * Faithfully recreating the Pinterest Wedding Invitation Reference
 * URL: https://in.pinterest.com/pin/1071012355158491151/
 */

(function () {
  'use strict';

  // State
  let isTransitioning = false;
  let isInvitationOpen = false;
  let animationTimeouts = [];

  // Configuration
  const CONFIG = {
    weddingDateISO: '2026-12-11T07:30:00+05:30',
    publicUrl: 'https://pushu1.github.io/param-pummy-wedding/',
    mapsUrl: 'https://maps.app.goo.gl/hPi6DXWJZEpUG5Vm9',
    hostPhone1: '9461061236',
    hostPhone2: '9887997822',
    venueAddress: 'Jain Bagbera Dadawadi, Venkatesh Marg, Pali, Rajasthan 306401, India',
  };

  // DOM Elements
  const coverStage = document.getElementById('cover-stage');
  const invitationMain = document.getElementById('invitation-main');
  const waxSealBtn = document.getElementById('wax-seal-button');
  const btnClickHere = document.getElementById('btn-click-here');
  const bgmPlayer = document.getElementById('bgm-player');
  const audioToggle = document.getElementById('audio-toggle');
  const speakerIcon = document.getElementById('speaker-icon');
  const audioBars = document.getElementById('audio-bars');
  const guestbookForm = document.getElementById('guestbook-form');
  const guestbookFeed = document.getElementById('guestbook-feed');
  const toastPopup = document.getElementById('toast-popup');
  const dockItems = document.querySelectorAll('.p-dock-item');

  // ===================================================================
  // 1. BACKGROUND AUDIO CONTROLLER
  // ===================================================================
  let isAudioPlaying = false;

  function initAudio() {
    if (!audioToggle || !bgmPlayer) return;

    audioToggle.addEventListener('click', toggleAudio);

    bgmPlayer.addEventListener('play', () => {
      isAudioPlaying = true;
      audioToggle.classList.add('is-playing');
      if (speakerIcon) speakerIcon.textContent = '🔊';
    });

    bgmPlayer.addEventListener('pause', () => {
      isAudioPlaying = false;
      audioToggle.classList.remove('is-playing');
      if (speakerIcon) speakerIcon.textContent = '🔈';
    });
  }

  function startAudioPlayback() {
    if (!bgmPlayer) return;
    bgmPlayer.volume = 0.85;
    const playPromise = bgmPlayer.play();
    if (playPromise !== undefined) {
      playPromise.catch(() => {
        isAudioPlaying = false;
      });
    }
  }

  function toggleAudio() {
    if (!bgmPlayer) return;
    if (bgmPlayer.paused) {
      bgmPlayer.play().catch(() => {});
    } else {
      bgmPlayer.pause();
    }
  }

  // ===================================================================
  // 2. CINEMATIC ENVELOPE OPENING ANIMATION
  // ===================================================================
  function startEnvelopeOpening() {
    if (isTransitioning || isInvitationOpen) return;
    isTransitioning = true;

    // Start background wedding music
    startAudioPlayback();

    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReducedMotion) {
      finishOpeningSequence();
      return;
    }

    // PHASE 1: Wax Seal Glows & Light Burst (0ms - 800ms)
    coverStage.classList.add('is-unsealing');

    // PHASE 2: Envelope Flap Opens Upward (850ms - 2000ms)
    const t1 = setTimeout(() => {
      coverStage.classList.add('is-flapping');
    }, 850);
    animationTimeouts.push(t1);

    // PHASE 3: Wedding Card Slides Out (2000ms - 3500ms)
    const t2 = setTimeout(() => {
      coverStage.classList.add('is-card-rising');
    }, 2000);
    animationTimeouts.push(t2);

    // PHASE 4: Card Expands to Fill Viewport (3600ms - 4800ms)
    const t3 = setTimeout(() => {
      coverStage.classList.add('is-card-expanding');
    }, 3600);
    animationTimeouts.push(t3);

    // PHASE 5: Transition to Main Card (4900ms)
    const t4 = setTimeout(() => {
      finishOpeningSequence();
    }, 4900);
    animationTimeouts.push(t4);
  }

  function finishOpeningSequence() {
    animationTimeouts.forEach(t => clearTimeout(t));
    animationTimeouts = [];

    isTransitioning = false;
    isInvitationOpen = true;

    if (invitationMain) {
      invitationMain.classList.add('is-active');
    }

    if (coverStage) {
      coverStage.classList.add('stage-dismissed');
    }

    document.body.classList.remove('is-locked');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  window.replayEnvelopeOpening = function () {
    window.scrollTo({ top: 0, behavior: 'instant' });
    document.body.classList.add('is-locked');

    if (coverStage) {
      coverStage.classList.remove('stage-dismissed', 'is-unsealing', 'is-flapping', 'is-card-rising', 'is-card-expanding');
    }
    if (invitationMain) {
      invitationMain.classList.remove('is-active');
    }

    isTransitioning = false;
    isInvitationOpen = false;
  };

  // ===================================================================
  // 3. AMBIENT PARTICLES CANVAS (GOLD DUST & PETALS)
  // ===================================================================
  function initAmbientCanvas() {
    const canvas = document.getElementById('ambient-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    window.addEventListener('resize', () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    });

    const particles = [];
    const maxParticles = window.innerWidth < 600 ? 20 : 35;

    for (let i = 0; i < maxParticles; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        radius: Math.random() * 2 + 1,
        speedY: Math.random() * 0.7 + 0.3,
        speedX: Math.random() * 0.4 - 0.2,
        opacity: Math.random() * 0.6 + 0.25,
        color: Math.random() > 0.4 ? 'rgba(212, 175, 55, ' : 'rgba(240, 215, 170, '
      });
    }

    function render() {
      ctx.clearRect(0, 0, width, height);

      particles.forEach(p => {
        p.y += p.speedY;
        p.x += p.speedX;

        if (p.y > height) {
          p.y = -10;
          p.x = Math.random() * width;
        }
        if (p.x > width) p.x = 0;
        if (p.x < 0) p.x = width;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = p.color + p.opacity + ')';
        ctx.fill();
      });

      requestAnimationFrame(render);
    }

    render();
  }

  // ===================================================================
  // 4. FLOATING DOCK NAVIGATION & SCROLL SPY
  // ===================================================================
  function initFloatingDock() {
    const sections = ['ceremonies-section', 'location-section', 'gallery-section', 'wishes-section'];

    dockItems.forEach(item => {
      item.addEventListener('click', e => {
        const targetId = item.getAttribute('href').replace('#', '');
        const targetEl = document.getElementById(targetId);
        if (targetEl) {
          e.preventDefault();
          targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
          dockItems.forEach(d => d.classList.remove('is-active'));
          item.classList.add('is-active');
        }
      });
    });

    // Scroll spy
    window.addEventListener('scroll', () => {
      let currentSection = '';
      const scrollPos = window.scrollY + 200;

      sections.forEach(id => {
        const el = document.getElementById(id);
        if (el) {
          const top = el.offsetTop;
          const height = el.offsetHeight;
          if (scrollPos >= top && scrollPos < top + height) {
            currentSection = id;
          }
        }
      });

      if (currentSection) {
        dockItems.forEach(item => {
          if (item.getAttribute('data-section') === currentSection) {
            item.classList.add('is-active');
          } else {
            item.classList.remove('is-active');
          }
        });
      }
    }, { passive: true });
  }

  // ===================================================================
  // 5. ADD TO CALENDAR HELPER
  // ===================================================================
  window.addToCalendar = function (title, startIso, endIso, location, description) {
    const formatTime = iso => iso.replace(/[-:]/g, '').replace('.000', '') + 'Z';
    const sDate = new Date(startIso);
    const eDate = new Date(endIso);
    const startStr = sDate.toISOString().replace(/[-:]/g, '').split('.')[0] + 'Z';
    const endStr = eDate.toISOString().replace(/[-:]/g, '').split('.')[0] + 'Z';

    const googleCalUrl = `https://calendar.google.com/calendar/render?action=TEMPLATE&text=${encodeURIComponent(title)}&dates=${startStr}/${endStr}&details=${encodeURIComponent(description)}&location=${encodeURIComponent(location)}`;
    window.open(googleCalUrl, '_blank');
  };

  // ===================================================================
  // 6. GUESTBOOK / BLESSING SUBMISSION
  // ===================================================================
  function initGuestbook() {
    if (!guestbookForm || !guestbookFeed) return;

    // Load saved wishes
    const saved = localStorage.getItem('kuldeep_teena_wishes');
    if (saved) {
      try {
        const list = JSON.parse(saved);
        list.forEach(w => prependWishCard(w.name, w.message, w.time));
      } catch (e) {}
    }

    guestbookForm.addEventListener('submit', e => {
      e.preventDefault();
      const nameInput = document.getElementById('guest-name');
      const msgInput = document.getElementById('guest-message');
      const name = nameInput.value.trim();
      const message = msgInput.value.trim();

      if (!name || !message) return;

      const dateStr = new Date().toLocaleDateString('en-GB') + ' | Warm Blessing';
      prependWishCard(name, message, dateStr);

      // Save to localStorage
      try {
        const current = JSON.parse(localStorage.getItem('kuldeep_teena_wishes') || '[]');
        current.unshift({ name, message, time: dateStr });
        localStorage.setItem('kuldeep_teena_wishes', JSON.stringify(current));
      } catch (e) {}

      nameInput.value = '';
      msgInput.value = '';

      showToast('Thank you for your warm blessings for Kuldeep & Teena! ♥');
    });
  }

  function prependWishCard(name, message, time) {
    if (!guestbookFeed) return;
    const card = document.createElement('div');
    card.className = 'p-wish-card';
    card.innerHTML = `
      <div class="p-wish-author">
        <span class="p-author-avatar">💛</span>
        <span class="p-author-name">${escapeHtml(name)}</span>
      </div>
      <p class="p-wish-text">"${escapeHtml(message)}"</p>
      <span class="p-wish-time">${escapeHtml(time)}</span>
    `;
    guestbookFeed.prepend(card);
  }

  function escapeHtml(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }

  // ===================================================================
  // 7. TOAST POPUP HELPER
  // ===================================================================
  function showToast(msg) {
    if (!toastPopup) return;
    toastPopup.textContent = msg;
    toastPopup.classList.add('show');
    setTimeout(() => {
      toastPopup.classList.remove('show');
    }, 3800);
  }

  // ===================================================================
  // 8. INITIALIZATION
  // ===================================================================
  function init() {
    // Single Click Action: CLICK HERE Button
    if (btnClickHere) {
      btnClickHere.addEventListener('click', (e) => {
        e.stopPropagation();
        startEnvelopeOpening();
      });
    }

    if (waxSealBtn) {
      waxSealBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        startEnvelopeOpening();
      });
    }

    if (coverStage) {
      coverStage.addEventListener('click', () => {
        startEnvelopeOpening();
      });
    }

    initAudio();
    initAmbientCanvas();
    initFloatingDock();
    initGuestbook();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
