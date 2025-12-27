from django.db import models
from django.conf import settings

class Project(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('complete', 'Complete'),
        ('abandoned', 'Abandoned'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='managed_projects', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def can_change_status(self, user):
        return user.is_authenticated and user == self.manager and user.is_project_manager()
