from rest_framework import permissions


class ReadOnlyOrAuthorPermission(permissions.BasePermission):
    """
    Разрешает чтение всем, но изменять или удалять объект может только его автор.
    """

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or obj.author == request.user
