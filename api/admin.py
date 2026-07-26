from django.contrib import admin
from .models import Artista, Album, CancionRadio

# Registramos nuestras tablas para que aparezcan en el panel de control
admin.site.register(Artista)
admin.site.register(Album)
admin.site.register(CancionRadio) # ¡Con esto ya puedes subir música!