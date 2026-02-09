import pytest
import json
from django.urls import reverse

@pytest.mark.django_db
def test_create_tenant_success(public_auth_client, tenant_post_data):
    url = reverse("tenants-list")
    response = public_auth_client.post(
        path=url, 
        data=json.dumps(tenant_post_data), 
        content_type="application/json"
        )

    assert response.status_code == 201
    
    