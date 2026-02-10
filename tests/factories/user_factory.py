from factory.django import DjangoModelFactory
from factory.faker import Faker

from users.models import User  

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
    
    email = Faker("email")
    password = Faker("password")
    first_name = Faker("first_name")
    last_name = Faker("last_name")