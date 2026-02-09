import pytest
import json
from django.urls import reverse

@pytest.mark.django_db
def test_create_user_success(public_tenant_client, user_post_data):
    url = reverse("users-list")
    
    response = public_tenant_client.post(
        path=url, 
        data=json.dumps(user_post_data), 
        content_type="application/json"
        )

    assert response.status_code == 201
    assert response.data["email"] == user_post_data["email"]

