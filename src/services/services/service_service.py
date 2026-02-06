from uuid import UUID

from services.repositories.service_repository import ServiceRepository
from systems.models import Service

class ServiceService:
    
    @staticmethod
    def get_service(service_id: UUID):
        return ServiceRepository.get_by_id(service_id)
    
    @staticmethod
    def destroy_service(service: Service):        
        return ServiceRepository.destroy(service)
    