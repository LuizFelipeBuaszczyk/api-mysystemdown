import pytest
from tests.factories.user_factory import UserFactory

@pytest.fixture
def user():
    return UserFactory.build()

@pytest.fixture
def users():
    return UserFactory.build_batch(size=3)

@pytest.fixture
def user_post_data():
    """Payload base para o endpoint de criação de usuário"""
    return {
        "email": "nM2Y8@example.com",
        "password": "password",
        "first_name": "John",
        "last_name": "Doe"
    }