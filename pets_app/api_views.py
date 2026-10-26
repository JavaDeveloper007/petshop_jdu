from rest_framework import viewsets
from .models import Pet
from .serializers import PetSerializer

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.select_related('category').all()
    serializer_class = PetSerializer