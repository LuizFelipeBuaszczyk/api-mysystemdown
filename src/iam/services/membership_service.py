from iam.repositories.membership_repository import MembershipRepository

from users.models import User
from tenants.models import Client

from utils.logger import get_logger

logger = get_logger(__name__)

class MembershipService:      
    
    @staticmethod
    def get_membership_by_tenant(tenant: Client):
        logger.info(f"Starting membership service get_membership_by_tenant - tenant_id: {tenant.name}")
        return MembershipRepository.get_memberships_by_tenant(tenant)
        
    @staticmethod
    def create_membership(data: dict):
        logger.info(f"Starting membership service create_membership - user_id: {data['user'].id}")
        return MembershipRepository.crate_membership(data)