from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    """
    Класс IsActive служит для ограничения доступа пользователей к API
    (доступ имеют только пользователи со статусом is_active)
    """
    def has_permission(self, request, view):
        return request.user.is_active
