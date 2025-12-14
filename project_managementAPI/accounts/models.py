from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('manager', 'Project Manager'),
        ('user', 'Regular User'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')

    def is_project_manager(self):
        return self.role == 'manager'
