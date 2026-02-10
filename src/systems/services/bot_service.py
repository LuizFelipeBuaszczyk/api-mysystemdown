from django.contrib.auth.hashers import make_password
import time

from systems.utils.token import generate_token, PREFIX_BOT_TOKEN

from systems.repositories.bot_repository import BotRepository
from systems.models import System, Bot

from utils.logger import logging

logger = logging.getLogger(__name__)

class BotService:
    @staticmethod
    def get_all(system: System):
        logger.info(f"Starting BotService get_all - system_id: {system.id}")
        return BotRepository.get_all(system)
    
    @staticmethod
    def create_bot(data: dict, system: System):
        logger.info(f"Starting BotService create_bot - system_id: {system.id}")
        data["system"] = system
        
        # Gerando token
        token = generate_token()
        data["prefix_token"] =  str(int(time.time()))
        data["api_token"] = make_password(token)
        
        created_bot = BotRepository.create_bot(data)
        created_bot.api_token = f"{PREFIX_BOT_TOKEN}{data["prefix_token"]}_{token}"
        return created_bot
    
    @staticmethod
    def delete_bot(bot: Bot):
        logger.info(f"Starting BotService delete_bot - bot_id: {bot.id}")
        return BotRepository.delete_bot(bot)
    