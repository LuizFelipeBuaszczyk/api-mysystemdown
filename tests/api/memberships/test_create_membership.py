import pytest
import json
from django.urls import reverse
from django_tenants.utils import schema_context

from iam.models import Membership
from users.models import User

@pytest.mark.django_db
def test_create_membership_success(tenant_client, membership_post_data):
    user = membership_post_data["user"]
    
    with schema_context(tenant_client.tenant.schema_name):
        user.save()
    
    membership_post_data["user"] = user.id
        
    url = reverse("tenant-memberships-list")
    
    response = tenant_client.post(
        path=url, 
        data=membership_post_data, 
        content_type="application/json"
        )

    assert response.status_code == 201

    membership = Membership.objects.get(id=response.data["id"])
    assert membership is not None
    assert membership.user.id == membership_post_data["user"]
    assert membership.group.id == membership_post_data["group"]
    