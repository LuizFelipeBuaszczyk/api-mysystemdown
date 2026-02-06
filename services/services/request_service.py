
from services.repositories.request_repository import RequestRepository 
from systems.models import Service

class RequestService:
    
    @staticmethod
    def list_requests_by_service(service: Service):
        return RequestRepository.get_all_by_service(service)
    
    @staticmethod
    def create_request(data: dict, service: Service):
        data["service"] = service
        data["response_size_bytes"] = len(data["response_body"])        
        return RequestRepository.create_request(data)