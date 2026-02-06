from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from iam.exceptions import InvalidCredentialsError, UserInactiveError, AccountNotVerifiedError

from config.exceptions import BusinessRuleError
from systems.repositories.bot_repository import BotRepository

class AuthService:
    
    @staticmethod
    def login(data: dict):
        email = data.get("email")
        password = data.get("password")
        
        user = authenticate(email=email, password=password)
        if not user:
            raise InvalidCredentialsError("Invalid email or password")
        if not user.is_active:
            raise UserInactiveError("User is inactive")
        if not user.is_verified:
            raise AccountNotVerifiedError("User is not verified")
        
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        
        return {
            "access_token": access_token,
            "refresh": str(refresh)
        }
        
    @staticmethod
    def refresh_token(data: dict):
        try:
            refresh = RefreshToken(data["refresh"])

            return {
                "access": str(refresh.access_token),
                "refresh": str(refresh),  
            }

        except TokenError:
            raise BusinessRuleError("Refresh token inválido ou expirado")