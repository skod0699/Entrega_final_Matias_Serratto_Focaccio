from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'destacado')    # Muestra la columna 'destacado'
    list_editable = ('destacado',)                      # Permite editar 'destacado' desde el listado
