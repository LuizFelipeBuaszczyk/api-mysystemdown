from django.contrib.auth.hashers import check_password

from iam.exceptions import InvalidApiTokenError, PermissionDenied

from systems.models import Bot
from systems.utils.token import PREFIX_BOT_TOKEN
from systems.repositories.bot_repository import BotRepository

class TokenAuthentication:
    
    @staticmethod
    def validate_bot_token(header: dict, **kwargs) -> bool :
        """Validate API Token for bot"""
        api_token = header.get("api-token", None)
        
        if not api_token:
            raise InvalidApiTokenError()
        
        if not api_token.startswith(PREFIX_BOT_TOKEN):
            raise InvalidApiTokenError()
        
        prefix = api_token[len(PREFIX_BOT_TOKEN):len(PREFIX_BOT_TOKEN)+10]        
        token = api_token[len(PREFIX_BOT_TOKEN) + len(prefix) + 1:]
        
    
        bot = BotRepository.get_bot_by_prefix(prefix)  
              
        if not bot:
            raise InvalidApiTokenError()
        
        if not check_password(token, bot.api_token):
            raise InvalidApiTokenError()
        
        if kwargs.get('service_pk'):
            if not bot.system.services.filter(id=kwargs.get('service_pk')).exists():
                raise PermissionDenied("You don't have permission to access this service")
        
        return True