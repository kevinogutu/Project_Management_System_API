Project Management System API
This project is part of my capstone work and focuses on building a fully functional Project Management System API using Django and Django REST Framework. The API will support project tracking, task management, user roles, and permissions.

Current Progress (Part 3)
The following setup and configuration steps have been completed:
Created the project directory Project_Management_System_API on GitHub and on the local machine.
Linked the GitHub repository to the local repository.
Set up a virtual environment (my_venv).
Installed core dependencies:
Django
Django REST Framework
Django CORS Headers
Created the main project project_managementAPI.
Created the foundational apps:
accounts
projects
tasks
reports
Updated project_managementAPI/settings.py to register installed apps and required frameworks.
Next Steps
The upcoming development goals include:
1.	Implementing the accounts app with a custom user model and role-based access.
2.	Creating the projects and tasks models and running migrations.
3.	Adding serializers and viewsets to handle API functionality 
12/14/2025
Implemented user model & roles (accounts)
Added AUTH_USER_MODEL = 'accounts.User' to seeting.py
Created registration serializer & view
Added accounts/view.py
Added accounts/urls.py



Project Goals
The final API will include:
User registration and authentication
Role-based permissions (Project Manager, standard users, etc.)
Project creation, updates, and status management
Task assignment, task status updates, and CRUD operations
Optional reporting endpoints for project/task analytics
Optional integration with external services (e.g., email notifications)

