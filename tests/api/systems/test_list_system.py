import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_empty_list_systems(tenant_client):
    url = reverse("systems-list")
    
    response = tenant_client.get(path=url)
    assert response.status_code == 200
    assert response.data == []
    
@pytest.mark.django_db
def test_list_systems(tenant_client, systems):
    url = reverse("systems-list")
    
    for system in systems:
        print(system)
        system.save()
    
    response = tenant_client.get(path=url)
    assert response.status_code == 200
    assert len(response.data) == 3