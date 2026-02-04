from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group

from iam.models import Membership

class MembershipPermission(BasePermission):
    
    def has_permission(self, request, view):
        system_pk = view.kwargs['system_pk']

        if view.action == "create":
            return Group.objects.filter(
                memberships__user=request.user,
                memberships__system__id=system_pk,
                permissions__codename="add_membership"
            ).exists()
        
        if view.action == "list":
            return request.user.has_perm("systems.view_membership")
        
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
            "list": "view_membership",
            "retrieve": "view_membership",
            "update": "change_membership",
            "partial_update": "change_membership",
            "destroy": "delete_membership",
        }

        required_perm = action_perm_map.get(view.action)

        if not required_perm:
            return False

        return role.permissions.filter(codename=required_perm).exists()