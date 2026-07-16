from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Este es el camino para el panel de administrador (ya viene por defecto)
    path('admin/', admin.site.urls),
    # ¡Esta es la línea clave! 
    # Aquí le decimos a Django: "Oye, cuando alguien en internet escriba '/api/' 
    # en la barra de direcciones, envíalo a leer el mapa de rutas que 
    # nosotros creamos adentro de la carpeta 'api'."
    path('api/', include('api.urls')),
    
    # NUEVO: Esta es la puerta para nuestro guardia de seguridad.
    # Cuando React necesite un Token, vendrá a esta dirección ('/o/').
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]