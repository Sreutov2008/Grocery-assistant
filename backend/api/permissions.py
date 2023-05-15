from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    message = 'Нужны права администратора'

    def has_permission(self, request, view):
        return (
               request.method in permissions.SAFE_METHODS
               or (request.user.is_authenticated and request.user.is_admin)
        )


class IsAdminAuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    message = 'Нужны хоть какие-нибудь права, либо просто читай'

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_admin
            or request.user == obj.author
        )
