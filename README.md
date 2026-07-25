# Backend API - Catalogo Musical

## Descripcion General

Esta aplicacion backend, construida con Python y Django REST Framework, constituye el motor y la capa de datos para el sistema de gestion del catalogo musical. Diseñada bajo una arquitectura de API REST pura, esta aplicacion no renderiza ninguna vista HTML, dedicandose exclusivamente al procesamiento de datos, manejo de la base de datos relacional y gestion estricta de la seguridad.

El proyecto destaca por su robusto sistema de autenticacion basado en OAuth 2.0, su configuracion de CORS para la comunicacion segura con el frontend (React), y la capacidad de gestionar archivos multimedia (imagenes de artistas y portadas de albumes).

---

## Caracteristicas Principales

* **API RESTful (CRUD Completo):** Endpoints habilitados para la creacion, lectura, actualizacion y eliminacion de registros (GET, POST, PUT/PATCH, DELETE) para las entidades de Artistas y Albumes.
* **Autenticacion y Seguridad (OAuth 2.0):** Implementacion de django-oauth-toolkit para la emision y validacion de tokens de acceso, protegiendo las rutas privadas de la API.
* **Manejo de Archivos Multimedia:** Soporte nativo para la carga y almacenamiento de imagenes utilizando Pillow.
* **Comunicacion Segura (CORS):** Configuracion de django-cors-headers para permitir el intercambio de recursos con el frontend.
* **Base de Datos Relacional:** Modelado de datos estructurado (Relacion Uno a Muchos) utilizando SQLite.

---

## Tecnologias Utilizadas

* **Core:** Python, Django.
* **API Framework:** Django REST Framework (DRF).
* **Seguridad:** django-oauth-toolkit (OAuth 2.0).
* **CORS:** django-cors-headers.
* **Procesamiento de Imagenes:** Pillow.
* **Base de Datos:** SQLite3.

---

## Estructura del Proyecto

El repositorio sigue una organizacion modular, separando responsabilidades entre aplicaciones, logica de negocio y configuracion:

```text
/BACKEND-CATALOGO
├── /catalogo_musical      # Configuracion principal del proyecto
│   ├── settings.py        # Configuraciones globales, apps, DB, CORS, Media
│   └── urls.py            # Enrutador principal (incluye rutas OAuth y Media)
├── /api                   # Aplicacion central de la API
│   ├── models.py          # Definicion de entidades (Artista, Album) y relaciones
│   ├── serializers.py     # Transformacion de modelos a formato JSON
│   ├── views.py           # Logica de las vistas para el CRUD
│   └── urls.py            # Endpoints especificos de la API (/api/artistas, etc.)
├── /media                 # Directorio de almacenamiento de imagenes subidas
│   ├── /artistas          # Fotos de los artistas
│   └── /albumes           # Portadas de los albumes
├── manage.py              # Script principal de administracion de Django
└── requirements.txt       # Dependencias exactas para replicar el entorno
```

---

## Configuracion de OAuth 2.0 (Para el Frontend)

Para que el proyecto se comunique correctamente con el frontend y permita el inicio de sesion, es necesario generar las credenciales de seguridad de la API:

1. Inicia el servidor y entra a http://localhost:8000/admin.
2. Inicia sesion con el superusuario.
3. Dirigete a la seccion Django OAuth Toolkit > Applications y añade una nueva con los siguientes datos:
   * Client type: Confidential
   * Authorization grant type: Resource owner password-based
   * Name: Frontend React
4. Guarda y proporciona el Client ID y Client Secret al equipo de frontend.

---

## Requisitos Previos e Instalacion

### Requisitos
* Python (v3.10 o superior) instalado en el sistema.
* Editor de codigo recomendado: VS Code.

### Pasos para iniciar el entorno de desarrollo

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd backend-catalogo
   ```

2. **Crear y activar un entorno virtual:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instalar las dependencias del proyecto:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar las migraciones a la base de datos:**
   ```bash
   python manage.py migrate
   ```

5. **Crear un superusuario (Administrador):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

7. **Abrir en el navegador:**
   La terminal indicara la URL local (por lo general http://localhost:8000).

---

## Comandos Utiles (Scripts)

* `python manage.py runserver`: Enciende el servidor local.
* `python manage.py makemigrations`: Prepara los cambios en la base de datos.
* `python manage.py migrate`: Aplica los cambios a la base de datos.
* `pip freeze > requirements.txt`: Actualiza la lista de dependencias del proyecto.

---

## Flujo de Trabajo Git

Comandos basicos para mantener el versionado al dia:

```bash
# Verificar el estado de los archivos modificados
git status

# Agregar todos los cambios al area de preparacion
git add .

# Realizar un commit descriptivo
git commit -m "feat: configuracion de base de datos y endpoints API"

# Enviar los cambios al repositorio remoto
git push
```

---
**Autor:** Nicolás Díaz
