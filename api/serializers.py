# 1. TRAEMOS LAS HERRAMIENTAS
# Importamos la herramienta 'serializers' desde la librería de Django REST Framework.
# Esta es la "máquina" que sabe cómo hacer la traducción de Python a JSON y viceversa.
from rest_framework import serializers

# Importamos nuestros "moldes" (modelos) Artista, Album y AHORA CancionRadio desde el archivo models.py.
# El punto (.) antes de models le dice a Python "busca el archivo models.py en esta misma carpeta".
from .models import Artista, Album, CancionRadio


# 2. CREAMOS EL TRADUCTOR PARA EL ARTISTA
# Creamos una clase llamada ArtistaSerializer. Al poner (serializers.ModelSerializer) entre paréntesis, 
# le estamos diciendo a Django: "Quiero que uses tu traductor automático para modelos". 
class ArtistaSerializer(serializers.ModelSerializer):
    
    # La clase 'Meta' funciona como el panel de control o menú de configuraciones de ESTE traductor.
    class Meta:
        # Instrucción 1: "Oye traductor, la información que vas a leer viene del modelo Artista".
        model = Artista
        
        # Instrucción 2: "Quiero que empaquetes y traduzcas TODOS los campos".
        # '__all__' es una palabra mágica que incluye: nombre, genero, biografia y también el 'id'.
        fields = '__all__'


# 3. CREAMOS EL TRADUCTOR PARA EL ÁLBUM
# Hacemos exactamente el mismo proceso, pero ahora diseñado para los discos.
class AlbumSerializer(serializers.ModelSerializer):
    
    class Meta:
        # Le decimos que este traductor específico solo se encargará del modelo Album.
        model = Album
        
        # Le pedimos que traduzca todos los campos, incluyendo la clave foránea del artista.
        fields = '__all__'


# 4. CREAMOS EL TRADUCTOR PARA LA RADIO
# Y aquí está nuestro nuevo traductor, totalmente independiente y pegado a la izquierda.
class CancionRadioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CancionRadio
        fields = '__all__'