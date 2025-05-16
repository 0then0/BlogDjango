from rest_framework import permissions


class IsAuthorOrAdmin(permissions.BasePermission):
    """
    Only allow the author of an object or staff to edit or delete it.
    Read-only for everyone else.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user or request.user.is_staff
