from uuid import UUID

from systems.models import Service, System

from utils.logger import get_logger

logger = get_logger(__name__)

class ServiceRepository:
    
    @staticmethod
    def get_all(system: System):
        logger.debug(f"Starting ServiceRepository get_all - system_id: {system.id}")
        return Service.objects.filter(system=system)
    
    @staticmethod
    def get_all_actives(system: System):
        logger.debug(f"Starting ServiceRepository get_all_actives - system_id: {system.id}")
        return Service.objects.filter(system=system, is_active=True)
    
    @staticmethod
    def create_service(data: dict):
        logger.debug(f"Starting ServiceRepository create_service - system_id: {data['system'].id}, title: {data['title']}")
        return Service.objects.create(**data)
    
    @staticmethod
    def get_by_title(title: str):
        logger.debug(f"Starting ServiceRepository get_by_title - title: {title}")
        return Service.objects.filter(title=title).values()
    
    @staticmethod
    def get_by_system_id(system_id: UUID, is_active: bool):
        logger.debug(f"Starting ServiceRepository get_by_system_id - system_id: {system_id}, is_active: {is_active}")
        return Service.objects.filter(
            system_id=system_id, 
            is_active=is_active
        )