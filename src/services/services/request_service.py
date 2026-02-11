
from services.repositories.request_repository import RequestRepository 
from systems.models import Service

from infra.cache.redis import RedisCache
from utils.logger import get_logger

logger = get_logger(__name__)

class RequestService:
    
    @staticmethod
    def list_requests_by_service(service: Service):
        logger.debug(f"Starting RequestService list_requests_by_service - service_id: {service.id}")
        KEY_NAME = f"list_requests_by_service.{service.id}"
        
        data = RequestRepository.get_all_by_service(service)
        RedisCache.set(KEY_NAME, data, 60)
        
        return data
    
    @staticmethod
    def create_request(data: dict, service: Service):
        logger.debug(f"Starting RequestService create_request - service_id: {service.id}")
        KEY_NAME = f"list_requests_by_service.{service.id}"
        
        data["service"] = service
        data["response_size_bytes"] = len(data["response_body"])        
        
        created_request = RequestRepository.create_request(data)
        RedisCache.delete(KEY_NAME)
        
        return created_request