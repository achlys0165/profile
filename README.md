# Personal Portfolio Website

A modern, responsive portfolio website built with Vue.js 3, featuring a dark cybersecurity-themed design, guestbook functionality, and contact form integration.

![Portfolio Screenshot](image.png)

## 🚀 Live Demo
- **Frontend:** [https://jan-sultan.vercel.app](https://jan-sultan.vercel.app)
- **Backend API:** [https://my-profile-1-js57.onrender.com/api/health](https://my-profile-1-js57.onrender.com/api/health)

---

## 📋 Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Deployment](#deployment)
- [API Documentation](#api-documentation)
- [Database Schema](#database-schema)
- [Customization](#customization)
- [License](#license)

---

## ✨ Features

### Frontend
- **Responsive Design** - Optimized for desktop, tablet, and mobile devices
- **Dark Theme** - Cybersecurity-inspired color palette with pink accents
- **Custom Cursor** - Animated cursor with hover effects
- **Scroll Animations** - Reveal animations on scroll
- **Guestbook** - Visitor message board with real-time updates
- **Contact Form** - Direct message functionality
- **Project Showcase** - Dynamic project cards with GitHub links

### Backend
- **REST API** - Flask-based API with CORS support
- **Database Integration** - Supabase PostgreSQL for data persistence
- **Guestbook Endpoints** - GET/POST for visitor entries
- **Contact Form Handling** - Store contact messages
- **Health Check** - API status monitoring

---

## 🛠 Tech Stack

### Frontend
| Technology | Purpose |
|------------|---------|
| Vue.js 3 | Frontend framework |
| Vite | Build tool & dev server |
| CSS3 | Styling with CSS variables |
| Intersection Observer | Scroll animations |

### Backend
| Technology | Purpose |
|------------|---------|
| Python 3.11 | Programming language |
| Flask | Web framework |
| Requests | HTTP library for Supabase |
| Gunicorn | WSGI HTTP server |

### Database & Hosting
| Service | Purpose |
|---------|---------|
| Supabase | PostgreSQL database |
| Vercel | Frontend hosting |
| Render | Backend hosting |

---

## 📁 Project Structure

```text
my-profile/
├── main/
│   ├── frontend/                 # Vue.js frontend
│   │   ├── src/
│   │   │   ├── components/       # Reusable components
│   │   │   │   ├── CustomCursor.vue
│   │   │   │   ├── BackgroundEffects.vue
│   │   │   │   ├── NavBar.vue
│   │   │   │   └── RuleDivider.vue
│   │   │   ├── sections/         # Page sections
│   │   │   │   ├── HeroSection.vue
│   │   │   │   ├── AboutSection.vue
│   │   │   │   ├── PhotoUpload.vue
│   │   │   │   ├── InterestsBlock.vue
│   │   │   │   ├── SkillsSection.vue
│   │   │   │   ├── SkillRow.vue
│   │   │   │   ├── ProjectsSection.vue
│   │   │   │   ├── ProjectCard.vue
│   │   │   │   ├── CertificatesSection.vue
│   │   │   │   ├── CertificateCard.vue
│   │   │   │   ├── GuestbookSection.vue
│   │   │   │   ├── GuestbookEntry.vue
│   │   │   │   ├── ContactSection.vue
│   │   │   │   ├── ContactLink.vue
│   │   │   │   └── FooterSection.vue
│   │   │   ├── services/
│   │   │   │   └── api.js        # API service layer
│   │   │   ├── directives/
│   │   │   │   └── reveal.js     # Scroll reveal directive
│   │   │   ├── App.vue           # Root component
│   │   │   └── main.js           # Entry point
│   │   ├── index.html
│   │   ├── package.json
│   │   └── vite.config.js
│   │
│   └── backend/                  # Flask backend
│       ├── app.py                # Main application
│       ├── requirements.txt      # Python dependencies
│       └── Procfile              # Render deployment config
│
├── README.md                     # This file
└── .gitignore

```

---

## 🚦 Getting Started

### Prerequisites
- Node.js 18+ 
- Python 3.11+
- Git

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/my-profile.git](https://github.com/yourusername/my-profile.git)
cd my-profile/main
```

### 2. Setup Frontend

```bash
cd frontend
npm install
```

Create `.env.local`:
```env
VITE_API_URL=http://localhost:5000
```

Start development server:
```bash
npm run dev
```

### 3. Setup Backend

```bash
cd ../backend
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

Create `.env`:
```env
SUPABASE_URL=[https://your-project.supabase.co](https://your-project.supabase.co)
SUPABASE_SERVICE_KEY=your-service-role-key
```

Start Flask server:
```bash
python app.py
```

---

## 🔐 Environment Variables

### Frontend (Vercel)
| Variable | Description | Example |
|---|---|---|
| `VITE_API_URL` | Backend API URL | `https://api.example.com` |

### Backend (Render)
| Variable | Description | Example |
|---|---|---|
| `SUPABASE_URL` | Supabase project URL | `https://abc123.supabase.co` |
| `SUPABASE_SERVICE_KEY` | Supabase service role key | `eyJhbG...` |

---

## 🚀 Deployment

### Frontend (Vercel)
1. Push code to GitHub
2. Connect repository to Vercel
3. Set environment variable `VITE_API_URL`
4. Deploy

```bash
# Using Vercel CLI
npm i -g vercel
vercel --prod
```

### Backend (Render)
1. Push code to GitHub
2. Create new Web Service on Render
3. Configure:
   - **Root Directory:** `main/backend`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app --bind 0.0.0.0:$PORT`
4. Add environment variables
5. Deploy

### Database (Supabase)
1. Create project on Supabase
2. Run SQL schema in SQL Editor:

```sql
create table guestbook (
    id uuid default gen_random_uuid() primary key,
    name text not null,
    message text not null,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

alter table guestbook enable row level security;
alter table contacts enable row level security;

create policy "Public can read guestbook" on guestbook for select using (true);
create policy "Public can insert guestbook" on guestbook for insert with check (true);
```

---

## 📡 API Documentation

**Base URL:** `https://your-render-app.onrender.com/api`

### Endpoints

#### `GET /api/health`
Check API status.

**Response:**
```json
{
  "status": "ok"
}
```

#### `GET /api/guestbook`
Retrieve all guestbook entries (newest first).
**Response:**
```json
{
  "success": true,
  "data": [
    {
      "id": "uuid",
      "name": "John Doe",
      "message": "Great portfolio!",
      "created_at": "2024-01-15T10:30:00Z"
    }
  ]
}
```

#### `POST /api/guestbook`
Create new guestbook entry.

**Request Body:**
```json
{
  "name": "John Doe",
  "message": "Your message here"
}
```

*Validation: `name` (required, max 40 chars), `message` (required, max 280 chars)*

#### `POST /api/contact`
Submit contact form.

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "message": "Your message"
}
```

*Validation: `name` (required), `email` (required, must contain @)*

---

---

## 🗄 Database Schema

### guestbook
| Column | Type | Description |
|---|---|---|
| id | uuid | Primary key, auto-generated |
| name | text | Visitor name |
| message | text | Visitor message |
| created_at | timestamptz | Auto-generated timestamp |

### contacts
| Column | Type | Description |
|---|---|---|
| id | uuid | Primary key, auto-generated |
| name | text | Sender name |
| email | text | Sender email |
| message | text | Message content |
| created_at | timestamptz | Auto-generated timestamp |

---

## 🎨 Customization

### Colors
Edit CSS variables in `src/App.vue`:
```css
:root {
  --ink: #0e0c0f;       /* Background */
  --pink: #f4a7b9;      /* Primary accent */
  --pink-pale: #fce8ee; /* Secondary accent */
  --white: #fafaf9;     /* Text */
  --muted: #7a6d80;     /* Muted text */
}
```

---

### Projects
Edit `src/sections/ProjectsSection.vue`:
```javascript
const projects = ref([
  {
    name: 'Your Project',
    icon: '🚀',
    description: 'Your description',
    tags: ['Vue', 'Node'],
    size: 'proj-wide',
    github: '[https://github.com/username/repo](https://github.com/username/repo)'
  }
])
```

---

### Profile Info
Update in:
- `src/sections/AboutSection.vue` - Bio text
- `src/sections/PhotoUpload.vue` - Name and photo
- `src/sections/ContactSection.vue` - Links and email

---

## 📝 License
This project is open source and available under the MIT License.

## 👤 Author
**Jan Sultan**
- GitHub: [@jan-sultan](https://github.com/achlys0165)
- LinkedIn: [linkedin.com/in/jan-sultan](https://www.linkedin.com/in/jansultan0210)
- TryHackMe: [tryhackme.com](https://tryhackme.com/p/jgsultan)

## 🙏 Acknowledgments
- Design inspired by cybersecurity aesthetics
- Fonts: Playfair Display, DM Mono, Instrument Sans (Google Fonts)
- Icons: Unicode emoji set


