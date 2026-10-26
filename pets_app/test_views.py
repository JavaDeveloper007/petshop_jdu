import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.django_db
def test_pet_create_requires_login(client):
    response = client.get(reverse('pet_create'))
    assert response.status_code == 302
    assert '/accounts/login/' in response.url

@pytest.mark.django_db
def test_pet_detail_requires_login(client):
    response = client.get(reverse('pet_detail', kwargs={'pk': 1}))
    assert response.status_code == 302
    assert '/accounts/login/' in response.url

    
@pytest.mark.django_db
def test_pet_list_returns_200(client):
    user = User.objects.create_user(username="tester", password="pass12345")
    client.force_login(user)

    response = client.get(reverse('pet_list'))

    assert response.status_code == 200
