from iam.repositories.membership_repository import MembershipRepository

from users.models import User
from tenants.models import Client

from utils.logger import get_logger
from infra.cache.redis import RedisCache

logger = get_logger(__name__)

class MembershipService:      
    
    @staticmethod
    def get_membership_by_tenant(tenant: Client):
        logger.info(f"Starting membership service get_membership_by_tenant - tenant_id: {tenant.name}")
        KEY_NAME = f"list_memberships_by_tenant"
        
        cached = RedisCache.get(KEY_NAME)
        if cached:
            return cached
        
        data = MembershipRepository.get_memberships_by_tenant(tenant)
        RedisCache.set(KEY_NAME, data, 60)
        return data
        
    @staticmethod
    def create_membership(data: dict):
        logger.info(f"Starting membership service create_membership - user_id: {data['user'].id}")
        KEY_NAME = f"list_memberships_by_tenant"
        
        created_memembership = MembershipRepository.crate_membership(data)
        RedisCache.delete(KEY_NAME)
        return created_memembership