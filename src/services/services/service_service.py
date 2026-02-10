from uuid import UUID

from services.repositories.service_repository import ServiceRepository
from systems.models import Service

from utils.logger import get_logger

logger = get_logger(__name__)

class ServiceService:
    
    @staticmethod
    def get_service(service_id: UUID):
        logger.info(f"Starting ServiceService get_service - service_id: {service_id}")
        return ServiceRepository.get_by_id(service_id)
    
    @staticmethod
    def destroy_service(service: Service):      
        logger.info(f"Starting ServiceService destroy_service - service_id: {service.id}")  
        return ServiceRepository.destroy(service)
    