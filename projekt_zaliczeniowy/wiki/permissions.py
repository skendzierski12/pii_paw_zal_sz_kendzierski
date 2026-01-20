from rest_framework import permissions

class IsAdminOrEditor(permissions.BasePermission):
      
    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        if request.method == 'GET':
            return True

        if request.method in ['POST', 'DELETE']:
            return request.user.is_staff
        
        if request.method == 'PUT':
            return request.user.is_staff or request.user.groups.filter(name='Editor').exists()
        
        return False

