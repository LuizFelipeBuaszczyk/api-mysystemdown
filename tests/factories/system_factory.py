from factory.django import DjangoModelFactory
from factory.faker import Faker

from systems.models import System

class SystemFactory(DjangoModelFactory):
    class Meta:
        model = System

    name = Faker("name")
    description = Faker("text")