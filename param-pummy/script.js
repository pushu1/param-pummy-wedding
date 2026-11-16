/**
 * PARAM & PUMMY — ROYAL PUNJABI WEDDING INVITATION
 * Interactive Cinematic Experience Scripts
 */

(function () {
  'use strict';

  // State
  let isTransitioning = false;
  let isInvitationOpen = false;
  let animationTimeouts = [];

  // Default Config
  const CONFIG = {
    weddingDateISO: '2026-12-02T11:00:00+05:30',
    publicUrl: localStorage.getItem('param_pummy_public_url') || 'https://pushu1.github.io/param-pummy-wedding/',
    hostPhone1: '9829312488',
    hostPhone2: '9079012387',
    venueAddress: 'Uday Vatika, Chadar wale Balaji, Pancham Nagar, Pali, Rajasthan',
  };

  // DOM Elements
  const coverStage = document.getElementById('cover-stage');
  const invitationMain = document.getElementById('invitation-main');
  const btnOpenInvite = document.getElementById('btn-open-invitation');
  const royalWaxSeal = document.getElementById('royal-seal');
  const btnSkipAnimation = document.getElementById('skip-animation-btn');
  const bgmPlayer = document.getElementById('bgm-player');
  const audioToggle = document.getElementById('audio-toggle');
  const discVinyl = document.getElementById('disc-vinyl');
  const audioBars = document.getElementById('audio-bars');

  // ===================================================================
  // 1. AUDIO PLAYER CONTROLLER
  // ===================================================================
  let isAudioPlaying = false;

  function initAudio() {
    if (!audioToggle || !bgmPlayer) return;

    audioToggle.addEventListener('click', toggleAudio);

    bgmPlayer.addEventListener('play', () => {
      isAudioPlaying = true;
      if (discVinyl) discVinyl.classList.add('is-spinning');
      if (audioBars) audioBars.classList.add('is-playing');
    });

    bgmPlayer.addEventListener('pause', () => {
      isAudioPlaying = false;
      if (discVinyl) discVinyl.classList.remove('is-spinning');
      if (audioBars) audioBars.classList.remove('is-playing');
    });
  }

  function startAudioPlayback() {
    if (!bgmPlayer) return;
    bgmPlayer.volume = 0.75;
    const playPromise = bgmPlayer.play();
    if (playPromise !== undefined) {
      playPromise.catch(() => {
        // Autoplay policy prevented playback until explicit user interaction
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
  // 2. CINEMATIC 3D ENVELOPE OPENING ANIMATION
  // ===================================================================
  function startCinematicOpening() {
    if (isTransitioning || isInvitationOpen) return;
    isTransitioning = true;

    // Start background audio
    startAudioPlayback();

    // Check reduced motion
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReducedMotion) {
      finishOpeningSequence();
      return;
    }

    // PHASE 1: Wax Seal Glows & Melts (0ms - 800ms)
    coverStage.classList.add('is-unsealing');

    // PHASE 2: Envelope Flap Opens in 3D (800ms - 2000ms)
    const t1 = setTimeout(() => {
      coverStage.classList.add('is-flapping');
    }, 850);
    animationTimeouts.push(t1);

    // PHASE 3: Card Emerges out of pocket (2000ms - 3600ms)
    const t2 = setTimeout(() => {
      coverStage.classList.add('is-card-rising');
    }, 2100);
    animationTimeouts.push(t2);

    // PHASE 4: Card blooms & expands to viewport (3600ms - 5000ms)
    const t3 = setTimeout(() => {
      coverStage.classList.add('is-card-expanding');
    }, 3700);
    animationTimeouts.push(t3);

    // PHASE 5: Reveal Main Invitation (5000ms)
    const t4 = setTimeout(() => {
      finishOpeningSequence();
    }, 5000);
    animationTimeouts.push(t4);
  }

  function finishOpeningSequence() {
    // Clear any pending timeouts
    animationTimeouts.forEach(t => clearTimeout(t));
    animationTimeouts = [];

    isTransitioning = false;
    isInvitationOpen = true;

    // Reveal main invitation
    if (invitationMain) {
      invitationMain.classList.add('is-active');
    }

    // Hide cover stage
    if (coverStage) {
      coverStage.classList.add('stage-hidden');
    }

    // Unlock document scrolling
    document.body.classList.remove('is-locked');

    // Smooth scroll to hero
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  window.replayCinematicOpening = function () {
    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'instant' });

    // Lock body
    document.body.classList.add('is-locked');

    // Reset classes
    if (coverStage) {
      coverStage.classList.remove('stage-hidden', 'is-unsealing', 'is-flapping', 'is-card-rising', 'is-card-expanding');
    }
    if (invitationMain) {
      invitationMain.classList.remove('is-active');
    }

    isTransitioning = false;
    isInvitationOpen = false;
  };

  // ===================================================================
  // 3. AMBIENT PARTICLE SYSTEM (GOLD DUST & ROSE PETALS)
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
    const maxParticles = window.innerWidth < 600 ? 25 : 45;

    // Particle types: Gold sparkles & Rose Petals
    for (let i = 0; i < maxParticles; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        radius: Math.random() * 2.5 + 1,
        speedY: Math.random() * 0.9 + 0.4,
        speedX: Math.random() * 0.6 - 0.3,
        opacity: Math.random() * 0.7 + 0.3,
        type: Math.random() > 0.4 ? 'gold' : 'petal',
        rotation: Math.random() * 360,
        rotationSpeed: (Math.random() - 0.5) * 1.5,
      });
    }

    function renderParticles() {
      ctx.clearRect(0, 0, width, height);

      particles.forEach(p => {
        p.y += p.speedY;
        p.x += Math.sin(p.y * 0.01) * 0.5 + p.speedX;
        p.rotation += p.rotationSpeed;

        if (p.y > height + 20) {
          p.y = -10;
          p.x = Math.random() * width;
        }

        ctx.save();
        ctx.translate(p.x, p.y);
        ctx.rotate((p.rotation * Math.PI) / 180);

        if (p.type === 'gold') {
          // Shimmering gold speck
          ctx.beginPath();
          ctx.arc(0, 0, p.radius, 0, Math.PI * 2);
          ctx.fillStyle = `rgba(243, 217, 159, ${p.opacity})`;
          ctx.shadowBlur = 8;
          ctx.shadowColor = '#ECC880';
          ctx.fill();
        } else {
          // Delicate Punjabi wedding rose petal
          ctx.beginPath();
          ctx.ellipse(0, 0, p.radius * 2.2, p.radius * 1.2, 0, 0, Math.PI * 2);
          ctx.fillStyle = `rgba(184, 109, 131, ${p.opacity * 0.8})`;
          ctx.shadowBlur = 4;
          ctx.shadowColor = '#F8E9E8';
          ctx.fill();
        }

        ctx.restore();
      });

      requestAnimationFrame(renderParticles);
    }

    // Only run if reduced motion is not preferred
    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      renderParticles();
    }
  }

  // ===================================================================
  // 4. LIVE REAL-TIME COUNTDOWN
  // ===================================================================
  function initCountdown() {
    const targetDate = new Date(CONFIG.weddingDateISO).getTime();
    const daysEl = document.getElementById('count-days');
    const hoursEl = document.getElementById('count-hours');
    const minutesEl = document.getElementById('count-minutes');
    const secondsEl = document.getElementById('count-seconds');
    const bannerEl = document.getElementById('countdown-live-banner');
    const gridEl = document.getElementById('countdown-grid');

    function update() {
      const now = Date.now();
      const diff = targetDate - now;

      if (diff <= 0) {
        if (daysEl) daysEl.textContent = '00';
        if (hoursEl) hoursEl.textContent = '00';
        if (minutesEl) minutesEl.textContent = '00';
        if (secondsEl) secondsEl.textContent = '00';
        if (gridEl) gridEl.style.display = 'none';
        if (bannerEl) bannerEl.style.display = 'block';
        return;
      }

      const days = Math.floor(diff / (1000 * 60 * 60 * 24));
      const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((diff % (1000 * 60)) / 1000);

      if (daysEl) daysEl.textContent = String(days).padStart(2, '0');
      if (hoursEl) hoursEl.textContent = String(hours).padStart(2, '0');
      if (minutesEl) minutesEl.textContent = String(minutes).padStart(2, '0');
      if (secondsEl) secondsEl.textContent = String(seconds).padStart(2, '0');
    }

    update();
    setInterval(update, 1000);
  }

  // ===================================================================
  // 5. ADD TO CALENDAR (.ICS) GENERATOR
  // ===================================================================
  window.addToCalendar = function (title, startLocal, endLocal, location, description) {
    // Format to YYYYMMDDTHHMMSS
    const formatTime = iso => iso.replace(/[-:]/g, '');
    const startTimeStr = formatTime(startLocal);
    const endTimeStr = formatTime(endLocal);

    const icsContent = [
      'BEGIN:VCALENDAR',
      'VERSION:2.0',
      'PRODID:-//Param and Pummy Wedding//EN',
      'CALSCALE:GREGORIAN',
      'METHOD:PUBLISH',
      'BEGIN:VEVENT',
      `SUMMARY:${title}`,
      `DESCRIPTION:${description}`,
      `LOCATION:${location}`,
      `DTSTART;TZID=Asia/Kolkata:${startTimeStr}`,
      `DTEND;TZID=Asia/Kolkata:${endTimeStr}`,
      'STATUS:CONFIRMED',
      'END:VEVENT',
      'END:VCALENDAR'
    ].join('\r\n');

    const blob = new Blob([icsContent], { type: 'text/calendar;charset=utf-8' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = `${title.replace(/[^a-zA-Z0-9]/g, '_')}.ics`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    showToast(`Added "${title}" to Calendar (.ics downloaded)`);
  };

  // ===================================================================
  // 6. PHOTO GALLERY LIGHTBOX & GUEST MEMORY PREVIEW
  // ===================================================================
  const galleryPhotos = [
    {
      src: 'assets/wedding_couple_0.jpg',
      caption: 'Our Royal Punjabi Wedding — A cinematic, anime-inspired wedding moment created for Param & Pummy.'
    },
    {
      src: 'assets/wedding_couple_1.jpg',
      caption: 'Our Wedding Moment — A special keepsake for Param & Pummy.'
    }
  ];
  let currentLightboxIndex = 0;

  window.openLightbox = function (index) {
    currentLightboxIndex = index;
    updateLightbox();
    const modal = document.getElementById('lightbox-modal');
    if (modal) modal.style.display = 'flex';
  };

  window.closeLightbox = function () {
    const modal = document.getElementById('lightbox-modal');
    if (modal) modal.style.display = 'none';
  };

  window.prevLightbox = function () {
    currentLightboxIndex = (currentLightboxIndex - 1 + galleryPhotos.length) % galleryPhotos.length;
    updateLightbox();
  };

  window.nextLightbox = function () {
    currentLightboxIndex = (currentLightboxIndex + 1) % galleryPhotos.length;
    updateLightbox();
  };

  function updateLightbox() {
    const imgEl = document.getElementById('lightbox-img');
    const capEl = document.getElementById('lightbox-caption');
    if (imgEl && galleryPhotos[currentLightboxIndex]) {
      imgEl.src = galleryPhotos[currentLightboxIndex].src;
      imgEl.alt = galleryPhotos[currentLightboxIndex].caption;
    }
    if (capEl && galleryPhotos[currentLightboxIndex]) {
      capEl.textContent = galleryPhotos[currentLightboxIndex].caption;
    }
  }

  // Keyboard navigation for Lightbox
  window.addEventListener('keydown', e => {
    const modal = document.getElementById('lightbox-modal');
    if (!modal || modal.style.display === 'none') return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') prevLightbox();
    if (e.key === 'ArrowRight') nextLightbox();
  });

  // Mobile swipe support for Lightbox
  let touchStartX = 0;
  const lightboxModal = document.getElementById('lightbox-modal');
  if (lightboxModal) {
    lightboxModal.addEventListener('touchstart', e => {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    lightboxModal.addEventListener('touchend', e => {
      const touchEndX = e.changedTouches[0].screenX;
      if (touchStartX - touchEndX > 50) nextLightbox();
      if (touchEndX - touchStartX > 50) prevLightbox();
    }, { passive: true });
  }

  // Guest Memory Upload Preview
  window.previewGuestMemory = function (input) {
    if (!input.files || !input.files[0]) return;
    const file = input.files[0];
    const reader = new FileReader();
    reader.onload = function (e) {
      const grid = document.getElementById('guest-preview-grid');
      if (grid) {
        const img = document.createElement('img');
        img.src = e.target.result;
        img.className = 'guest-preview-thumb';
        img.alt = 'Guest wedding memory preview';
        grid.appendChild(img);
        showToast('Photo added to preview! Thank you for sharing.');
      }
    };
    reader.readAsDataURL(file);
  };

  // ===================================================================
  // 7. INTERACTIVE RSVP & DIRECT WHATSAPP CONFIRMATION
  // ===================================================================
  window.handleRSVPSubmit = function (event) {
    event.preventDefault();
    const form = event.target;
    const name = form.name.value.trim();
    const phone = form.phone.value.trim();
    const guests = form.guests.value;
    const attending = form.attending.value === 'yes' ? 'Joyfully Accept' : 'Regretfully Decline';
    
    // Checked functions
    const selectedEvents = Array.from(form.querySelectorAll('input[name="events"]:checked')).map(el => el.value).join(', ') || 'All Functions';
    const message = form.message.value.trim();

    const rsvpRecord = {
      timestamp: new Date().toLocaleString(),
      name,
      phone,
      guests,
      attending,
      events: selectedEvents,
      message
    };

    // Store in localStorage
    const savedRSVPs = JSON.parse(localStorage.getItem('param_pummy_rsvps') || '[]');
    savedRSVPs.push(rsvpRecord);
    localStorage.setItem('param_pummy_rsvps', JSON.stringify(savedRSVPs));

    // Show feedback banner
    const feedbackBanner = document.getElementById('rsvp-feedback-banner');
    if (feedbackBanner) {
      feedbackBanner.className = 'rsvp-feedback success';
      feedbackBanner.style.display = 'block';
      feedbackBanner.innerHTML = `<strong>✨ Thank You, ${name}!</strong> Your RSVP has been recorded. Opening WhatsApp to notify the family...`;
    }

    // Compose formatted WhatsApp notification for the host
    const waText = encodeURIComponent(
      `*Wedding RSVP — Param & Pummy*\n\n` +
      `👤 *Name:* ${name}\n` +
      `📞 *Phone:* ${phone}\n` +
      `👥 *Guests:* ${guests}\n` +
      `🌸 *Status:* ${attending}\n` +
      `📅 *Functions:* ${selectedEvents}\n` +
      (message ? `💌 *Wishes:* "${message}"\n\n` : '\n') +
      `Sent via Param & Pummy Royal Wedding Experience.`
    );

    // Open WhatsApp after brief delay
    setTimeout(() => {
      window.open(`https://wa.me/91${CONFIG.hostPhone1}?text=${waText}`, '_blank', 'noopener');
    }, 1200);

    form.reset();
    showToast('RSVP saved! WhatsApp opened.');
  };

  // ===================================================================
  // 8. WHATSAPP SHARING HUB & UTILITIES
  // ===================================================================
  window.shareOnWhatsApp = function () {
    const text = encodeURIComponent(
      `ੴ With the blessings of Waheguru\n\n` +
      `Mr. Sewa Singh Rodh & Mrs. Gurmeet Kaur Rodh cordially invite you to celebrate the royal wedding of their son:\n\n` +
      `✨ *Paramveer Singh (Param)* & *Manpreet Kaur (Pummy)* ✨\n\n` +
      `📅 *Wedding Ceremony:* 02 December 2026 at 11:00 AM\n` +
      `🎉 *Grand Reception:* 03 December 2026 at 7:00 PM\n` +
      `📍 *Venue:* Uday Vatika, Pali, Rajasthan\n\n` +
      `Experience our cinematic invitation here:\n` +
      `${CONFIG.publicUrl}`
    );
    window.open(`https://wa.me/?text=${text}`, '_blank', 'noopener');
  };

  window.nativeShare = async function () {
    const shareData = {
      title: 'Param & Pummy — Royal Wedding Invitation',
      text: 'With the blessings of Waheguru, you are cordially invited to celebrate the wedding of Paramveer Singh & Manpreet Kaur on 2 December 2026 in Pali, Rajasthan.',
      url: CONFIG.publicUrl
    };

    if (navigator.share) {
      try {
        await navigator.share(shareData);
      } catch (err) {
        // User cancelled or share failed
      }
    } else {
      copyInvitationLink();
    }
  };

  window.copyInvitationLink = async function () {
    try {
      await navigator.clipboard.writeText(CONFIG.publicUrl);
      showToast('Invitation link copied to clipboard!');
    } catch (err) {
      // Fallback
      prompt('Copy this wedding invitation URL:', CONFIG.publicUrl);
    }
  };

  window.copyVenueAddress = async function () {
    try {
      await navigator.clipboard.writeText(CONFIG.venueAddress);
      showToast('Venue address copied to clipboard!');
    } catch (err) {
      prompt('Copy venue address:', CONFIG.venueAddress);
    }
  };

  // Toast Notification
  function showToast(msg) {
    const toast = document.getElementById('toast-notice');
    if (!toast) return;
    toast.textContent = msg;
    toast.classList.add('show');
    setTimeout(() => {
      toast.classList.remove('show');
    }, 3500);
  }

  // ===================================================================
  // 9. HOST ADMIN PANEL & CSV EXPORT
  // ===================================================================
  window.openAdminModal = function () {
    const modal = document.getElementById('admin-modal');
    if (!modal) return;
    modal.style.display = 'flex';
    renderAdminRSVPs();
  };

  window.closeAdminModal = function () {
    const modal = document.getElementById('admin-modal');
    if (modal) modal.style.display = 'none';
  };

  function renderAdminRSVPs() {
    const records = JSON.parse(localStorage.getItem('param_pummy_rsvps') || '[]');
    const tbody = document.getElementById('admin-rsvp-tbody');
    const totalEl = document.getElementById('stat-total-rsvps');
    const guestsEl = document.getElementById('stat-total-guests');

    if (totalEl) totalEl.textContent = records.length;

    let guestCount = 0;
    records.forEach(r => {
      const g = parseInt(r.guests, 10);
      guestCount += isNaN(g) ? 5 : g;
    });
    if (guestsEl) guestsEl.textContent = guestCount;

    if (!tbody) return;

    if (records.length === 0) {
      tbody.innerHTML = '<tr><td colspan="6" style="text-align:center;color:#888;">No RSVPs recorded yet.</td></tr>';
      return;
    }

    tbody.innerHTML = records.map(r => `
      <tr>
        <td>${r.timestamp}</td>
        <td><strong>${escapeHtml(r.name)}</strong></td>
        <td>${escapeHtml(r.phone)}</td>
        <td>${escapeHtml(r.guests)}</td>
        <td>${escapeHtml(r.attending)}</td>
        <td>${escapeHtml(r.message || '-')}</td>
      </tr>
    `).join('');
  }

  window.exportRSVPstoCSV = function () {
    const records = JSON.parse(localStorage.getItem('param_pummy_rsvps') || '[]');
    if (records.length === 0) {
      alert('No RSVP records to export yet.');
      return;
    }

    const headers = ['Timestamp', 'Full Name', 'Phone', 'Guests', 'Status', 'Functions', 'Message'];
    const rows = records.map(r => [
      `"${r.timestamp}"`,
      `"${r.name}"`,
      `"${r.phone}"`,
      `"${r.guests}"`,
      `"${r.attending}"`,
      `"${r.events}"`,
      `"${(r.message || '').replace(/"/g, '""')}"`
    ]);

    const csvContent = [headers.join(','), ...rows.map(row => row.join(','))].join('\r\n');
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = `Param_Pummy_Wedding_RSVPs_${new Date().toISOString().slice(0, 10)}.csv`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    showToast('Exported RSVPs to CSV successfully!');
  };

  window.clearRSVPRecords = function () {
    if (confirm('Are you sure you want to clear all stored RSVP records?')) {
      localStorage.removeItem('param_pummy_rsvps');
      renderAdminRSVPs();
      showToast('RSVP records reset.');
    }
  };

  function escapeHtml(str) {
    if (!str) return '';
    return str.replace(/[&<>"']/g, m => ({
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&quot;',
      "'": '&#39;'
    })[m]);
  }

  // Admin URL update
  const adminUrlInput = document.getElementById('admin-public-url');
  if (adminUrlInput) {
    adminUrlInput.addEventListener('change', e => {
      CONFIG.publicUrl = e.target.value.trim();
      localStorage.setItem('param_pummy_public_url', CONFIG.publicUrl);
      showToast('Public invitation URL updated!');
    });
  }

  // ===================================================================
  // 10. INITIALIZATION
  // ===================================================================
  function init() {
    // Bind opening triggers
    if (btnOpenInvite) btnOpenInvite.addEventListener('click', startCinematicOpening);
    if (royalWaxSeal) royalWaxSeal.addEventListener('click', startCinematicOpening);
    if (btnSkipAnimation) btnSkipAnimation.addEventListener('click', finishOpeningSequence);

    // Init components
    initAudio();
    initAmbientCanvas();
    initCountdown();
  }

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
