from django.urls import path
from .views import HomeView, AboutView, BlogCafeListView, PostDetailView

app_name = 'novedades'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),               # Ruta para Home '/'
    path('about/', AboutView.as_view(), name='about'),       # Ruta para About '/about/'
    path('pages/', BlogCafeListView.as_view(), name='list'), # Ruta para listado de posts '/pages/'
    path('pages/<int:pk>/', PostDetailView.as_view(), name='detail'),  # Detalle post '/pages/<id>/'
]
