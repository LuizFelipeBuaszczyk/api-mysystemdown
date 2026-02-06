from uuid import UUID

from users.models import User

class UserRepository:
    
    @staticmethod
    def create_user(data: dict) -> User:
        password = data.pop("password")
        user = User(**data)
        user.set_password(password)
        user.save()
        return user
    
    @staticmethod
    def get_user_by_email(email: str):
        return User.objects.filter(email=email).values()