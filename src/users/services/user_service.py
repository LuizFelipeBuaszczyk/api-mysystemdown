from users.repositories.user_repository import UserRepository
from users.models import User
from django.contrib.auth.models import Group

class UserService:
    
    @staticmethod
    def create_user(data: dict):
        group = Group.objects.get(name="user_base")
        
        #TODO: Após implementar a verificação do email, remover essa linha
        data['is_verified'] = True
        user = UserRepository.create_user(data)                
        user.groups.add(group)
        return user
    
    @staticmethod
    def get_user_by_email(email: str):
        return UserRepository.get_user_by_email(email)