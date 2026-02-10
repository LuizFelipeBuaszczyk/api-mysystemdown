
from systems.models import System

from utils.logger import get_logger

logger = get_logger(__name__)

class SystemRepository:       
    
    @staticmethod
    def get_all():
        logger.debug("Starting SystemRepository get_all")
        return System.objects.distinct()
    
    @staticmethod
    def get_by_name(name: str):
        logger.debug(f"Starting SystemRepository get_by_name - name: {name}")
        return System.objects.filter(name=name).values()
    
    @staticmethod
    def create_system(data: dict):
        logger.debug(f"Starting SystemRepository create_system - name: {data['name']}")
        return System.objects.create(**data)
    