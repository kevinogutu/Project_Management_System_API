
Django Project Management API
A robust backend API for a Project Management System. This system allows users to manage projects and tasks with granular, role-based permissions (Managers vs. Regular Users), utilizing JWT authentication and scalable architecture.
🚀 Features
•	Role-Based Access Control: Custom user model distinguishing between Managers (full project control) and Users (task execution).
•	Project & Task Management: Complete CRUD operations for project lifecycles and task assignments.
•	Secure Authentication: Modern JWT (JSON Web Token) implementation for secure API access.
•	Data Validation: Comprehensive serializers to validate incoming data and format JSON responses.
•	Analytics: Optional reporting endpoints for project status breakdowns and task summaries.

🏗️ Architecture & Design Decisions
This project follows a scalable Django app structure. Below is a breakdown of the core components and the reasoning behind them.
Component	Functionality (What)	Necessity (Why)
Project Setup	My_venv+core/ Project_Management_System_API	Isolates dependencies; central container for all apps.
App Structure	Split into accounts, projects, tasks, reports	Keeps code organized, modular, and scalable.
Custom User	Extends default user with role field	Enables specific permissions (e.g., "Only Managers update status").
Database Models	Project & Task tables	Defines the core data structure for the ORM to build SQL tables.
Serializers	Python Objects ↔ JSON	APIs speak JSON; serializers handle validation and conversion.
Permissions	Custom Permission Classes	Restricts unauthorized actions (e.g., preventing users from deleting projects).
ViewSets/Routers	CRUD logic & URL mapping	Handles the actual request processing and maps URLs automatically.
Authentication	JWT Implementation	Stateless, secure verification of who is making the request.

🛠️ Installation & Setup
Follow these steps to get the API running locally.
Prerequisites
•	Python 3.8+
•	SQLite3
1. Clone and Configure
Bash
# Clone the repository
git clone https://github.com/kevinogutu/Project_Management_System_API.git
cd django-pm-api

# Create a virtual environment
python -m venv my_venv

# Activate the virtual environment
# Windows:
my_venv\Scripts\activate
# Mac/Linux:
source my_venv/bin/activate
2. Install Dependencies
Bash
pip install -r requirements.txt
3. Database Migration
Initialize the database tables based on the models.
Bash
python manage.py makemigrations
python manage.py migrate
4. Create Superuser (Admin)
Bash
python manage.py createsuperuser
5. Run the Server
Bash
python manage.py runserver
The API will be available at http://127.0.0.1:8000/.

🔌 API Endpoints

The API is structured around RESTful principles.
Authentication
•	POST /api/token/ - Obtain JWT access & refresh tokens.
•	POST /api/token/refresh/ - Refresh access token.
Projects
•	GET /api/projects/ - List all projects (Permissions apply).
•	POST /api/projects/ - Create a new project (Manager only).
•	PATCH /api/projects/{id}/ - Update project details/status.
Tasks
•	GET /api/tasks/ - List tasks.
•	POST /api/tasks/ - Create a task linked to a project.
•	PATCH /api/tasks/{id}/ - Update task status/assignee.
Reports
•	GET /api/reports/dashboard/ - Returns summary metrics (Total projects, task completion rates).

🧪 Testing
Automated tests are included to ensure permission logic and data integrity are maintained.
Bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test projects
Why this matters: Tests prevent regressions, ensuring that a regular user never accidentally gets Manager privileges.

📦 Deployment
This project is configured for deployment on Heroku or PythonAnywhere.
Production Checklist:
1.	Set DEBUG = False in settings.
2.	Configure ALLOWED_HOSTS.
3.	Install Gunicorn as the WSGI server.
4.	Run database migrations on the production server.

🤝 Contributing
1.	Fork the project
2.	Create your feature branch (git checkout -b feature/AmazingFeature)
3.	Commit your changes (git commit -m 'Add some AmazingFeature')
4.	Push to the branch (git push origin feature/AmazingFeature)
5.	Open a Pull Request

