from django.db import models

# Definimos el modelo 'Artista', que hereda de 'models.Model'. 
# Esto le dice a Django que cree una tabla en la base de datos para almacenar artistas.
class Artista(models.Model):
    # 'nombre' es un campo de caracteres (cadena de texto). 
    # 'max_length=150' restringe la longitud máxima del nombre a 150 caracteres.
    nombre = models.CharField(max_length=150)
    
    # 'genero' es otro campo de texto corto, limitado a 100 caracteres.
    genero = models.CharField(max_length=100)
    
    # 'biografia' es un campo de texto largo sin límite de caracteres específico.
    # 'blank=True' indica que este campo es opcional y puede dejarse vacío en los formularios.
    biografia = models.TextField(blank=True)

    # El método especial __str__ define la representación en forma de cadena del objeto.
    # Gracias a esto, en el panel de administración de Django verás el nombre del 
    # artista en lugar de algo genérico como "Artista object (1)".
    def __str__(self):
        return self.nombre


# Definimos el modelo 'Album', que creará una tabla en la base de datos para los álbumes.
class Album(models.Model):
    # Título del álbum, limitado a 150 caracteres.
    titulo = models.CharField(max_length=150)
    
    # 'fecha_lanzamiento' es un campo que solo almacena fechas (año, mes, día).
    fecha_lanzamiento = models.DateField()
    
    # Esta es la línea clave que crea la relación "Uno a Muchos" (Un artista -> Muchos álbumes).
    # - ForeignKey: Establece que este campo es una clave foránea hacia el modelo 'Artista'.
    # - on_delete=models.CASCADE: Si un Artista es eliminado de la base de datos, 
    #   Django eliminará en cascada (automáticamente) todos los Álbumes asociados a él.
    # - related_name='albumes': Crea una relación inversa. Te permite buscar todos los 
    #   álbumes de un artista específico usando algo como `mi_artista.albumes.all()`.
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='albumes')

    # Retorna una cadena formateada (f-string) que muestra el título del álbum 
    # seguido de un guion y el nombre del artista asociado.
    def __str__(self):
        return f"{self.titulo} - {self.artista.nombre}"