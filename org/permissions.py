from rest_framework.permissions import IsAuthenticated


class EmployeesPermissions(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_staff
