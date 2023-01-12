from django.urls import path
from .views import create_publications, list_publications


urlpatterns = [
    path('create_publications/', create_publications),
    path('list_publications/', list_publications),
]