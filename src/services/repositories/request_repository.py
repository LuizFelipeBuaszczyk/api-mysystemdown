from services.models import Request
from systems.models import Service  

from utils.logger import get_logger

logger = get_logger(__name__)

class RequestRepository:
    
    @staticmethod
    def get_all_by_service(service: Service):
        logger.debug(f"Starting RequestRepository get_all_by_service - service_id: {service.id}")
        return Request.objects.filter(service=service)
    
    @staticmethod
    def create_request(data: dict):
        logger.debug(f"Starting RequestRepository create_request - service_id: {data['service'].id}")
        return Request.objects.create(**data)