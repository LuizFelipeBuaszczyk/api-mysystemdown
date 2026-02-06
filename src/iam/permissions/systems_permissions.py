from rest_framework.permissions import BasePermission
from iam.models import Membership

class SystemPermission(BasePermission):
    
    def has_permission(self, request, view):
        if view.action == "create":
            return request.user.has_perm("systems.add_system")
        if view.action == "list":
            return request.user.has_perm("systems.view_system")
        
        return False
    
    def has_object_permission(self, request, view, obj):
        
        membership = Membership.objects.filter(
            user=request.user,
            system=obj
        ).select_related("role").first()

        if not membership:
            return False

        role = membership.group

        action_perm_map = {
            "list": "view_system",
            "retrieve": "view_system",
            "update": "change_system",
            "partial_update": "change_system",
            "destroy": "delete_system",
        }

        required_perm = action_perm_map.get(view.action)

        if not required_perm:
            return False

        return role.permissions.filter(codename=required_perm).exists()