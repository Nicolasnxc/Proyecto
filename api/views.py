# Importamos la herramienta de Django REST que nos regala todo el CRUD ya hecho.
# Es como una plantilla mágica que ya sabe cómo Crear, Leer, Editar y Borrar.
from rest_framework import viewsets

# Traemos nuestros modelos (las tablas de la base de datos)
# El punto (.) significa "búscalo en esta misma carpeta"
from .models import Artista, Album

# Traemos los traductores que hicimos en el paso anterior
from .serializers import ArtistaSerializer, AlbumSerializer

# Creamos la "vista" (el mesero) para los Artistas. 
# Al ponerle '(viewsets.ModelViewSet)', le damos los poderes del CRUD automático.
class ArtistaViewSet(viewsets.ModelViewSet):
    
    # 'queryset' le dice de dónde va a sacar la información.
    # Aquí le decimos: "Ve a la base de datos y trae TODOS los artistas guardados".
    queryset = Artista.objects.all()
    
    # 'serializer_class' le dice qué traductor va a usar.
    # Le decimos: "Usa el traductor de artistas para convertir los datos a JSON".
    serializer_class = ArtistaSerializer


# Hacemos exactamente lo mismo para la tabla de Álbumes
class AlbumViewSet(viewsets.ModelViewSet):
    
    # Le decimos que busque y traiga todos los álbumes guardados en la base de datos
    queryset = Album.objects.all()
    
    # Le asignamos su traductor correspondiente de álbumes
    serializer_class = AlbumSerializer