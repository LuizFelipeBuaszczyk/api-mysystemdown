from rest_framework.permissions import BasePermission

from systems.models import Service   
from iam.authentication.token_auth import TokenAuthentication

BOT_ACTIONS = ["create", "list"]

class RequestPermission(BasePermission):
    
    def has_permission(self, request, view):
        service_pk = view.kwargs.get("service_pk", None)
        
        if not request.user.is_authenticated:
            if view.action not in BOT_ACTIONS:
                return False
            return TokenAuthentication.validate_bot_token(request.headers, service_pk=service_pk)

     
        if view.action == "list":
            return Service.objects.filter(
                id=service_pk,
                system__memberships__user=request.user,
                system__memberships__group__permissions__codename="view_request"
            ).exists()
            
        
        return False
    
    def has_object_permission(self, request, view, obj):
        return True