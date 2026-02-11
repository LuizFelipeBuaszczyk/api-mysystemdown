from systems.repositories.service_repository import ServiceRepository
from systems.models import System

from infra.cache.redis import RedisCache
from utils.logger import get_logger

logger = get_logger(__name__)

class ServiceService:

    @staticmethod
    def list_services(system: System, just_actives: bool):   
        logger.info(f"Stating ServiceService list_services - system_id: {system.id}")
        KEY_NAME = f"list_services.{system.id}.{just_actives}"
        
        cached = RedisCache.get(KEY_NAME)
        if cached:
            return cached
        
        data = ServiceRepository.get_all_actives(system) if just_actives else ServiceRepository.get_all(system)
        RedisCache.set(KEY_NAME, data, 60)
        return data
    
    @staticmethod
    def create_service(data: dict, system: System):
        logger.info(f"Starting ServiceService create_service - system_id: {system.id}")
        KEY_NAME_ACTIVES = f"list_services.{system.id}.{True}"
        KEY_NAME_ALL = f"list_services.{system.id}.{False}"
        data["system"] = system
        created_service = ServiceRepository.create_service(data)
        RedisCache.delete(KEY_NAME_ALL)
        RedisCache.delete(KEY_NAME_ACTIVES)
        return created_service
