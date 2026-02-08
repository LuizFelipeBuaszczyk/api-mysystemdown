
from tenants.repositories.client_repository import ClientRepository
from tenants.repositories.domain_repository import DomainRepository
from iam.services.membership_service import MembershipService

from django.contrib.auth.models import Group
from users.models import User

class TenantService():

    @staticmethod
    def create_tenant(data: dict, user: User):
        client = data["client"]
        client = ClientRepository.create_client(client)

        domain = data["domain"]
        domain["tenant"] = client
        domain = DomainRepository.create_domain(data["domain"])

        membership = MembershipService.create_membership(
            data={
                "user": user,
                "group": Group.objects.get(name="owner"),
                "tenant": client
            }
        )

        return {
            "client": client,
            "domain": domain
        }