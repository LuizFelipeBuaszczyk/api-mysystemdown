from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group

from iam.models import Membership

class MembershipPermission(BasePermission):
    
    def has_permission(self, request, view):
        if view.action == "create":
            return Group.objects.filter(
                memberships__user=request.user,
                memberships__tenant=request.tenant,
                permissions__codename="add_membership"
            ).exists()
        
        if view.action == "list":
            return Group.objects.filter(
                memberships__user=request.user,
                memberships__tenant=request.tenant,
                permissions__codename="view_membership"
            ).exists()
        
        return False
    
    def has_object_permission(self, request, view, obj):
        return False