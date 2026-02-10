
from iam.models import Membership

from tenants.models import Client
from users.models import User

from utils.logger import get_logger

logger = get_logger(__name__)

class MembershipRepository:
    
    @staticmethod
    def get_memberships_by_tenant(tenant: Client):
        logger.debug(f"Starting repository get_memberships_by_tenant - tenant_id: {tenant.name}")
        return Membership.objects.filter(tenant=tenant).select_related("user")
    
    @staticmethod
    def crate_membership(data: dict):
        logger.debug(f"Starting repository crate_membership - user_id: {data['user'].id}")
        return Membership.objects.create(**data)