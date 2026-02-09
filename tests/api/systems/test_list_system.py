import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_list_systems(tenant_client):
    url = reverse("systems-list")
    
    response = tenant_client.get(path=url)
    print(response)
    assert response.status_code == 200