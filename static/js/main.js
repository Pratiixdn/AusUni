/* ═══════════════════════════════════════════════════════════
   AusUni – Main JavaScript
   Dark Mode | Autocomplete | Bookmarks | Compare | Misc
   ═══════════════════════════════════════════════════════════ */

'use strict';

// ── Theme (Dark / Light Mode) ─────────────────────────────
const themeToggle = document.getElementById('themeToggle');
const themeIcon   = document.getElementById('themeIcon');
const html        = document.documentElement;

function applyTheme(theme) {
    html.setAttribute('data-theme', theme);
    localStorage.setItem('ausuni-theme', theme);
    if (themeIcon) {
        themeIcon.className = theme === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-fill';
    }
}

// Load saved theme or system preference
(function initTheme() {
    const saved = localStorage.getItem('ausuni-theme');
    if (saved) {
        applyTheme(saved);
    } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
        applyTheme('dark');
    }
})();

if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        const current = html.getAttribute('data-theme') || 'light';
        applyTheme(current === 'dark' ? 'light' : 'dark');
    });
}

// ── Search Autocomplete ───────────────────────────────────
(function initAutocomplete() {
    const input   = document.getElementById('navSearchInput');
    const results = document.getElementById('searchAutocomplete');
    if (!input || !results) return;

    let debounceTimer;

    input.addEventListener('input', () => {
        clearTimeout(debounceTimer);
        const q = input.value.trim();
        if (q.length < 2) { results.style.display = 'none'; return; }

        debounceTimer = setTimeout(async () => {
            try {
                const res  = await fetch(`/api/search/autocomplete/?q=${encodeURIComponent(q)}`);
                const data = await res.json();
                renderAutocomplete(data.results);
            } catch (e) { results.style.display = 'none'; }
        }, 200);
    });

    function renderAutocomplete(items) {
        if (!items.length) { results.style.display = 'none'; return; }
        results.innerHTML = items.map(item => `
            <a class="autocomplete-item" href="${item.url}">
                <span class="autocomplete-type">${item.type}</span>
                ${escHtml(item.label)}
            </a>
        `).join('');
        results.style.display = 'block';
    }

    // Close on outside click
    document.addEventListener('click', e => {
        if (!input.contains(e.target) && !results.contains(e.target)) {
            results.style.display = 'none';
        }
    });

    // Keyboard navigation
    input.addEventListener('keydown', e => {
        const items = results.querySelectorAll('.autocomplete-item');
        const focused = results.querySelector('.autocomplete-item:focus');
        if (e.key === 'ArrowDown') {
            e.preventDefault();
            if (focused) { const next = focused.nextElementSibling; if (next) next.focus(); }
            else if (items[0]) items[0].focus();
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            if (focused) { const prev = focused.previousElementSibling; if (prev) prev.focus(); else input.focus(); }
        } else if (e.key === 'Escape') {
            results.style.display = 'none';
            input.blur();
        }
    });
})();

// ── Hero Search (on home page) ────────────────────────────
(function initHeroSearch() {
    const heroInput = document.getElementById('heroSearchInput');
    if (!heroInput) return;
    heroInput.addEventListener('keydown', e => {
        if (e.key === 'Enter') {
            const q = heroInput.value.trim();
            if (q) window.location.href = `/search/?q=${encodeURIComponent(q)}`;
        }
    });
})();

// ── Bookmark Toggle (AJAX) ────────────────────────────────
document.querySelectorAll('.btn-bookmark').forEach(btn => {
    btn.addEventListener('click', async e => {
        e.preventDefault();
        const url  = btn.dataset.url;
        const icon = btn.querySelector('i');
        try {
            const res  = await fetch(url, {
                method: 'GET',
                headers: { 'X-Requested-With': 'XMLHttpRequest' }
            });
            const data = await res.json();
            if (data.action === 'added') {
                btn.classList.add('active');
                if (icon) icon.className = 'bi bi-bookmark-heart-fill';
                btn.title = 'Remove bookmark';
                showToast('Bookmarked!', 'success');
            } else {
                btn.classList.remove('active');
                if (icon) icon.className = 'bi bi-bookmark-heart';
                btn.title = 'Bookmark this university';
                showToast('Bookmark removed', 'info');
            }
        } catch (err) {
            showToast('Something went wrong', 'error');
        }
    });
});

// ── Compare Selector ─────────────────────────────────────
(function initCompare() {
    const compareCheckboxes = document.querySelectorAll('.compare-checkbox');
    const compareBar        = document.getElementById('compareBar');
    const compareBtn        = document.getElementById('compareBtn');
    const compareCount      = document.getElementById('compareCount');
    const selected          = new Set();

    if (!compareCheckboxes.length) return;

    compareCheckboxes.forEach(cb => {
        cb.addEventListener('change', () => {
            const slug = cb.dataset.slug;
            if (cb.checked) {
                if (selected.size >= 3) {
                    cb.checked = false;
                    showToast('You can compare up to 3 universities', 'warning');
                    return;
                }
                selected.add(slug);
            } else {
                selected.delete(slug);
            }
            updateCompareBar();
        });
    });

    function updateCompareBar() {
        if (!compareBar) return;
        if (selected.size >= 2) {
            compareBar.classList.remove('d-none');
            if (compareCount) compareCount.textContent = selected.size;
        } else {
            compareBar.classList.add('d-none');
        }
        if (compareBtn) {
            const params = Array.from(selected).map(s => `uni=${s}`).join('&');
            compareBtn.href = `/compare/?${params}`;
        }
    }
})();

// ── Filter Form Auto-Submit ───────────────────────────────
document.querySelectorAll('.filter-auto-submit').forEach(select => {
    select.addEventListener('change', () => {
        select.closest('form').submit();
    });
});

// ── Sticky Navbar Shadow on Scroll ───────────────────────
(function initNavScroll() {
    const nav = document.getElementById('mainNav');
    if (!nav) return;
    window.addEventListener('scroll', () => {
        nav.style.boxShadow = window.scrollY > 10
            ? '0 2px 20px rgba(0,0,0,0.12)'
            : '';
    }, { passive: true });
})();

// ── Smooth Scroll for Anchor Links ───────────────────────
document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
        const target = document.querySelector(a.getAttribute('href'));
        if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// ── Copy to Clipboard ────────────────────────────────────
document.querySelectorAll('[data-copy]').forEach(btn => {
    btn.addEventListener('click', () => {
        navigator.clipboard.writeText(btn.dataset.copy).then(() => {
            showToast('Copied!', 'success');
        });
    });
});

// ── Toast Notifications ──────────────────────────────────
function showToast(msg, type = 'info') {
    const colours = {
        success: '#0da271',
        info:    '#1a6ef8',
        warning: '#f5a623',
        error:   '#e53e3e',
    };
    const toast = document.createElement('div');
    toast.style.cssText = `
        position: fixed; bottom: 1.5rem; right: 1.5rem; z-index: 99999;
        background: ${colours[type] || colours.info};
        color: white; padding: 0.75rem 1.25rem;
        border-radius: 10px; font-size: 0.875rem; font-weight: 600;
        font-family: 'Sora', sans-serif;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        display: flex; align-items: center; gap: 0.5rem;
        animation: toastIn 0.3s ease;
        max-width: 320px;
    `;
    toast.textContent = msg;
    document.body.appendChild(toast);
    setTimeout(() => { toast.style.animation = 'toastOut 0.3s ease forwards'; setTimeout(() => toast.remove(), 300); }, 2500);
}

// Toast animations (injected once)
if (!document.getElementById('toast-styles')) {
    const style = document.createElement('style');
    style.id = 'toast-styles';
    style.textContent = `
        @keyframes toastIn  { from { opacity: 0; transform: translateY(16px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes toastOut { to   { opacity: 0; transform: translateY(16px); } }
    `;
    document.head.appendChild(style);
}

// ── Animated Count-Up for Stats ──────────────────────────
(function initCountUp() {
    const counters = document.querySelectorAll('[data-count]');
    if (!counters.length) return;

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            const el  = entry.target;
            const end = parseInt(el.dataset.count, 10);
            let start = 0;
            const dur = 1200;
            const step = end / (dur / 16);
            const timer = setInterval(() => {
                start += step;
                if (start >= end) { el.textContent = end.toLocaleString(); clearInterval(timer); }
                else el.textContent = Math.floor(start).toLocaleString();
            }, 16);
            observer.unobserve(el);
        });
    }, { threshold: 0.3 });

    counters.forEach(el => observer.observe(el));
})();

// ── Utility: HTML Escape ─────────────────────────────────
function escHtml(str) {
    return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;');
}
