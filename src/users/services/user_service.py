from users.repositories.user_repository import UserRepository
from django.conf import settings
from django.contrib.auth.models import Group

from utils.token import create_token_jwt
from utils.logger import get_logger
from infra.email.email import Email, EmailType

logger = get_logger(__name__)

class UserService:
    
    @staticmethod
    def create_user(data: dict):
        logger.info(f"Starting service create_user - email: {data['email']}")
        group = Group.objects.get(name="user_base")
        
        user = UserRepository.create_user(data)  
        
        confirmation_token = create_token_jwt({"id": str(user.id)})
        context = {
            "username": user.first_name + " " + user.last_name,
            "confirmation_url": f"{settings.DOMAIN_URL}/auth/confirm-email?token={confirmation_token}"
        }
        Email.send_email("Verify your email", user.email, EmailType.CONFIRM_EMAIL_USER, context)
        user.groups.add(group)
        return user
    
    @staticmethod
    def get_user_by_email(email: str):
        return UserRepository.get_user_by_email(email)