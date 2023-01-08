from django.contrib import admin
from django.urls import include, path
from Web.views import index
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),

    path('components/', include('components.urls')),
    path('publications/', include('publications.urls')),
    path('users/', include('users.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)