from django.contrib import admin
from django.urls import include, path
from Web.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),

    path('components/', include('components.urls')),
    path('publications/', include('publications.urls')),
    path('users/', include('users.urls')),
]
