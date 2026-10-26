import pytest
from pets_app.models import Pet

@pytest.mark.django_db
def test_pet_creation():
    pet = Pet.objects.create(name="Barsik", species="Mushuk", age=3)
    assert pet.name == "Barsik"
    assert Pet.objects.count() == 1


@pytest.mark.django_db
def test_pet_str_without_category():
    pet = Pet.objects.create(name="Rex", species="It", age=5)
    assert "Rex" in str(pet)