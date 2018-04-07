from rest_framework import permissions


class IsFaculty(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role == 1:
            return True
        else:
            return False


class IsStudent(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role == 2:
            return True
        else:
            return False