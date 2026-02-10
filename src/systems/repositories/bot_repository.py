from systems.models import Bot
from systems.models import System

from utils.logger import get_logger

logger = get_logger(__name__)

class BotRepository:
    
    @staticmethod
    def get_bot_by_prefix(prefix: str):
        logger.debug(f"Starting BotRepository get_bot_by_prefix - prefix: {prefix}")
        return Bot.objects.filter(prefix_token=prefix).first()
    
    @staticmethod
    def get_all(system: System):
        logger.debug(f"Starting BotRepository get_all - system_id: {system.id}")
        return Bot.objects.filter(system=system)

    @staticmethod
    def create_bot(data: dict):
        logger.debug(f"Starting BotRepository create_bot - system_id: {data['system'].id}, bot_name: {data['bot_name']}")
        return Bot.objects.create(**data)
    
    @staticmethod
    def delete_bot(bot: Bot):
        logger.debug(f"Starting BotRepository delete_bot - bot_id: {bot.id}")
        return bot.delete()