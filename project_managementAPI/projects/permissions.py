from rest_framework import permissions

class IsProjectManagerOrReadOnly(permissions.BasePermission):
    """
    Allow full write for project manager, read-only for others.
    For status-change endpoint we will require manager specifically.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE methods allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow manager (object.manager) to edit
        return request.user.is_authenticated and obj.manager == request.user and request.user.is_project_manager()
class IsProjectManager(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.manager == request.user and request.user.is_project_manager()
