# 🎓 Django Student Management System

This is a basic Student Management System built using **Django** and **SQLite**. It allows users to add, edit, delete, and view student records through a simple web interface. It includes a Django admin panel for managing student data and uses no REST APIs or external databases.

---

## 🚀 Features

- Add new students
- Edit student information
- Delete student records
- View all students
- Built-in Django admin dashboard
- Uses SQLite as the default database

---

## 🧰 Tech Stack

- Python 3.x
- Django 4.x
- SQLite (default database)

---

## ⚙️ How to Set Up the Project

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system
2. Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
4. Apply Migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
5. Create a Superuser
bash
Copy
Edit
python manage.py createsuperuser
Follow the prompts to set up your admin login credentials.

6. Run the Development Server
bash
Copy
Edit
python manage.py runserver
Open your browser and visit:

http://127.0.0.1:8000/ – Main site

http://127.0.0.1:8000/admin/ – Admin dashboard

📁 Project Structure
perl
Copy
Edit
student-management-system/
├── manage.py
├── db.sqlite3
├── app_name/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── student_management/
│   ├── settings.py
│   └── urls.py
├── requirements.txt
└── README.md
☁️ Push the Project to GitHub
bash
Copy
Edit
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/student-management-system.git
git branch -M main
git push -u origin main
👨‍💻 Author
Your Cassian
GitHub: https://github.com/yourusername












