from systems.repositories.system_repository import SystemRepository
from systems.exceptions import SystemAlreadyExistsError

from iam.services.membership_service import MembershipService
from users.models import User
from systems.models import System

class SystemService:
       
    @staticmethod
    def list_systems(user: User):
        return SystemRepository.get_all(user)        
    
    @staticmethod
    def create_system(data: dict, owner: User):
        existing = SystemRepository.get_by_name(data["name"])
        
        if existing:
            raise SystemAlreadyExistsError("System name has already registred")
        
        system = SystemRepository.create_system(data)
        data = {
            "user": owner,
            "system": system,
            "role":"owner"
        }
        member = MembershipService.create_membership(data)
        return system