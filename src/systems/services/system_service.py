from systems.repositories.system_repository import SystemRepository
from systems.exceptions import SystemAlreadyExistsError

from infra.cache.redis import RedisCache
from utils.logger import get_logger

logger = get_logger(__name__)

class SystemService:
       
    @staticmethod
    def list_systems():
        logger.info("Starting SystemService list_systems")
        KEY_NAME = "list_systems"
        
        cached = RedisCache.get(KEY_NAME)
        if cached:
            return cached
        
        data = SystemRepository.get_all()        
        RedisCache.set(KEY_NAME, data, 60)
        return data
    
    @staticmethod
    def create_system(data: dict):
        logger.info(f"Starting SystemService create_system - name: {data['name']}")
        existing = SystemRepository.get_by_name(data["name"])
        
        if existing:
            raise SystemAlreadyExistsError("System name has already registred")
        
        created_system = SystemRepository.create_system(data)
        RedisCache.delete("list_systems")
        return created_system