from systems.repositories.service_repository import ServiceRepository
from systems.models import System

class ServiceService:

    @staticmethod
    def list_services(system: System, just_actives: bool):   
        return ServiceRepository.get_all_actives(system) if just_actives else ServiceRepository.get_all(system)
    
    @staticmethod
    def create_service(data: dict, system: System):
        data["system"] = system
        return ServiceRepository.create_service(data)
