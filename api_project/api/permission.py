# api/permissions.py
from rest_framework.permissions import BasePermission

class IsBookOwner(BasePermission):
    """
    Custom permission to only allow the owner of a book to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Allow access if the user is the owner of the book (example condition)
        return obj.owner == request.user
