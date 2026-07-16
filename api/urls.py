# Importamos las herramientas de Django para crear las rutas de internet
from django.urls import path, include

# Importamos un 'Router'. Es como un mapa inteligente.
# En lugar de escribir nosotros la ruta de Crear, la de Borrar, la de Editar...
# el Router las crea todas automáticamente por nosotros.
from rest_framework.routers import DefaultRouter

# Importamos las vistas (los meseros) que acabamos de crear
from . import views

# Creamos nuestro mapa inteligente
router = DefaultRouter()

# Registramos nuestras puertas en el mapa. 
# Si alguien entra a la ruta '/artistas', lo atiende el ArtistaViewSet
router.register(r'artistas', views.ArtistaViewSet)

# Si alguien entra a la ruta '/albumes', lo atiende el AlbumViewSet
router.register(r'albumes', views.AlbumViewSet)

# Aquí armamos la lista final de direcciones de nuestra aplicación
urlpatterns = [
    # Le decimos a Django: "Incluye aquí todas las rutas que el mapa creó solito"
    path('', include(router.urls)),
]