from django.db import connection
from django.core.cache import cache
from utils.logger import get_logger

logger = get_logger(__name__)

class RedisCache:
    
    @classmethod
    def get(cls, key):
        logger.debug(f"Starting RedisCache get - key: {key}")
        key = cls.__get_tenant_key(key)
        return cache.get(key)
    
    @classmethod
    def set(cls, key: str, value, timeout: int | None):
        """
        Args:
            key (str): Key to index data
            value (any): Data to be stored
            timeout (int | None): Timeout in minutes
        """
        logger.debug(f"Starting RedisCache set - key: {key}")
        key = cls.__get_tenant_key(key)
        timeout = 60 * timeout if timeout else None
        return cache.set(key, value, timeout)
    
    @classmethod
    def delete(cls, key: str):
        logger.debug(f"Starting RedisCache delete - key: {key}")
        key = cls.__get_tenant_key(key)
        return cache.delete(key)
    
    @staticmethod
    def __get_tenant_key(key: str) -> str:
        return f"tenant.{connection.tenant.schema_name}.{key}"