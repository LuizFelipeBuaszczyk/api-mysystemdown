from systems.repositories.system_repository import SystemRepository
from systems.exceptions import SystemAlreadyExistsError

from utils.logger import get_logger

logger = get_logger(__name__)

class SystemService:
       
    @staticmethod
    def list_systems():
        logger.info("Starting SystemService list_systems")
        return SystemRepository.get_all()        
    
    @staticmethod
    def create_system(data: dict):
        logger.info(f"Starting SystemService create_system - name: {data['name']}")
        existing = SystemRepository.get_by_name(data["name"])
        
        if existing:
            raise SystemAlreadyExistsError("System name has already registred")
        
        return SystemRepository.create_system(data)