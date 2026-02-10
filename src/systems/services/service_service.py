from systems.repositories.service_repository import ServiceRepository
from systems.models import System

from utils.logger import get_logger

logger = get_logger(__name__)

class ServiceService:

    @staticmethod
    def list_services(system: System, just_actives: bool):   
        logger.info(f"Stating ServiceService list_services - system_id: {system.id}")
        return ServiceRepository.get_all_actives(system) if just_actives else ServiceRepository.get_all(system)
    
    @staticmethod
    def create_service(data: dict, system: System):
        logger.info(f"Starting ServiceService create_service - system_id: {system.id}")
        data["system"] = system
        return ServiceRepository.create_service(data)
