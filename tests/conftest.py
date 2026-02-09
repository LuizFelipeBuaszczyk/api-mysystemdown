import pytest
from tenants.models import Client, Domain
from iam.models import Membership, Group
from rest_framework.test import APIClient
from django.core.management import call_command
from django_tenants.utils import schema_context

@pytest.fixture(scope="session")
def public_tenant(django_db_setup, django_db_blocker):
    """Inicializa setup inicial para os testes.
    ---
    - django_db_setup: Garante que o banco está pronto para os testes
    - django_db_bloquer: Bloqueia o acesso ao banco para os testes
    """
    with django_db_blocker.unblock(): ## Desbloqueia o acesso ao banco 
        tenant, created = Client.objects.get_or_create(
            schema_name="public",
            defaults={"name": "Public"}
        )

        Domain.objects.get_or_create(
            domain="localhost",
            tenant=tenant,
            defaults={"is_primary": True}
        )
        
        if created:
            with schema_context(tenant.schema_name):
                call_command("seed_roles", verbosity=0)
                call_command("seed_group_permissions", verbosity=0)

    return tenant

@pytest.fixture(scope="session")
def user(django_db_setup, django_db_blocker, public_tenant):
    from django_tenants.utils import schema_context
    
    from users.models import User
    with django_db_blocker.unblock():
        with schema_context(public_tenant.schema_name):
            return User.objects.create(
                email="test@test.com",
                password="123456",
                first_name="Test",
                last_name="User"
            )

@pytest.fixture
def public_tenant_client(public_tenant):
    from django_tenants.test.client import TenantClient
    return TenantClient(public_tenant)

@pytest.fixture(scope="session")
def tenant1(create_tenant, user):
    tenant = create_tenant(
        schema_name="tenant1",
        domain="tenant1.localhost",
        name="Tenant 1",
        user=user
    )
    return tenant
    
    
@pytest.fixture
def tenant_client(tenant1, user):
    from django_tenants.test.client import TenantClient
    from rest_framework_simplejwt.tokens import RefreshToken

    client = TenantClient(tenant1)

    token = RefreshToken.for_user(user)
    client.defaults["HTTP_AUTHORIZATION"] = f"Bearer {token.access_token}"
    return client


@pytest.fixture
def public_auth_client(public_tenant_client, user):
    from rest_framework_simplejwt.tokens import RefreshToken

    token = RefreshToken.for_user(user)
    public_tenant_client.defaults["HTTP_AUTHORIZATION"] = f"Bearer {token.access_token}"
    return public_tenant_client

pytest_plugins = [
    "tests.fixtures.user_fixture",
    "tests.fixtures.tenant_fixture",
    "tests.fixtures.system_fixture",
    "tests.fixtures.tenant_fixture"
]