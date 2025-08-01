from django.db import models
from django.utils import timezone


class Post(models.Model):
    titulo = models.CharField("Título", max_length=200)
    contenido = models.TextField("Contenido")
    imagen = models.ImageField("Imagen", upload_to='posts/', blank=True, null=True)
    fecha = models.DateTimeField("Fecha de publicación", default=timezone.now)
    destacado = models.BooleanField(default=False)  # Nuevo campo

    def __str__(self):
        return self.titulo
