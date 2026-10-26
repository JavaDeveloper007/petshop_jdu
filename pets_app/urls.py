from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from pets_app.api_views import PetViewSet

router = DefaultRouter()
router.register('petshop', PetViewSet, basename='pet')


urlpatterns = [
    path('', views.pet_list, name='pet_list'),
    path('cbv/', views.PetListView.as_view(), name='pet_list_cbv'),
    path('posts/<int:pk>/', views.pet_detail, name='pet_detail'),
    path('posts/create/', views.pet_create, name='pet_create'),
    path('api/', include(router.urls)),
]