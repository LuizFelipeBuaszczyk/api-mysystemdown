import pytest
from tests.factories.user_factory import UserFactory
from iam.models import Membership
from django.contrib.auth.models import Group

@pytest.fixture
def memberships(users, tenant1):
    list = []

    list.append(Membership(user=users[0], group=Group.objects.get(name="admin"), tenant=tenant1))
    list.append(Membership(user=users[1], group=Group.objects.get(name="viewer"), tenant=tenant1))

    return list

@pytest.fixture
def membership_post_data(user):        
    return {
        "user": user,
        "group": 4
    }