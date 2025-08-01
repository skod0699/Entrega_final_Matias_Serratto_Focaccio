from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
path('novedades/', include(('novedades.urls', 'novedades'), namespace='novedades')),
    path('pages/', include('pages.urls')),  
    path('accounts/', include('accounts.urls')),
    path('mensajes/', include(('mensajes.urls', 'mensajes'), namespace='mensajes')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
