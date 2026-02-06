
from systems.models import System
from users.models import User

class SystemRepository:       
    
    
    @staticmethod
    def get_all(user: User):
        return System.objects.filter(
            memberships__user=user
        ).distinct()
    
    @staticmethod
    def get_by_name(name: str):
        return System.objects.filter(name=name).values()
    
    @staticmethod
    def create_system(data: dict):
        return System.objects.create(**data)
    