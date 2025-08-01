from django.urls import path
from . import views

app_name = 'mensajes'

urlpatterns = [
    path('', views.MensajeListView.as_view(), name='lista'),
    path('enviar/', views.MensajeCreateView.as_view(), name='enviar'),
    path('<int:pk>/', views.MensajeDetailView.as_view(), name='detalle'),
]
