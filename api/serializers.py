# 1. TRAEMOS LAS HERRAMIENTAS
# Importamos la herramienta 'serializers' desde la librería de Django REST Framework.
# Esta es la "máquina" que sabe cómo hacer la traducción de Python a JSON y viceversa.
from rest_framework import serializers

# Importamos nuestros "moldes" (modelos) Artista y Album desde el archivo models.py.
# El punto (.) antes de models es muy importante: le dice a Python "busca el archivo models.py 
# exactamente en la misma carpeta donde estamos parados ahora mismo".
from .models import Artista, Album


# 2. CREAMOS EL TRADUCTOR PARA EL ARTISTA
# Creamos una clase llamada ArtistaSerializer. Al poner (serializers.ModelSerializer) entre paréntesis, 
# le estamos diciendo a Django: "Quiero que uses tu traductor automático para modelos". 
# Esto nos ahorra tener que escribir a mano cada línea que queremos traducir.
class ArtistaSerializer(serializers.ModelSerializer):
    
    # La clase 'Meta' funciona como el panel de control o menú de configuraciones de ESTE traductor.
    # Aquí es donde le damos las instrucciones exactas de qué y cómo traducir.
    class Meta:
        # Instrucción 1: "Oye traductor, la información que vas a leer viene del modelo Artista".
        model = Artista
        
        # Instrucción 2: "Quiero que empaquetes y traduzcas TODOS los campos".
        # '__all__' es una palabra mágica que incluye: nombre, genero, biografia y también 
        # el 'id' (el número único oculto que Django le da a cada artista automáticamente).
        fields = '__all__'


# 3. CREAMOS EL TRADUCTOR PARA EL ÁLBUM
# Hacemos exactamente el mismo proceso, pero ahora diseñado para los discos.
class AlbumSerializer(serializers.ModelSerializer):
    
    class Meta:
        # Le decimos que este traductor específico solo se encargará del modelo Album.
        model = Album
        
        # Le pedimos que traduzca todos los campos. ¡Ojo aquí! Como pusimos '__all__', 
        # este traductor también va a incluir el campo de la clave foránea (el artista dueño del álbum),
        # mostrándolo generalmente como el número de 'id' del artista.
        fields = '__all__'