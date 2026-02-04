from iam.repositories.membership_repository import MembershipRepository

from users.models import User
from systems.models import System

class MembershipService:      
    
    @staticmethod
    def get_membership_by_system(system: System):
        return MembershipRepository.get_memberships_by_system(system)
        
    @staticmethod
    def create_membership(data: dict, system: System):
        data["system"] = system
        return MembershipRepository.crate_membership(data)