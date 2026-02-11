from django.contrib.auth.hashers import make_password
import time

from systems.utils.token import generate_token, PREFIX_BOT_TOKEN

from systems.repositories.bot_repository import BotRepository
from systems.models import System, Bot

from infra.cache.redis import RedisCache
from utils.logger import logging

logger = logging.getLogger(__name__)

class BotService:
    @staticmethod
    def get_all(system: System):
        logger.info(f"Starting BotService get_all - system_id: {system.id}")
        KEY_NAME = f"list_bots.{system.id}"
        
        cached = RedisCache.get(KEY_NAME)
        if cached:
            return cached
        
        data = BotRepository.get_all(system)
        RedisCache.set(KEY_NAME, data, 60)
        return data
    
    @staticmethod
    def create_bot(data: dict, system: System):
        logger.info(f"Starting BotService create_bot - system_id: {system.id}")
        KEY_NAME = f"list_bots.{system.id}"
        data["system"] = system
        
        # Gerando token
        token = generate_token()
        data["prefix_token"] =  str(int(time.time()))
        data["api_token"] = make_password(token)
        
        created_bot = BotRepository.create_bot(data)
        created_bot.api_token = f"{PREFIX_BOT_TOKEN}{data["prefix_token"]}_{token}"
        
        RedisCache.delete(KEY_NAME)
        return created_bot
    
    @staticmethod
    def delete_bot(bot: Bot):
        logger.info(f"Starting BotService delete_bot - bot_id: {bot.id}")
        KEY_NAME = f"list_bots.{bot.system.id}"
        RedisCache.delete(KEY_NAME)
        return BotRepository.delete_bot(bot)
    