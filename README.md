
# 🏡 Rent Wise – House Catalog Web App

**Rent Wise** is a modern, responsive house catalog application built with **Django** and **Tailwind CSS**.  
Users can browse, list, and manage rental properties with ease.



### ⚙️ Tech Stack
---

- 🐍 **Backend:** Django (Python)
- 🎨 **Frontend:** Tailwind CSS via npm
- 🔐 **Auth:** Custom Django app (`accounts`)
- 🏘️ **Listings:** Managed by the `properties` app
- 🛠️ **Tooling:** Environment variables with `.env`

---


### ✨ Features

---

- 🏠 Create, update, and delete house listings
- 🔍 Filter and search through properties
- 📸 Upload property images
- 👤 User registration and authentication
- 📱 Fully responsive layout with Tailwind
- ✅ Built-in email validation

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/PyWise/rent_wise.git
cd rent_wise
````

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Install Tailwind (Node) dependencies

```bash
npm install
```

### 5️⃣ Set up environment variables

```bash
cp .env_sample .env
# Fill in your secrets in the .env file
```

### 6️⃣ Apply migrations

```bash
python manage.py migrate
```

### 7️⃣ Start the development server

```bash
python manage.py runserver
```

➡️ Open your browser: [http://localhost:8000](http://localhost:8000)

---

## 🧱 Project Structure

```
rent_wise/
├── accounts/              # User authentication (login/register)
├── properties/            # House/property listing logic
├── static/                # Static files (CSS, JS, images)
├── templates/             # Global HTML templates
├── .env_sample            # Sample env file
├── .gitignore             # Git ignored files
├── manage.py              # Django CLI entry point
├── package.json           # Tailwind/npm setup
├── package-lock.json      # NPM lock file
└── .vscode/               # (Optional) VSCode settings
```

---

## 🎨 Tailwind Setup

This project uses [Tailwind CSS](https://tailwindcss.com/) via npm.

To start the Tailwind watcher:

```bash
npx tailwindcss -i ./static/src/input.css -o ./static/css/output.css --watch
```

You can also define this as a script in `package.json`:

```json
"scripts": {
  "dev": "tailwindcss -i ./static/src/input.css -o ./static/css/output.css --watch"
}
```

Then just run:

```bash
npm run dev
```

---

## 📜 License

Licensed under the **MIT License**.

---

> 🧠 Made with care by **PyWise** using Django + Tailwind ❤️
