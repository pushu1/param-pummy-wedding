/**
 * CHIRANJEEV KULDEEP & SOU. KA. TINA
 * Royal Digital Wedding Invitation Experience
 * Inspired by Reference Video: 3D Envelope Opening & Interactive Journey
 */

(function () {
  'use strict';

  // State Variables
  let isTransitioning = false;
  let isInvitationOpen = false;
  let animationTimeouts = [];

  // Configuration
  const CONFIG = {
    weddingDateISO: '2026-12-11T07:30:00+05:30', // Baraat / Wedding day start
    publicUrl: localStorage.getItem('kuldeep_tina_public_url') || 'https://pushu1.github.io/param-pummy-wedding/',
    mapsUrl: 'https://maps.app.goo.gl/hPi6DXWJZEpUG5Vm9',
    hostPhone1: '9461061236',
    hostPhone2: '9887997822',
    venueAddress: 'Jain Bagbera Dadawadi, Venkatesh Marg, Pali, Rajasthan 306401, India',
  };

  // DOM Elements
  const coverStage = document.getElementById('cover-stage');
  const invitationMain = document.getElementById('invitation-main');
  const btnOpenInvite = document.getElementById('btn-open-invitation');
  const waxSealBtn = document.getElementById('wax-seal-button');
  const btnSkipAnimation = document.getElementById('skip-animation-btn');
  const bgmPlayer = document.getElementById('bgm-player');
  const audioToggle = document.getElementById('audio-toggle');
  const discIcon = document.getElementById('disc-icon');
  const audioBars = document.getElementById('audio-bars');

  // ===================================================================
  // 1. BACKGROUND AUDIO CONTROLLER
  // ===================================================================
  let isAudioPlaying = false;

  function initAudio() {
    if (!audioToggle || !bgmPlayer) return;

    audioToggle.addEventListener('click', toggleAudio);

    bgmPlayer.addEventListener('play', () => {
      isAudioPlaying = true;
      if (discIcon) discIcon.classList.add('is-spinning');
      if (audioBars) audioBars.classList.add('is-playing');
    });

    bgmPlayer.addEventListener('pause', () => {
      isAudioPlaying = false;
      if (discIcon) discIcon.classList.remove('is-spinning');
      if (audioBars) audioBars.classList.remove('is-playing');
    });
  }

  function startAudioPlayback() {
    if (!bgmPlayer) return;
    bgmPlayer.volume = 0.8;
    const playPromise = bgmPlayer.play();
    if (playPromise !== undefined) {
      playPromise.catch(() => {
        // Autoplay policy prevented playback until user interaction
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
  // 2. CINEMATIC 3D ENVELOPE OPENING ANIMATION (REFERENCE VIDEO STYLE)
  // ===================================================================
  function startEnvelopeOpening() {
    if (isTransitioning || isInvitationOpen) return;
    isTransitioning = true;

    // Start background wedding music
    startAudioPlayback();

    // Check accessibility reduced motion
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReducedMotion) {
      finishOpeningSequence();
      return;
    }

    // PHASE 1: Wax Seal Glows & Illuminates (0ms - 800ms)
    coverStage.classList.add('is-unsealing');

    // PHASE 2: Envelope Flap Opens Upward with 3D Perspective (850ms - 2000ms)
    const t1 = setTimeout(() => {
      coverStage.classList.add('is-flapping');
    }, 850);
    animationTimeouts.push(t1);

    // PHASE 3: Wedding Card Slides Out of Pocket & Shimmers (2100ms - 3600ms)
    const t2 = setTimeout(() => {
      coverStage.classList.add('is-card-rising');
    }, 2100);
    animationTimeouts.push(t2);

    // PHASE 4: Card Blooms Forward & Expands to Viewport (3700ms - 5000ms)
    const t3 = setTimeout(() => {
      coverStage.classList.add('is-card-expanding');
    }, 3700);
    animationTimeouts.push(t3);

    // PHASE 5: Reveal Main Invitation Website (5000ms)
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

    // Activate main invitation
    if (invitationMain) {
      invitationMain.classList.add('is-active');
    }

    // Hide envelope stage
    if (coverStage) {
      coverStage.classList.add('stage-dismissed');
    }

    // Unlock page scrolling
    document.body.classList.remove('is-locked');

    // Smooth scroll to hero
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  window.replayEnvelopeOpening = function () {
    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'instant' });

    // Lock body
    document.body.classList.add('is-locked');

    // Reset envelope classes
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
  // 3. AMBIENT PARTICLES CANVAS (GOLD PARTICLES & ROSE PETALS)
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

    for (let i = 0; i < maxParticles; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        radius: Math.random() * 2.5 + 1,
        speedY: Math.random() * 0.8 + 0.35,
        speedX: Math.random() * 0.5 - 0.25,
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
          ctx.beginPath();
          ctx.arc(0, 0, p.radius, 0, Math.PI * 2);
          ctx.fillStyle = `rgba(212, 175, 55, ${p.opacity})`;
          ctx.shadowBlur = 8;
          ctx.shadowColor = '#D4AF37';
          ctx.fill();
        } else {
          ctx.beginPath();
          ctx.ellipse(0, 0, p.radius * 2.2, p.radius * 1.2, 0, 0, Math.PI * 2);
          ctx.fillStyle = `rgba(224, 185, 155, ${p.opacity * 0.8})`;
          ctx.shadowBlur = 4;
          ctx.shadowColor = '#FAF7F2';
          ctx.fill();
        }

        ctx.restore();
      });

      requestAnimationFrame(renderParticles);
    }

    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      renderParticles();
    }
  }

  // ===================================================================
  // 4. LIVE REAL-TIME WEDDING COUNTDOWN TIMER
  // ===================================================================
  function initCountdown() {
    const targetDate = new Date(CONFIG.weddingDateISO).getTime();
    const daysEl = document.getElementById('cd-days');
    const hoursEl = document.getElementById('cd-hours');
    const minutesEl = document.getElementById('cd-minutes');
    const secondsEl = document.getElementById('cd-seconds');
    const clockEl = document.getElementById('countdown-clock');
    const bannerEl = document.getElementById('cd-celebration-banner');

    function updateClock() {
      const now = Date.now();
      const diff = targetDate - now;

      if (diff <= 0) {
        if (daysEl) daysEl.textContent = '00';
        if (hoursEl) hoursEl.textContent = '00';
        if (minutesEl) minutesEl.textContent = '00';
        if (secondsEl) secondsEl.textContent = '00';
        if (clockEl) clockEl.style.display = 'none';
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

    updateClock();
    setInterval(updateClock, 1000);
  }

  // ===================================================================
  // 5. ADD TO CALENDAR (.ICS) GENERATOR
  // ===================================================================
  window.addToCalendar = function (title, startLocal, endLocal, location, description) {
    const formatTime = iso => iso.replace(/[-:]/g, '');
    const startTimeStr = formatTime(startLocal);
    const endTimeStr = formatTime(endLocal);

    const icsContent = [
      'BEGIN:VCALENDAR',
      'VERSION:2.0',
      'PRODID:-//Kuldeep & Tina Wedding//EN',
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

    showToast(`Added "${title}" to your calendar!`);
  };

  // ===================================================================
  // 6. INTERACTIVE RSVP & DIRECT WHATSAPP CONFIRMATION
  // ===================================================================
  window.handleRSVPSubmit = function (event) {
    event.preventDefault();
    const form = event.target;
    const name = form.name.value.trim();
    const phone = form.phone.value.trim();
    const guests = form.guests.value;
    const attending = form.attending.value === 'yes' ? 'Joyfully Accept with Family' : 'Regretfully Unable to Attend';
    
    const selectedEvents = Array.from(form.querySelectorAll('input[name="events"]:checked'))
      .map(el => el.value).join(', ') || 'All Functions';
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
    const savedRSVPs = JSON.parse(localStorage.getItem('kuldeep_tina_rsvps') || '[]');
    savedRSVPs.push(rsvpRecord);
    localStorage.setItem('kuldeep_tina_rsvps', JSON.stringify(savedRSVPs));

    // Feedback banner
    const feedbackBanner = document.getElementById('rsvp-success-banner');
    if (feedbackBanner) {
      feedbackBanner.style.display = 'block';
      feedbackBanner.innerHTML = `<strong>✨ Thank You, ${name}!</strong> Your RSVP has been confirmed. Forwarding to the family on WhatsApp...`;
    }

    // Format WhatsApp Message for the host
    const waText = encodeURIComponent(
      `*Wedding RSVP — Chiranjeev Kuldeep & Sou. Ka. Tina*\n\n` +
      `👤 *Name:* ${name}\n` +
      `📞 *Phone:* ${phone}\n` +
      `👥 *Family Members:* ${guests}\n` +
      `🌸 *Attendance:* ${attending}\n` +
      `📅 *Ceremonies:* ${selectedEvents}\n` +
      (message ? `💌 *Warm Wishes:* "${message}"\n\n` : '\n') +
      `Sent via Kuldeep & Tina Royal Wedding Experience.`
    );

    // Open WhatsApp after slight pause
    setTimeout(() => {
      window.open(`https://wa.me/91${CONFIG.hostPhone2}?text=${waText}`, '_blank', 'noopener');
    }, 1200);

    form.reset();
    showToast('RSVP confirmed! Opening WhatsApp.');
  };

  // ===================================================================
  // 7. WHATSAPP SHARING HUB & UTILITIES
  // ===================================================================
  window.shareOnWhatsApp = function () {
    const text = encodeURIComponent(
      `॥ श्री गणेशाय नमः ॥\n\n` +
      `By the divine blessings of Lord Shri Vinayakji Maharaj, Smt. Chandra Devi & Shri Jasrajji Upadhyay cordially invite you to celebrate the auspicious wedding of their beloved son:\n\n` +
      `✨ *Chiranjeev Kuldeep* & *Sou. Ka. Tina* ✨\n\n` +
      `📅 *Wedding Ceremony:* Friday, 11 December 2026\n` +
      `🎉 *Blessing Ceremony & Grand Reception:* Sunday, 13 December 2026 (06:00 PM onwards)\n` +
      `📍 *Reception Venue:* Jain Bagbera Dadawadi, Venkatesh Marg, Pali, Rajasthan\n\n` +
      `Experience our luxury cinematic wedding invitation here:\n` +
      `${CONFIG.publicUrl}`
    );
    window.open(`https://wa.me/?text=${text}`, '_blank', 'noopener');
  };

  window.nativeShare = async function () {
    const shareData = {
      title: 'Kuldeep & Tina — Royal Wedding Invitation',
      text: '॥ श्री गणेशाय नमः ॥ You are cordially invited to celebrate the auspicious wedding ceremony of Chiranjeev Kuldeep & Sou. Ka. Tina on 11 December 2026 in Pali, Rajasthan.',
      url: CONFIG.publicUrl
    };

    if (navigator.share) {
      try {
        await navigator.share(shareData);
      } catch (err) {}
    } else {
      copyInvitationLink();
    }
  };

  window.copyInvitationLink = async function () {
    try {
      await navigator.clipboard.writeText(CONFIG.publicUrl);
      showToast('Invitation link copied to clipboard!');
    } catch (err) {
      prompt('Copy invitation link:', CONFIG.publicUrl);
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

  // Toast Notification helper
  function showToast(msg) {
    const toast = document.getElementById('toast-popup');
    if (!toast) return;
    toast.textContent = msg;
    toast.classList.add('show');
    setTimeout(() => {
      toast.classList.remove('show');
    }, 3500);
  }

  // ===================================================================
  // 8. HOST ADMINISTRATION & CSV EXPORT
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
    const records = JSON.parse(localStorage.getItem('kuldeep_tina_rsvps') || '[]');
    const tbody = document.getElementById('admin-rsvp-table-body');
    const totalEl = document.getElementById('admin-stat-responses');
    const guestsEl = document.getElementById('admin-stat-guests');

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

  window.exportRSVPsToCSV = function () {
    const records = JSON.parse(localStorage.getItem('kuldeep_tina_rsvps') || '[]');
    if (records.length === 0) {
      alert('No RSVP records to export yet.');
      return;
    }

    const headers = ['Timestamp', 'Full Name', 'Phone', 'Guests', 'Status', 'Ceremonies', 'Wishes'];
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
    link.download = `Kuldeep_Tina_Wedding_RSVPs_${new Date().toISOString().slice(0, 10)}.csv`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    showToast('Exported RSVPs to CSV successfully!');
  };

  window.clearRSVPRecords = function () {
    if (confirm('Are you sure you want to clear all stored RSVP records?')) {
      localStorage.removeItem('kuldeep_tina_rsvps');
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

  // Update public URL from admin
  const adminUrlInput = document.getElementById('admin-website-url');
  if (adminUrlInput) {
    adminUrlInput.addEventListener('change', e => {
      CONFIG.publicUrl = e.target.value.trim();
      localStorage.setItem('kuldeep_tina_public_url', CONFIG.publicUrl);
      showToast('Public website URL updated!');
    });
  }

  // ===================================================================
  // 9. INITIALIZATION
  // ===================================================================
  function init() {
    if (btnOpenInvite) btnOpenInvite.addEventListener('click', startEnvelopeOpening);
    if (waxSealBtn) waxSealBtn.addEventListener('click', startEnvelopeOpening);
    if (btnSkipAnimation) btnSkipAnimation.addEventListener('click', finishOpeningSequence);

    initAudio();
    initAmbientCanvas();
    initCountdown();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
