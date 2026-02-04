from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group

from systems.models import Service

class ServicePermission(BasePermission):
    
    def has_permission(self, request, view):
        system_pk = view.kwargs['system_pk']

        if view.action == "create":
            return Group.objects.filter(
                memberships__user=request.user,
                memberships__system__id=system_pk,
                permissions__codename="add_service"
            ).exists()
        
        if view.action == "list":
            return Group.objects.filter(
                memberships__user=request.user,
                memberships__system__id=system_pk,
                permissions__codename="view_service"
            ).exists()
        
        return False
    
    def has_object_permission(self, request, view, obj):
        service = Service.objects.filter(
            user=request.user,
            system=obj
        ).select_related("role").first()

        if not service:
            return False

        role = service.group

        action_perm_map = {
            "list": "view_service",
            "retrieve": "view_service",
            "update": "change_service",
            "partial_update": "change_service",
            "destroy": "delete_service",
        }

        required_perm = action_perm_map.get(view.action)

        if not required_perm:
            return False

        return role.permissions.filter(codename=required_perm).exists()