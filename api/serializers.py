# Primero, traemos la herramienta de Django REST Framework que hace las traducciones
from rest_framework import serializers

# Luego, importamos nuestros modelos Artista y Album desde el archivo models.py
# El punto (.) antes de models significa "en esta misma carpeta"
from .models import Artista, Album

# Creamos el traductor para la tabla Artista
class ArtistaSerializer(serializers.ModelSerializer):
    
    # La clase Meta es como las "configuraciones" de nuestro traductor
    class Meta:
        # Aquí le decimos: "Oye, quiero que traduzcas la información del modelo Artista"
        model = Artista
        
        # Con '__all__' le decimos: "Por favor, traduce absolutamente todos los campos 
        # que creamos en models.py (el id, nombre, genero, biografia)"
        fields = '__all__'


# Hacemos exactamente lo mismo para la tabla Album
class AlbumSerializer(serializers.ModelSerializer):
    
    class Meta:
        # Aquí le decimos que el modelo a traducir es Album
        model = Album
        
        # Y también queremos que traduzca todos los campos (titulo, fecha, etc.)
        fields = '__all__'