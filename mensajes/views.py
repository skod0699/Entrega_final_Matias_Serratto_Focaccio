from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Mensaje
from django.contrib.auth.models import User

class MensajeListView(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'mensajes/mensaje_list.html'

    def get_queryset(self):
        # Mostrar solo mensajes donde el usuario sea destinatario
        return Mensaje.objects.filter(destinatario=self.request.user).order_by('-fecha_envio')

class MensajeDetailView(LoginRequiredMixin, DetailView):
    model = Mensaje
    template_name = 'mensajes/mensaje_detail.html'

    def get_queryset(self):
        # Solo mensajes donde el usuario sea destinatario (o también remitente si quieres)
        return Mensaje.objects.filter(destinatario=self.request.user)

class MensajeCreateView(LoginRequiredMixin, CreateView):
    model = Mensaje
    fields = ['destinatario', 'asunto', 'contenido']
    template_name = 'mensajes/mensaje_form.html'
    success_url = reverse_lazy('mensajes:lista')

    def form_valid(self, form):
        form.instance.remitente = self.request.user
        return super().form_valid(form)
