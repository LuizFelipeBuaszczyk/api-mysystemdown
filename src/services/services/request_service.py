
from services.repositories.request_repository import RequestRepository 
from systems.models import Service

from utils.logger import get_logger

logger = get_logger(__name__)

class RequestService:
    
    @staticmethod
    def list_requests_by_service(service: Service):
        logger.debug(f"Starting RequestService list_requests_by_service - service_id: {service.id}")
        return RequestRepository.get_all_by_service(service)
    
    @staticmethod
    def create_request(data: dict, service: Service):
        logger.debug(f"Starting RequestService create_request - service_id: {service.id}")
        data["service"] = service
        data["response_size_bytes"] = len(data["response_body"])        
        return RequestRepository.create_request(data)