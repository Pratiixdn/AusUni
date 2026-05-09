# 🎓 AusUni – Australian University Portal

**A production-ready Django web application helping international students explore Australian universities, courses, tuition fees, scholarships, and admission requirements.**

---

## 📁 Project Structure

```
ausuni/
├── ausuni/                    # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── universities/              # Main Django app
│   ├── models.py              # Full database schema
│   ├── views.py               # All views
│   ├── urls.py                # URL patterns
│   ├── admin.py               # Admin configuration
│   ├── context_processors.py
│   ├── sitemaps.py            # SEO sitemaps
│   └── management/commands/
│       └── seed_universities.py  # Data seeding command
├── data/universities/         # University data files
│   ├── university_of_canberra.py
│   ├── university_of_sydney.py
│   ├── monash_university.py
│   ├── unsw_sydney.py
│   ├── australian_national_university.py
│   ├── university_of_melbourne.py
│   └── qut_and_rmit.py        # QUT + RMIT combined
├── templates/
│   ├── base.html              # Base template (dark/light mode)
│   ├── universities/
│   │   ├── home.html
│   │   ├── university_list.html
│   │   ├── university_detail.html
│   │   ├── course_list.html
│   │   ├── scholarship_list.html
│   │   ├── search_results.html
│   │   └── state_detail.html
│   └── pages/
│       ├── about.html
│       ├── privacy_policy.html
│       ├── contact.html
│       └── disclaimer.html
├── static/
│   ├── css/main.css           # Full design system
│   └── js/main.js             # Dark mode, autocomplete, bookmarks
├── manage.py
└── requirements.txt
```

---

## ⚡ Quick Setup (Local Development)

### 1. Clone / Extract the Project
```bash
cd ~/projects
# Extract the provided zip or clone your repo
cd ausuni
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py makemigrations universities
python manage.py migrate
```

### 5. Seed the Database
```bash
python manage.py seed_universities
```
This will create:
- All 8 Australian states and territories
- All major cities (Sydney, Melbourne, Brisbane, Perth, Adelaide, Canberra, etc.)
- 10+ universities with full data (USYD, UNSW, Monash, ANU, UniMelb, UC, QUT, RMIT, UQ, UWA, Curtin, UoA)
- 60+ courses with fees, IELTS requirements, career outcomes
- 30+ scholarships with coverage, eligibility, and links

### 6. Create Admin Superuser
```bash
python manage.py createsuperuser
```

### 7. Collect Static Files (for production) / Run Dev Server
```bash
# Development
python manage.py runserver

# Then open: http://127.0.0.1:8000/
# Admin:      http://127.0.0.1:8000/admin/
```

---

## 🗺️ URL Structure

| URL | View | Description |
|-----|------|-------------|
| `/` | `home` | Homepage with hero, states, featured unis |
| `/universities/` | `university_list` | Filterable list of all universities |
| `/universities/<slug>/` | `university_detail` | Full university page |
| `/universities/<uni>/courses/<course>/` | `course_detail` | Course detail page |
| `/courses/` | `course_list` | Smart course finder with filters |
| `/scholarships/` | `scholarship_list` | All scholarships |
| `/australia/<state>/` | `state_detail` | State overview |
| `/australia/<state>/<city>/` | `city_detail` | City universities |
| `/search/` | `search` | Full-text search |
| `/compare/` | `compare` | Side-by-side comparison |
| `/bookmarks/` | `bookmark_list` | Session bookmarks |
| `/about/` | `about` | About page |
| `/privacy-policy/` | `privacy_policy` | Privacy policy (AdSense) |
| `/contact/` | `contact` | Contact form |
| `/disclaimer/` | `disclaimer` | Disclaimer |
| `/sitemap.xml` | sitemap | SEO sitemap |
| `/admin/` | admin | Django admin |

---

## ✨ Features

### Core Features
- ✅ **State → City → University → Course → Scholarship** hierarchy
- ✅ **Smart search** with autocomplete (AJAX)
- ✅ **Advanced filters**: State, level, fee range, IELTS score, type
- ✅ **University comparison** (up to 3 at once)
- ✅ **Bookmarks** (session-based, no login required)
- ✅ **Dark mode / Light mode** toggle with system preference detection

### Universities Included
| University | State | Group | Ranking |
|-----------|-------|-------|---------|
| University of Sydney | NSW | Go8 | #18 World |
| UNSW Sydney | NSW | Go8 | #19 World |
| University of Melbourne | VIC | Go8 | #13 World |
| Monash University | VIC | Go8 | #37 World |
| Australian National University | ACT | Go8 | #30 World |
| University of Queensland | QLD | Go8 | #40 World |
| University of Western Australia | WA | Go8 | #72 World |
| University of Adelaide | SA | Go8 | #82 World |
| University of Canberra | ACT | — | QS 601–650 |
| QUT | QLD | ATN | QS 381–400 |
| RMIT University | VIC | ATN | QS 192 |
| Curtin University | WA | ATN | QS 185 |

### SEO & AdSense Ready
- ✅ Meta descriptions and titles per page
- ✅ XML Sitemap (`/sitemap.xml`)
- ✅ Privacy Policy page
- ✅ Disclaimer page
- ✅ About page
- ✅ Contact page
- ✅ Original, helpful content
- ✅ Fast loading (minimal dependencies)
- ✅ Mobile responsive

---

## ➕ Adding More Universities

Create a new file in `data/universities/`, e.g. `griffith_university.py`:

```python
UNIVERSITY = {
    "name": "Griffith University",
    "short_name": "Griffith",
    "type": "public",
    "group": "none",
    "state": "Queensland",
    "city": "Gold Coast",
    "official_website": "https://www.griffith.edu.au",
    # ... etc
}
CAMPUSES = [...]
COURSES = [...]
SCHOLARSHIPS = [...]
```

Then in `seed_universities.py`, import and add it to the seeding list.

---

## 🚀 Production Deployment

### Option A: DigitalOcean / Ubuntu VPS

```bash
# 1. Install system dependencies
sudo apt update
sudo apt install python3-pip python3-venv nginx postgresql

# 2. Setup PostgreSQL
sudo -u postgres createdb ausuni
sudo -u postgres createuser ausuni_user

# 3. Update settings.py
# Set DEBUG=False
# Set ALLOWED_HOSTS=['yourdomain.com']
# Switch to PostgreSQL database settings

# 4. Configure Gunicorn
gunicorn ausuni.wsgi:application --workers 3 --bind 0.0.0.0:8000

# 5. Configure Nginx as reverse proxy
# Point to Gunicorn socket

# 6. Collect static files
python manage.py collectstatic

# 7. Setup SSL with Certbot
sudo certbot --nginx -d yourdomain.com
```

### Option B: Railway / Render (Free Tier)

```bash
# railway.json or render.yaml
# Add: gunicorn ausuni.wsgi:application
# Set environment variables for SECRET_KEY, DATABASE_URL
# Add: python manage.py migrate && python manage.py seed_universities
```

### Option C: PythonAnywhere (Easy)

1. Upload project files
2. Create a virtual environment and install requirements
3. Set WSGI path to `ausuni.wsgi`
4. Run `python manage.py migrate && python manage.py seed_universities`

---

## 🔐 Environment Variables (Production)

Create a `.env` file (never commit this):

```
SECRET_KEY=your-very-long-random-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@host:5432/ausuni
```

---

## 🗃️ Database Models Summary

| Model | Key Fields |
|-------|-----------|
| `State` | name, slug, abbreviation, capital |
| `City` | name, state, cost_of_living |
| `University` | name, type, group, ranking_qs, official_website |
| `Campus` | university, city, is_main, facilities |
| `Course` | name, level, tuition_fee_annual, ielts_overall, official_url |
| `Scholarship` | name, coverage, coverage_percentage, deadline, official_url |
| `Bookmark` | session_key, university, course |

---

## 📊 Admin Panel

Access at `/admin/` with your superuser credentials.

Features:
- Inline campus/scholarship editing on University page
- List filters by state, type, group
- Search by name, city
- Toggle `is_featured` and `is_popular` inline
- Bulk actions

---

*AusUni – Not affiliated with any Australian university. Information is for guidance only.*

---

## 📊 Complete University Coverage (2026)

| State/Territory | Universities | Count |
|----------------|-------------|-------|
| **NSW** | USYD, UNSW, UTS, Macquarie, Newcastle, Wollongong, WSU, ACU, CSU, SCU, UNE, Avondale | 12 |
| **VIC** | UniMelb, Monash, RMIT, Swinburne, Deakin, La Trobe, VU, Federation, Divinity | 9 |
| **QLD** | UQ, QUT, Griffith, JCU, Bond, CQU, UniSQ, UniSC | 8 |
| **WA** | UWA, Curtin, ECU, Murdoch, Notre Dame | 5 |
| **SA** | Adelaide University *(merged 2026)*, Flinders, Torrens | 3 |
| **ACT** | ANU, UC | 2 |
| **NT** | CDU | 1 |
| **TAS** | UTAS | 1 |
| **Total** | All official Australian universities | **41** |

### Data Files
```
data/universities/
├── university_of_sydney.py          # USYD
├── unsw_sydney.py                   # UNSW
├── monash_university.py             # Monash
├── university_of_melbourne.py       # UniMelb
├── australian_national_university.py # ANU
├── university_of_canberra.py        # UC
├── qut_and_rmit.py                  # QUT + RMIT
├── nsw_universities.py              # UTS, Macquarie, Newcastle, UOW,
│                                    # WSU, ACU, CSU, SCU, UNE, Avondale
├── vic_universities.py              # Swinburne, Deakin, La Trobe, VU,
│                                    # Federation, University of Divinity
├── qld_universities.py              # UQ, Griffith, JCU, Bond, CQU,
│                                    # UniSQ, UniSC
└── wa_sa_nt_tas_universities.py     # UWA, Curtin, ECU, Murdoch, Notre Dame,
                                     # Adelaide Uni (merged), Flinders, Torrens,
                                     # CDU, UTAS
```
