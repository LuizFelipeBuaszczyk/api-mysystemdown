from iam.repositories.membership_repository import MembershipRepository

from users.models import User
from tenants.models import Client

class MembershipService:      
    
    @staticmethod
    def get_membership_by_tenant(tenant: Client):
        return MembershipRepository.get_memberships_by_tenant(tenant)
        
    @staticmethod
    def create_membership(data: dict):
        return MembershipRepository.crate_membership(data)