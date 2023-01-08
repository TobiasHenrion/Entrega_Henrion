from django.urls import path
from components.views import list_components, create_components

urlpatterns = [
    path('list_components/', list_components),
    path('create_components/', create_components),
]