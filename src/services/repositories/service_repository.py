from uuid import UUID  

from systems.models import Service

class ServiceRepository:
    
    @staticmethod
    def get_by_id(service_id: UUID):
        return Service.objects.filter(id=service_id).first()
    
    @staticmethod
    def destroy(service: Service):
        return service.delete()