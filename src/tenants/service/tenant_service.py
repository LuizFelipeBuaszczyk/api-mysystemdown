
from tenants.repositories.client_repository import ClientRepository
from tenants.repositories.domain_repository import DomainRepository
from iam.services.membership_service import MembershipService

from django.contrib.auth.models import Group
from users.models import User

from utils.logger import get_logger

logger = get_logger(__name__)

class TenantService():

    @staticmethod
    def create_tenant(data: dict, user: User):
        logger.info(f"Starting tenant service create_tenant - user_id: {user.id}")
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