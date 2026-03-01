# Blog

This is multi-author blogging platform built with Django and styled using Tailwind CSS + DaisyUI.  
It provides a public-facing blog and a private dashboard for content management.

## 📸 Screenshots

<img src="https://i.ibb.co/C5801w97/Screenshot-2026-03-01-212142.png" />
<img src="https://i.ibb.co/9mJ2R0xp/Screenshot-2026-03-01-212206.png" />
<img src="https://i.ibb.co/zVF6qqT8/Screenshot-2026-03-01-212213.png" />
<img src="https://i.ibb.co/Mxxt1FX1/Screenshot-2026-03-01-212222.png" />
<img src="https://i.ibb.co/B5f1Wk99/Screenshot-2026-03-01-212238.png" />
<img src="https://i.ibb.co/GQ5tDrmv/Screenshot-2026-03-01-212310.png" />
<img src="https://i.ibb.co/bgZWBCpt/Screenshot-2026-03-01-212342.png" />
<img src="https://i.ibb.co/wFkHKcJb/Screenshot-2026-03-01-212348.png" />
<img src="https://i.ibb.co/SqgSfKM/Screenshot-2026-03-01-212401.png" />
<img src="https://i.ibb.co/Myt8yJRD/Screenshot-2026-03-01-212408.png" />
<img src="https://i.ibb.co/VpCH2dn3/Screenshot-2026-03-01-212415.png" />

## 🚀 Features

### Public Side
- Homepage listing posts
- Single post page with rich text content
- Category-based filtering
- Author pages
- Authors listing page
- Categories listing page

### Authentication
- User registration
- Login / Logout
- Profile page
- Django messages integration for feedback

### Dashboard (CMS)
- Create post with CKEditor
- Select categories via styled checkboxes
- Publish posts
- Delete posts
- Posts management table
- Profile access

---

## 🛠 Tech Stack

- **Backend:** Django
- **Frontend:** Tailwind CSS, DaisyUI
- **Rich Text Editor:** CKEditor
- **Icons:** Font Awesome
- **Database:** SQLite (default, configurable)

---
## Users → Authors → Posts → Categories

- Custom `Author` model linked to Django `User`
- Slug-based routing
- Template inheritance
- Modular dashboard layout

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/sojwal-patil/Blog
cd blog
```

## Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

## Install dependencies

```bash 
pip install -r requirements.txt
```

## Run migrations

```bash
python manage.py migrate
```

## Create Super User

```bash
python manage.py createsuperuser 
```

## Run developmental server
```bash
python manage.py createsuperuser
```
