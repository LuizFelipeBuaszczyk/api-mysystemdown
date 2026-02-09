import pytest

@pytest.fixture
def system_post_data():
    return {
        "name": "System 1",
        "description": "System 1 description"
    }