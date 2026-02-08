from django.core.management.base import BaseCommand
from tenants.models import Domain, Client

class Command(BaseCommand):
    def handle(self, *args, **options):
        tenant = Client.objects.create(schema_name="public", name="Public")
        domain = Domain.objects.create(domain="localhost", tenant=tenant, is_primary=True)

        self.stdout.write(self.style.SUCCESS("Tenant seed completed successfully"))