from django.db import models
from django.urls import reverse

class Page(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('pages:detail', kwargs={'slug': self.slug})
