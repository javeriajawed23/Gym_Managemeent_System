# Gym_Managemeent_System
🏋️A complete solution to manage members, trainers, and workouts efficiently.

📌 Overview

The Gym Management System is a web-based application built with Django to streamline gym operations such as member registration, trainer assignments, attendance tracking, payment management, and workout plans. With a Bootstrap-powered UI and PostgreSQL database, it ensures efficiency, security, and ease of use for both admins and members.

🛠️ Tech Stack

Backend Framework: Django (Python)

Database: PostgreSQL (managed via pgAdmin)

Frontend: HTML, CSS, Bootstrap

Server/Environment: Django Development Server

🚀 Features

🔑 Role-based Login: Admin, Trainer, Member

👤 Member Management: Add, update, and track member profiles

🏋️ Trainer Module: Assign trainers and manage schedules

🏃 Attendance Tracking: Daily check-ins and logs

💳 Payment System: Manage membership fees and due dates

📋 Workout Plans: Trainers can create and assign routines

📊 Reports Dashboard: Insights on members, revenue, and attendance

⚙️ Installation & Setup

Clone the repository:

git clone https://github.com/yourusername/gym-management-system.git
cd gym-management-system


Create & activate a virtual environment:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py migrate


Run the server:

python manage.py runserver

🎯 Usage

Admin can manage members, trainers, payments, and attendance.

Trainers can create workout plans and monitor assigned members.

Members can log in to view schedules, attendance, and payment status.
