---

````markdown
# 🏡 Rent Wise – House Catalog Web App

Rent Wise is a modern and responsive house catalog web application built with **Django** and **Tailwind CSS**. It allows users to browse, list, and manage rental properties easily.

---

## 🔧 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Tailwind CSS
- **Auth:** Custom Django app (`accounts`)
- **Listings:** Managed by the `properties` app
- **Styling Tooling:** Tailwind CSS via npm
- **Environment Management:** `.env` support

---

## ✨ Features

- 🏠 Create, edit, and delete house listings
- 🔍 Filter and search for properties
- 📸 Upload house images
- 👤 User authentication (login, register)
- 💡 Responsive layout with Tailwind CSS
- ✅ Email validation (included)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/rent_wise.git
cd rent_wise
````

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Node/Tailwind dependencies

```bash
npm install
```

### 5. Copy the environment file

```bash
cp .env_sample .env
# Then fill in your secret keys and configs
```

### 6. Run database migrations

```bash
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open your browser at `http://localhost:8000`.

---

## 🧱 Project Structure

```
rent_wise/                 # Django project root
├── accounts/              # Handles user registration/login
├── properties/            # Manages house listings
├── static/                # Global static assets
├── templates/             # Global HTML templates
├── .env_sample            # Sample environment variables
├── .gitignore             # Files ignored by git
├── manage.py              # Django command-line utility
├── package.json           # Tailwind + npm dependencies
├── package-lock.json      # NPM lock file
└── .vscode/               # (Optional) VSCode settings
```

---

## 🛠 Tailwind Setup

This project uses Tailwind CSS via npm.

To compile Tailwind:

```bash
npx tailwindcss -i ./static/src/input.css -o ./static/css/output.css --watch
```

You can automate this with a script in `package.json`.

---

## 📜 License

This project is licensed under the **MIT License**.

---

> Made with 🧠 by \PyWise using Django + Tailwind ❤️

```
