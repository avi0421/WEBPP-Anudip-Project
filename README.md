# WEBPP-Anudip-Project
# 🧾 Django Invoice App

A Django-based web application to create, manage, and view customer invoices. It uses Django's ORM, views, templates, and models to keep everything structured and maintainable.

---

## 🚀 Getting Started

Follow the steps below to set up the project in a virtual environment (`env`) using VS Code and Windows CMD.

---

### ✅ Prerequisites

- Python installed (preferably 3.10+)
- Git installed
- VS Code (with Python extension)

---

### 🛠️ Setup Steps (Windows - CMD)

1. **Create a project folder**
    ```bash
    mkdir django-invoicesapp
    cd django-invoicesapp
    ```

2. **Open folder in VS Code**
    - Hold `Shift` + right click → Select **"Open with Code"**

3. **Create virtual environment**
    ```bash
    python -m venv env
    ```

4. **Activate virtual environment**
    ```bash
    cd env
    Scripts\activate
    ```

5. **Go back to project root**
    ```bash
    cd ..
    ```

6. **Install Django**
    ```bash
    pip install django
    ```

7. **Create Django project**
    ```bash
    django-admin startproject invoice_project
    cd invoice_project
    ```

8. **Start the app**
    ```bash
    python manage.py startapp invoice_app
    ```

9. **Move `invoice_app` folder into `env` if needed** (optional step if you're organizing it that way)

10. **Run the development server**
    ```bash
    python manage.py runserver
    ```

---

