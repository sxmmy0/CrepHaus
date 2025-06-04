# 👟 Crep Haus

**Crep Haus** is a full-stack e-commerce web application built for sneaker enthusiasts. It allows users to browse, select, and “buy” their favourite trainers from a range of styles and categories. Designed with a clean UI and user-first experience, this project showcases dynamic cart functionality, user authentication, and a responsive layout.

---

## 📦 Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Database:** SQLite (default Django setup)
- **Tools:** Docker (in progress)

---

## 🔑 Key Features

- 🧾 **User Authentication**: Register, log in, and manage accounts securely
- 🛒 **Shopping Cart**: Add items, adjust quantities, remove products
- 🔎 **Product Browsing**: Explore a curated list of sneaker styles
- 💳 **Checkout Process**: Input payment and delivery details to simulate order placement

---

## 🚀 Live Demo

🔗 [GitHub-hosted Screenshot or Demo](https://github.com/user-attachments/assets/7e8a6318-1c92-4a20-9229-007ef2c7f90a)

> *Note: Live deployment coming soon – Docker setup in progress.*

---

## 🛠️ Installation Instructions

### 1. Clone the repository
```bash
git clone https://github.com/sxmmy0/CrepHaus
cd CrepHaus
```
### 2. (Optional) Create a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```
### 5. Run Server
```
python manage.py runserver
```
