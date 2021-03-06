from rest_framework.permissions import BasePermission


class IsAuthorPermission(BasePermission):
    def has_object_permission(self, request, obj):
        return request.user.is_authenticated and request.user == obj.author

