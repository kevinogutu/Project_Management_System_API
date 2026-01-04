from rest_framework import permissions

class IsProjectManagerOrReadOnly(permissions.BasePermission):
    

    def has_object_permission(self, request, view, obj):
       
        if request.method in permissions.SAFE_METHODS:
            return True
       
        return request.user.is_authenticated and obj.manager == request.user and request.user.is_project_manager()
class IsProjectManager(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.manager == request.user and request.user.is_project_manager()
