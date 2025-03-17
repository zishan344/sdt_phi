from rest_framework.permissions import BasePermission

class IsLibrarian(BasePermission):
    def has_permission(self, request, view):
        # Librarians (staff) have full access
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)