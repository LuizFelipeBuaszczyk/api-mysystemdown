from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from systems.models import System

class Command(BaseCommand):
    # Manipula os grupos
    owner = Group.objects.get(name="owner")
    admin = Group.objects.get(name="admin")
    viewer = Group.objects.get(name="viewer")
    user_base = Group.objects.get(name="user_base")
    
    def handle(self, *args, **options):              
    
        # Adicionando permissões
        self._add_system_permissions()
        
        self.stdout.write(self.style.SUCCESS("Group permissions seed completed successfully"))
        
    def _add_system_permissions(self):
        # Busca todas as permissões de systems
        system_ct = ContentType.objects.get_for_model(System)
        perms = Permission.objects.filter(content_type=system_ct) 
        
        # Adiciona as regras
        self.user_base.permissions.set(perms.filter(
            codename__in=["add_system"]
        ))
        
        self.owner.permissions.set(perms.filter(
            codename__in=["view_system", "change_system", "delete_system"]
        ))

        self.admin.permissions.set(perms.filter(
            codename__in=["view_system", "change_system"]
        ))

        self.viewer.permissions.set(perms.filter(
            codename__in=["view_system"]
        ))
