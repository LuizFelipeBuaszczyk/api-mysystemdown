from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    def handle(self, *args, **options):
        roles = [
            "user_base", 
            "owner", 
            "admin", 
            "viewer"
        ]
        
        for role in roles:
            Group.objects.get_or_create(name=role)
            
        self.stdout.write(self.style.SUCCESS("Role seed completed successfully"))           
        