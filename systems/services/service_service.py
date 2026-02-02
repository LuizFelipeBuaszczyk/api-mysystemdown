from systems.repositories.service_repository import ServiceRepository
from systems.models import System

class ServiceService:

    @staticmethod
    def list_services(is_active: bool):
        return ServiceRepository.get_all(is_active)
    
    @staticmethod
    def create_service(data: dict, system: System):
        data["system"] = system
        service = ServiceRepository.create_service(data)