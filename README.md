# Rastogi Traders (रस्तोगी ट्रेडर्स) — Rural Agricultural Business Website

[![Django](https://img.shields.io/badge/Django-5.x%20%2F%206.x-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)]()
[![Target Audience](https://img.shields.io/badge/Audience-Rural%20India%20Farmers-orange.svg)]()

> **"स्थानीय दुकान + आधुनिक सुविधा + भरोसेमंद सेवा"**
> A production-ready, trust-first, mobile-optimized agricultural web platform built for North Indian farmers, dairy livestock owners, and rural customers.

---

## 🌟 Key Features

### 1. 🌾 Authentic Hindi-First Design & Natural Devanagari Copy
- Crafted specifically for North Indian farmers with authentic agricultural terminology (*उर्वरक, खाद, कीटनाशक, फसल सुरक्षा, पशु आहार, आज का भाव पूछें, दुकान तक पहुँचें*).
- Typography optimized for high legibility using **Noto Sans Devanagari** and **Hind**.

### 2. 📲 Instant WhatsApp-First Customer Service
- Pre-filled Devanagari WhatsApp inquiry URLs for every product, offer, and crop guide.
- Example message: `नमस्ते, मुझे Rastogi Traders से '[PRODUCT NAME] ([BRAND])' की कीमत और उपलब्धता के बारे में जानकारी चाहिए।`
- Persistent floating WhatsApp button and sticky mobile bottom navigation bar.

### 3. 📞 One-Tap Direct Calling & Store Navigation
- Prominent `tel:` dialer buttons with minimum 48px touch targets.
- Embedded Google Maps and one-tap directions link for local store discovery.

### 4. 🛒 Agricultural Product Catalogue
- Browse Fertilizers (उर्वरक), Pesticides (कीटनाशक), Cattle Feed (पशु आहार), and Seeds (उन्नत बीज).
- Live stock availability indicators (*दुकान पर उपलब्ध, सीमित स्टॉक, ऑर्डर पर उपलब्ध*).
- Instant client-side debounced search and category filter pills.
- Agricultural safety disclaimer on every chemical product.

### 5. 👨‍🌾 Farmer Corner (किसान कॉर्नर)
- Stage-wise agronomy guides for prominent Indian crops: **गेहूँ (Wheat), धान (Paddy), गन्ना (Sugarcane), सरसों (Mustard), आलू (Potato), मक्का (Maize)**.
- Balanced fertilizer schedules (बेसल डोज, पहली सिंचाई, टॉप ड्रेसिंग) and pest management tips.

### 6. 🔥 Seasonal Offers & Verified Customer Reviews
- Manage seasonal combo discounts, bundle deals, and valid dates in Django Admin.
- Real farmer testimonials from surrounding villages with 5-star ratings.

### 7. 📸 Shop & Stock Photo Gallery
- Responsive interactive gallery with category filter pills and image lightbox preview.

### 8. 🛡️ 100% Non-Hardcoded Django Admin Experience
- Business owners can modify phone numbers, WhatsApp numbers, shop address, opening hours, Google Maps links, hero subtitles, trust points, and story directly from Django Admin without writing code.

---

## 🛠️ Technology Stack

- **Backend**: Python 3.12+, Django 5.x / 6.x
- **Database**: SQLite (Local development) / PostgreSQL ready via `dj-database-url`
- **Frontend**: Semantic HTML5, Vanilla CSS3 (Custom Agricultural Design System Tokens), Vanilla JavaScript (no heavy node runtime needed)
- **Image Processing**: Pillow
- **Environment Management**: `python-dotenv`

---

## 🚀 Quick Start & Local Setup

### 1. Clone the repository & Navigate
```bash
cd Rastogi_Traders_Website
```

### 2. Create and activate a virtual environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy `.env.example` to `.env`:
```bash
# Windows PowerShell
copy .env.example .env

# Linux / macOS
cp .env.example .env
```

### 5. Run Database Migrations
```bash
python manage.py migrate
```

### 6. Populate Realistic Indian Agricultural Seed Data
Populates categories (Fertilizers, Pesticides, Cattle Feed, Seeds), products (IFFCO DAP, Urea, Coragen, Confidor, Godrej Cattle Feed), crop guides, agronomy tips, offers, reviews, and store details:
```bash
python populate_data.py
```

### 7. Create Superuser (Admin)
You can run our automated helper script or create a custom superuser:
```bash
python create_superuser.py
# Default credentials created:
# Username: admin
# Password: adminpassword123
```
*Or manually:*
```bash
python manage.py createsuperuser
```

### 8. Start the Development Server
```bash
python manage.py runserver
```

Open your browser and visit:
- **Website**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## ⚙️ Environment Variables

| Variable | Description | Default (Local) |
|---|---|---|
| `SECRET_KEY` | Django Secret Key | Dev Key |
| `DEBUG` | Debug mode (`True` / `False`) | `True` |
| `ALLOWED_HOSTS` | Comma-separated allowed hostnames | `localhost,127.0.0.1` |
| `DATABASE_URL` | PostgreSQL connection string (Optional) | SQLite local file |
| `BUSINESS_PHONE` | Default business telephone | `+919876543210` |
| `WHATSAPP_NUMBER` | Default business WhatsApp | `+919876543210` |
| `GOOGLE_MAPS_URL` | Default Google Maps link | Maps URL |

---

## 📋 Django Admin Content Management Guide

The Django Admin panel (`/admin/`) has been customized with simple Hindi & English labels:

1. **दुकान की जानकारी (Business Profile)**:
   - Edit store name, primary & secondary phone numbers, WhatsApp number.
   - Update address, landmark, opening hours, and Sunday timings.
   - Update Google Maps embed iframe and directions URL.
   - Update hero section titles and trust bullet points.
2. **उत्पाद प्रबंधन (Products & Categories)**:
   - Add/edit products, assign categories, upload photos.
   - Toggle availability status (*In Stock / Limited Stock / Out of Stock*).
   - Flag products as featured on the homepage.
3. **आज के खास ऑफर (Offers)**:
   - Create seasonal discount banners with validity dates.
4. **किसान कॉर्नर (Crop Guides & Farmer Tips)**:
   - Publish crop advisories with fertilizer schedules and pest protection tips.
5. **ग्राहकों की राय (Customer Reviews)**:
   - Review and approve local farmer feedback.
6. **वेबसाइट पूछताछ संदेश (Contact Enquiries)**:
   - View customer inquiries submitted through the contact forms.

---

## 🧪 Running Automated Tests

Run the full Django test suite (15 unit tests covering views, search, forms, sitemaps, robots.txt):
```bash
python manage.py test
```

---

## 🚢 Production Deployment Guide (Render, Railway, VPS)

### 1. Cloud Deployment (Render / Railway / Heroku)
The repository includes a ready-to-use `Procfile` and `render.yaml`.

#### Option A: Deploy on Render (Recommended)
1. Push code to your GitHub/GitLab repository.
2. Sign in to [Render.com](https://render.com) and click **New > Blueprint**.
3. Select this repository. Render will automatically read `render.yaml`, set up Python 3.12, run migrations, collect static files with WhiteNoise, and launch Gunicorn.
4. In Render Dashboard, set your environment variables:
   - `DEBUG=False`
   - `ALLOWED_HOSTS=your-app.onrender.com,rastogitraders.com`
   - `CSRF_TRUSTED_ORIGINS=https://your-app.onrender.com,https://rastogitraders.com`
   - `CSRF_COOKIE_SECURE=True`
   - `SESSION_COOKIE_SECURE=True`

#### Option B: Deploy on Ubuntu Linux VPS (Nginx + Gunicorn + Systemd)
```bash
# Clone and setup virtual environment
git clone <repo-url> rastogi_traders
cd rastogi_traders
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure environment
cp .env.production.example .env
nano .env  # Update SECRET_KEY, ALLOWED_HOSTS, and CSRF_TRUSTED_ORIGINS

# Migrate and collect static
python manage.py migrate
python manage.py collectstatic --noinput

# Start Gunicorn service via systemd
sudo systemctl enable --now gunicorn
```

---

## 🌐 Custom Domain & Cloudflare SSL Setup

1. **Purchase Domain**: Register your domain (e.g. `rastogitraders.in` or `rastogitraders.com`) via Namecheap, GoDaddy, or Hostinger.
2. **Add to Cloudflare (Free)**:
   - Create a free account on [Cloudflare](https://www.cloudflare.com).
   - Change your domain nameservers at your registrar to Cloudflare's nameservers.
3. **Configure DNS Records**:
   - Add a `CNAME` record for `@` pointing to your Render app (`your-app.onrender.com`) or `A` record pointing to your VPS IP.
   - Add a `CNAME` record for `www` pointing to `@`.
4. **Enable SSL/TLS**:
   - In Cloudflare SSL/TLS tab, set encryption mode to **Full** or **Full (strict)**.
   - Enable **Always Use HTTPS** and **Automatic HTTPS Rewrites**.

---

## 🔍 Google Search Console & Local SEO (Google Business Profile)

### 1. Google Search Console Verification
1. Visit [Google Search Console](https://search.google.com/search-console).
2. Add Property with your live domain: `https://rastogitraders.com`.
3. Submit your XML Sitemap:
   ```
   https://rastogitraders.com/sitemap.xml
   ```
4. Verify that `/robots.txt` is accessible and points to `sitemap.xml`.

### 2. Google Business Profile (Google Maps)
1. Go to [Google Business Profile](https://www.google.com/business/).
2. Register **रस्तोगी ट्रेडर्स (Rastogi Traders)** under category **Agricultural Service / Fertilizer Supplier / Animal Feed Store**.
3. Add exact physical shop address, pin location on Google Maps, and store opening hours (e.g. 08:00 AM - 08:00 PM).
4. Add the website link `https://rastogitraders.com` and primary contact phone number.
5. Upload storefront photos, stock arrival photos, and store signboards.


---

## 📄 License & Ownership

© 2026 **Rastogi Traders**. सर्वाधिकार सुरक्षित।
Designed & developed as a rural-focused agricultural business digital platform.
