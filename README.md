# Office Employee Management System (Django)

A comprehensive Django-based Office Management System designed to manage employees, departments, attendance, payroll, tasks, and organizational workflows in a structured environment.

---

## 🚀 Features

### 👨‍💼 Employee Management
- Add, update, and manage employee records
- Assign departments and roles
- Store employee contact and hire details

### 📊 HR & Operations Modules
- Attendance tracking system (Present/Absent/Late)
- Payroll management with salary calculations
- Task assignment and tracking
- Training session management
- Meeting scheduling system

### 💰 Financial Management
- Expense tracking system
- Payroll with basic, overtime, and tax deduction handling

### 📂 Additional Features
- Image upload support for records
- Feedback system for employees
- Organized department-wise structure

---

## 🛠️ Tech Stack
- Backend: Django (Python)
- Frontend: HTML, CSS
- Database: SQLite
- Media handling for image uploads

---

## 🏗️ Project Architecture
- Modular Django app structure (`emp_app`)
- MVC architecture (Model-View-Template)
- Separate models for HR operations, finance, and management

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/your-username/office-employee-project.git
cd office-employee-project
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver