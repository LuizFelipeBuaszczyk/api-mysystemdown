from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from systems.models import System, Bot, Service
from iam.models import Membership

class Command(BaseCommand):
    # Manipula os grupos
    owner = Group.objects.get(name="owner")
    admin = Group.objects.get(name="admin")
    viewer = Group.objects.get(name="viewer")
    user_base = Group.objects.get(name="user_base")
    
    def handle(self, *args, **options):              
    
        # Adicionando permissões
        self._add_system_permissions()
        self._add_bot_permissions()
        self._add_service_permissions()
        self._add_membership_permissions()
        
        self.stdout.write(self.style.SUCCESS("Group permissions seed completed successfully"))
        
    def _add_system_permissions(self):
        # Busca todas as permissões de systems
        content_type  = ContentType.objects.get_for_model(System)
        perms = Permission.objects.filter(content_type=content_type) 
        
        # Adiciona as regras
        self.user_base.permissions.add(*perms.filter(
            codename__in=["view_system", "add_system"]
        ))
        
        self.owner.permissions.add(*perms.filter(
            codename__in=[ "view_system", "change_system", "delete_system"]
        ))

        self.admin.permissions.add(*perms.filter(
            codename__in=["view_system", "change_system"]
        ))

        self.viewer.permissions.add(*perms.filter(
            codename__in=["view_system"]
        ))
        
    def _add_bot_permissions(self):
        content_type = ContentType.objects.get_for_model(Bot)
        perms = Permission.objects.filter(content_type=content_type) 
        
        # Adiciona as regras
        
        self.owner.permissions.add(*perms.filter(
            codename__in=["add_bot", "view_bot", "change_bot", "delete_bot"]
        ))

        self.admin.permissions.add(*perms.filter(
            codename__in=["add_bot", "view_bot", "change_bot", "delete_bot"]
        ))

        self.viewer.permissions.add(*perms.filter(
            codename__in=["view_bot", "change_bot"]
        ))
        
    def _add_service_permissions(self):
        content_type = ContentType.objects.get_for_model(Service)
        perms = Permission.objects.filter(content_type=content_type) 
        
        # Adiciona as regras
        
        self.owner.permissions.add(*perms.filter(
            codename__in=["add_service", "view_service", "change_service", "delete_service"]
        ))

        self.admin.permissions.add(*perms.filter(
            codename__in=["add_service", "view_service", "change_service", "delete_service"]
        ))

        self.viewer.permissions.add(*perms.filter(
            codename__in=["add_service", "view_service", "change_service", "delete_service"]
        ))    
        
    def _add_membership_permissions(self):
        # Busca todas as permissões de Membership
        content_type  = ContentType.objects.get_for_model(Membership)
        perms = Permission.objects.filter(content_type=content_type) 
        
        self.owner.permissions.add(*perms.filter(
            codename__in=["add_membership", "view_membership", "change_membership", "delete_membership"]
        ))

        self.admin.permissions.add(*perms.filter(
            codename__in=["add_membership", "view_membership", "change_membership", "delete_membership"]
        ))

        self.viewer.permissions.add(*perms.filter(
            codename__in=["view_membership"]
        ))
        
