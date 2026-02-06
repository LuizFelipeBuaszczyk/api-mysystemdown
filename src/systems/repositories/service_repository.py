from uuid import UUID

from systems.models import Service, System


class ServiceRepository:
    
    @staticmethod
    def get_all(system: System):
        return Service.objects.filter(system=system)
    
    @staticmethod
    def get_all_actives(system: System):
        return Service.objects.filter(system=system, is_active=True)
    
    @staticmethod
    def create_service(data: dict):
        return Service.objects.create(**data)
    
    @staticmethod
    def get_by_title(title: str):
        return Service.objects.filter(title=title).values()
    
    @staticmethod
    def get_by_system_id(system_id: UUID, is_active: bool):
        return Service.objects.filter(
            system_id=system_id, 
            is_active=is_active
        )