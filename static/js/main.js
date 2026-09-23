/**
 * Rastogi Traders - Interactive Scripts
 * Mobile Navigation, Live Status, Lightbox & Search Filter
 */

document.addEventListener('DOMContentLoaded', () => {
  initMobileDrawer();
  initLiveShopStatus();
  initGalleryLightbox();
  initLiveProductFilter();
});

/**
 * 1. Mobile Drawer Navigation Toggle
 */
function initMobileDrawer() {
  const menuBtn = document.getElementById('mobile-menu-toggle');
  const drawer = document.getElementById('mobile-drawer');
  const overlay = document.getElementById('mobile-drawer-overlay');
  const closeBtn = document.getElementById('drawer-close-btn');

  if (!menuBtn || !drawer || !overlay) return;

  function openDrawer() {
    drawer.classList.add('active');
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    drawer.classList.remove('active');
    overlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  menuBtn.addEventListener('click', openDrawer);
  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
  overlay.addEventListener('click', closeDrawer);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('active')) {
      closeDrawer();
    }
  });
}

/**
 * 2. Live Shop Status Indicator
 * Calculates whether the physical shop is open based on IST (Asia/Kolkata)
 */
function initLiveShopStatus() {
  const statusEl = document.getElementById('live-shop-status');
  if (!statusEl) return;

  try {
    const now = new Date();
    // Convert to IST offset UTC+5:30
    const utc = now.getTime() + (now.getTimezoneOffset() * 60000);
    const istDate = new Date(utc + (3600000 * 5.5));

    const day = istDate.getDay(); // 0 = Sunday, 1 = Monday...
    const hours = istDate.getHours();
    const minutes = istDate.getMinutes();
    const timeDec = hours + (minutes / 60);

    let isOpen = false;

    if (day >= 1 && day <= 6) {
      // Monday - Saturday: 8:00 AM to 8:00 PM
      if (timeDec >= 8.0 && timeDec <= 20.0) {
        isOpen = true;
      }
    } else if (day === 0) {
      // Sunday: 9:00 AM to 2:00 PM
      if (timeDec >= 9.0 && timeDec <= 14.0) {
        isOpen = true;
      }
    }

    if (isOpen) {
      statusEl.innerHTML = '<span class="status-dot"></span> दुकान अभी खुली है (Shop Open)';
      statusEl.style.color = '#86efac';
    } else {
      statusEl.innerHTML = '<span class="status-dot" style="background-color: #fca5a5;"></span> दुकान बंद है (कल सुबह 8:00 बजे खुलेगी)';
      statusEl.style.color = '#fca5a5';
    }
  } catch (e) {
    // Fallback default
    statusEl.innerHTML = '<span class="status-dot"></span> सेवा में तत्पर • सुबह 8:00 से शाम 8:00';
  }
}

/**
 * 3. Gallery Lightbox Preview
 */
function initGalleryLightbox() {
  const galleryItems = document.querySelectorAll('.gallery-item');
  if (!galleryItems.length) return;

  let modal = document.getElementById('gallery-lightbox-modal');
  if (!modal) {
    modal = document.createElement('div');
    modal.id = 'gallery-lightbox-modal';
    modal.style.cssText = `
      position: fixed; top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(0,0,0,0.85); z-index: 2100; display: none;
      align-items: center; justify-content: center; padding: 20px;
      cursor: zoom-out;
    `;
    modal.innerHTML = `
      <div style="position: relative; max-width: 900px; max-height: 90vh; text-align: center;">
        <img id="lightbox-img" src="" style="max-width: 100%; max-height: 80vh; border-radius: 12px; box-shadow: 0 10px 40px rgba(0,0,0,0.5); object-fit: contain; margin: 0 auto;" />
        <p id="lightbox-caption" style="color: #fff; font-size: 1.1rem; font-weight: 700; margin-top: 12px;"></p>
        <button id="lightbox-close" style="position: absolute; top: -40px; right: 0; background: none; border: none; color: #fff; font-size: 2rem; cursor: pointer;">✕</button>
      </div>
    `;
    document.body.appendChild(modal);

    modal.addEventListener('click', (e) => {
      if (e.target.id !== 'lightbox-img') {
        modal.style.display = 'none';
      }
    });

    const closeBtn = document.getElementById('lightbox-close');
    if (closeBtn) {
      closeBtn.addEventListener('click', () => { modal.style.display = 'none'; });
    }
  }

  const lightboxImg = document.getElementById('lightbox-img');
  const lightboxCaption = document.getElementById('lightbox-caption');

  galleryItems.forEach(item => {
    item.addEventListener('click', () => {
      const img = item.querySelector('img');
      const caption = item.getAttribute('data-caption') || item.querySelector('.gallery-overlay')?.innerText || '';
      if (img && lightboxImg) {
        lightboxImg.src = img.src;
        if (lightboxCaption) lightboxCaption.innerText = caption;
        modal.style.display = 'flex';
      }
    });
  });
}

/**
 * 4. Client-side Live Product Filter Debounce
 */
function initLiveProductFilter() {
  const searchInput = document.getElementById('live-search-input');
  if (!searchInput) return;

  let debounceTimer;
  searchInput.addEventListener('input', (e) => {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
      const query = e.target.value.toLowerCase().trim();
      const productCards = document.querySelectorAll('.product-card-item');

      if (!productCards.length) return;

      productCards.forEach(card => {
        const title = card.getAttribute('data-title')?.toLowerCase() || '';
        const brand = card.getAttribute('data-brand')?.toLowerCase() || '';
        const category = card.getAttribute('data-category')?.toLowerCase() || '';

        if (!query || title.includes(query) || brand.includes(query) || category.includes(query)) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    }, 200);
  });
}
