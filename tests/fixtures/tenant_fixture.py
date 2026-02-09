import pytest


@pytest.fixture(scope="session")
def create_tenant(django_db_setup, django_db_blocker, public_tenant):
    from django_tenants.utils import schema_context
    from tenants.models import Client, Domain
    from iam.models import Membership, Group
    
    tenants_cache = {}

    def _create(schema_name, domain, name, user):
        if schema_name in tenants_cache:
            return tenants_cache[schema_name]
        
        with django_db_blocker.unblock():
            with schema_context(public_tenant.schema_name):
                tenant = Client.objects.create(
                    schema_name=schema_name,
                    name=name
                )

                Domain.objects.create(
                    domain=domain,
                    tenant=tenant,
                    is_primary=True
                )
                
                Membership.objects.create(
                    user=user,
                    group=Group.objects.get(name="owner"),
                    tenant=tenant
                )

                    
        tenants_cache[schema_name] = tenant
        return tenant

    return _create

@pytest.fixture
def tenant_post_data():
    """Payload base para o endpoint de criação de tenant"""
    return {
        "client": {
            "schema_name": "tenant_test",
            "name": "Tenant Test"
        },
        "domain": {
            "domain": "tenant_test.locahost"
        }
    }