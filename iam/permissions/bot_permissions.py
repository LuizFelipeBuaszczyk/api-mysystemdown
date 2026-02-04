from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group

from systems.models import Bot

class BotPermission(BasePermission):
    
    def has_permission(self, request, view):
        system_pk = view.kwargs['system_pk']

        if view.action == "create":
            return Group.objects.filter(
                memberships__user=request.user,
                memberships__system__id=system_pk,
                permissions__codename="add_bot"
            ).exists()
        
        if view.action == "list":
            return request.user.has_perm("systems.view_bot")
        
        return False
    
    def has_object_permission(self, request, view, obj):
        bot = Bot.objects.filter(
            user=request.user,
            system=obj
        ).select_related("role").first()

        if not bot:
            return False

        role = bot.group

        action_perm_map = {
            "list": "view_bot",
            "retrieve": "view_bot",
            "update": "change_bot",
            "partial_update": "change_bot",
            "destroy": "delete_bot",
        }

        required_perm = action_perm_map.get(view.action)

        if not required_perm:
            return False

        return role.permissions.filter(codename=required_perm).exists()