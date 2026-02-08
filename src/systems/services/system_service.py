from systems.repositories.system_repository import SystemRepository
from systems.exceptions import SystemAlreadyExistsError

from iam.services.membership_service import MembershipService
from users.models import User
from systems.models import System
from tenants.models import Client
from django.contrib.auth.models import Group

class SystemService:
       
    @staticmethod
    def list_systems():
        return SystemRepository.get_all()        
    
    @staticmethod
    def create_system(data: dict):
        existing = SystemRepository.get_by_name(data["name"])
        
        if existing:
            raise SystemAlreadyExistsError("System name has already registred")
        
        return SystemRepository.create_system(data)