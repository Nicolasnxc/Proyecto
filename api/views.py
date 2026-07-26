# Importamos la herramienta de Django REST que nos regala todo el CRUD ya hecho.
# Es como una plantilla mágica que ya sabe cómo Crear, Leer, Editar y Borrar.
from rest_framework import viewsets

from rest_framework.permissions import AllowAny 
# Traemos nuestros modelos (las tablas de la base de datos)
# AQUÍ ESTÁ LA CORRECCIÓN: Agregamos CancionRadio a la lista activa de importaciones
from .models import Artista, Album, CancionRadio

# Traemos los traductores que hicimos en el paso anterior
# AQUÍ ESTÁ LA CORRECCIÓN: Agregamos CancionRadioSerializer a la lista
from .serializers import ArtistaSerializer, AlbumSerializer, CancionRadioSerializer

# ==========================================
# 1. VISTA PARA ARTISTAS
# ==========================================
# Creamos la "vista" (el mesero) para los Artistas. 
# Al ponerle '(viewsets.ModelViewSet)', le damos los poderes del CRUD automático.
class ArtistaViewSet(viewsets.ModelViewSet):
    
    # 'queryset' le dice de dónde va a sacar la información.
    # Aquí le decimos: "Ve a la base de datos y trae TODOS los artistas guardados".
    queryset = Artista.objects.all()
    
    # 'serializer_class' le dice qué traductor va a usar.
    # Le decimos: "Usa el traductor de artistas para convertir los datos a JSON".
    serializer_class = ArtistaSerializer


# ==========================================
# 2. VISTA PARA ÁLBUMES
# ==========================================
# Hacemos exactamente lo mismo para la tabla de Álbumes
class AlbumViewSet(viewsets.ModelViewSet):
    
    # Le decimos que busque y traiga todos los álbumes guardados en la base de datos
    queryset = Album.objects.all()
    
    # Le asignamos su traductor correspondiente de álbumes
    serializer_class = AlbumSerializer


# ==========================================
# 3. NUEVA VISTA PARA LA RADIO
# ==========================================
# Igual de independiente y alineada a la izquierda que las otras dos.
class CancionRadioViewSet(viewsets.ModelViewSet):
    queryset = CancionRadio.objects.all()
    serializer_class = CancionRadioSerializer
    permission_classes = [AllowAny]  