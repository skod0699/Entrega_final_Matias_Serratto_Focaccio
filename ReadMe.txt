Café Artesano - Proyecto Django
==============================

Este es un proyecto web desarrollado en Django que funciona como blog y gestión de novedades sobre café artesanal. Incluye sistema de usuarios, perfiles, mensajes y más.

Requisitos
----------
- Python 3.8 o superior
- Virtualenv (entorno virtual)
- Git (opcional, para clonar el repositorio)

Instalación
-----------
1. Clona el repositorio (si usas Git):
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio

2. Crea y activa un entorno virtual:
   - Windows (PowerShell):
     python -m venv venv
     .\venv\Scripts\activate

   - Linux / Mac:
     python3 -m venv venv
     source venv/bin/activate

3. Instala las dependencias:
   pip install -r requirements.txt

4. Aplica las migraciones:
   python manage.py migrate

5. (Opcional) Crea un superusuario para el admin:
   python manage.py createsuperuser

6. Ejecuta el servidor de desarrollo:
   python manage.py runserver

Uso
---
- Accede al sitio en http://127.0.0.1:8000/novedades/
- Regístrate o inicia sesión en /accounts/signup/ y /accounts/login/
- Edita tu perfil en /accounts/profile/
- Consulta novedades en /novedades/
- Administra mensajes en /mensajes/

Notas
-----
- Las imágenes se almacenan en la carpeta /media/
- En modo DEBUG se sirven automáticamente archivos estáticos y media
- Para producción, configurar variables de entorno y usar un servidor WSGI/ASGI

Autor
-----
Matías Serratto Focaccio

Licencia
--------
Este proyecto es para uso educativo y personal.

