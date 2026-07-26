# Backend Catálogo Musical - Django

## Descripción General
Esta aplicación backend, construida con Django y Django REST Framework, constituye el servidor para la gestión de un catálogo musical. Diseñada como proyecto integrador, la plataforma proporciona interfaces para la gestión de Artistas, Álbumes y una sección de Radio (Canciones), implementando un flujo completo de autenticación OAuth 2.0 mediante django-oauth-toolkit.

El proyecto destaca por su arquitectura limpia y modular, siguiendo las mejores prácticas de Django REST Framework con ViewSets y Routers para generar automáticamente las rutas CRUD completas. Implementa autenticación basada en tokens OAuth 2.0, protección de rutas mediante permisos de autenticación, y configuración CORS para permitir el consumo desde el frontend (React/Vite).

## Características Principales
- **Gestión de Catálogo (CRUD Completo)**: Rutas para Artistas, Álbumes y Canciones de Radio con operaciones Create, Read, Update, Delete.
- **Autenticación Segura OAuth 2.0**: Implementación completa con django-oauth-toolkit, emisión de tokens de acceso (Bearer Tokens), refresh tokens y protección de rutas mediante `IsAuthenticated`.
- **Relaciones de Base de Datos**: Modelo relacional Artista (1) → Álbumes (N) con ForeignKey y related_name para consultas inversas eficientes.
- **Servicio de Archivos Multimedia**: Configuración de `MEDIA_URL` y `MEDIA_ROOT` para servir imágenes (portadas, fotos de artistas) y archivos de audio (radio) en desarrollo.
- **Panel de Administración Django**: Modelos registrados en Django Admin para gestión visual de datos.
- **CORS Habilitado**: Configuración `CORS_ALLOW_ALL_ORIGINS = True` para desarrollo frontend desacoplado.
- **Interfaz Navegable (Browsable API)**: Interfaz web interactiva de DRF para probar las rutas directamente desde el navegador.

## Tecnologías Utilizadas
- **Core**: Python 3.x, Django 6.0.7, Django REST Framework 3.17.1
- **Autenticación**: django-oauth-toolkit 3.3.0 (OAuth 2.0), oauthlib 3.3.1
- **Base de Datos**: SQLite3 (desarrollo), compatible con PostgreSQL/MySQL (producción)
- **Archivos Multimedia**: Pillow 12.3.0 (procesamiento de imágenes)
- **CORS**: django-cors-headers 4.9.0
- **Utilidades**: python-dotenv (variables de entorno), cryptography, jwcrypto (JWT/OAuth)

## Estructura del Proyecto
El repositorio sigue la estructura estándar de un proyecto Django, separando la configuración del proyecto (`catalogo_musical`) de la aplicación de negocio (`api`):

```
/PROYECTO-MUSICA
├── /api                          # Aplicación principal (lógica de negocio)
│   ├── /migrations               # Migraciones de base de datos
│   ├── __init__.py
│   ├── admin.py                  # Registro de modelos en Django Admin
│   ├── apps.py
│   ├── models.py                 # Modelos: Artista, Album, CancionRadio
│   ├── serializers.py            # Serializers DRF (ModelSerializer)
│   ├── tests.py
│   ├── urls.py                   # Router DRF + endpoints API
│   └── views.py                  # ViewSets (ModelViewSet) para CRUD automático
├── /catalogo_musical             # Configuración del proyecto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py               # Configuración principal (DB, Auth, CORS, Media, DRF)
│   ├── urls.py                   # URLs raíz: admin, api/, o/ (OAuth)
│   └── wsgi.py
├── /media                        # Archivos subidos por usuarios (imágenes, audio)
│   ├── /albumes
│   ├── /artistas
│   └── /musica_radio
├── .gitignore                    # Archivos ignorados por Git
├── manage.py                     # Script de gestión Django
└── requirements.txt              # Dependencias del proyecto
```

## Modelos de Datos

### Artista
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | AutoField | PK automático |
| nombre | CharField(150) | Nombre del artista |
| genero | CharField(100) | Género musical |
| biografia | TextField | Biografía opcional (blank=True) |
| foto | ImageField | Imagen subida a `media/artistas/` (opcional) |

### Album
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | AutoField | PK automático |
| titulo | CharField(150) | Título del álbum |
| fecha_lanzamiento | DateField | Fecha opcional (null=True, blank=True) |
| portada | ImageField | Imagen subida a `media/albumes/` (opcional) |
| artista | ForeignKey | Relación Many-to-One con Artista (CASCADE, related_name='albumes') |

### CancionRadio
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | AutoField | PK automático |
| titulo | CharField(200) | Título de la canción |
| artista | CharField(200) | Nombre del artista (default: "MeloVerse Stream") |
| archivo_audio | FileField | Archivo de audio subido a `media/musica_radio/` |

## Endpoints de la API (REST)

La API está versionada bajo el prefijo `/api/` y utiliza `DefaultRouter` para generar rutas estándar:

| Recurso | Endpoints Generados | Descripción |
|---------|---------------------|-------------|
| **Artistas** | `GET/POST /api/artistas/` | Listar todos / Crear nuevo |
| | `GET/PUT/PATCH/DELETE /api/artistas/{id}/` | Detalle / Actualizar / Eliminar |
| **Álbumes** | `GET/POST /api/albumes/` | Listar todos / Crear nuevo |
| | `GET/PUT/PATCH/DELETE /api/albumes/{id}/` | Detalle / Actualizar / Eliminar |
| **Radio** | `GET/POST /api/radio/` | Listar canciones / Subir nueva |
| | `GET/PUT/PATCH/DELETE /api/radio/{id}/` | Detalle / Actualizar / Eliminar |

> **Nota**: Todos los endpoints CRUD requieren autenticación OAuth 2.0 (Header: `Authorization: Bearer <access_token>`).

## Endpoints de Autenticación (OAuth 2.0)
Prefijo: `/o/`

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/o/authorize/` | GET | Página de autorización (consentimiento) |
| `/o/token/` | POST | Obtener Access Token + Refresh Token |
| `/o/revoke_token/` | POST | Revocar token |
| `/o/introspect/` | POST | Introspección de token |

**Flujo típico (Password Grant / Client Credentials):**
```bash
# Obtener token (ejemplo con client_credentials)
curl -X POST http://localhost:8000/o/token/ \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials&client_id=TU_CLIENT_ID&client_secret=TU_CLIENT_SECRET"

# Usar token en endpoints protegidos
curl -H "Authorization: Bearer TU_ACCESS_TOKEN" http://localhost:8000/api/artistas/
```

## Variables de Entorno (.env)
Crea un archivo `.env` en la raíz del proyecto (junto a `manage.py`) basado en:

```env
# Configuración Django
SECRET_KEY=tu_clave_secreta_django_muy_larga_y_segura
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Base de datos (SQLite por defecto, cambiar para producción)
# DATABASE_URL=postgres://user:pass@localhost:5432/dbname

# OAuth 2.0 (Credenciales de la aplicación cliente registrada en Django Admin)
OAUTH2_CLIENT_ID=tu_client_id
OAUTH2_CLIENT_SECRET=tu_client_secret

# CORS (para desarrollo)
CORS_ALLOW_ALL_ORIGINS=True
```

> **Nota**: En `settings.py` se usa `SECRET_KEY` hardcodeada para desarrollo. En producción **debe** leerse de variable de entorno.

## Requisitos Previos e Instalación

### Requisitos
- Python 3.10+
- pip y virtualenv (recomendado)
- Git

### Pasos para iniciar el entorno de desarrollo

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd Proyecto-de-musica
   ```

2. **Crear y activar entorno virtual:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno:**
   Copia `.env.example` a `.env` y ajusta valores (ver sección anterior).

5. **Ejecutar migraciones:**
   ```bash
   python manage.py migrate
   ```

6. **Crear superusuario (para Django Admin y registro de aplicación OAuth):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Registrar aplicación OAuth 2.0 (Client):**
   - Inicia el servidor (`python manage.py runserver`)
   - Accede a `http://localhost:8000/admin/`
   - Ve a **OAuth2 Provider > Applications > Add Application**
   - Completa:
     - **Name**: `Frontend Catalogo`
     - **Client type**: `Confidential`
     - **Authorization grant type**: `Resource owner password-based` (o `Client credentials` según tu flujo)
     - **Redirect uris**: `http://localhost:5173/callback` (tu frontend)
   - Guarda y anota **Client ID** y **Client Secret** para tu `.env` frontend.

8. **Ejecutar servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

9. **Verificar:**
   - API: `http://localhost:8000/api/`
   - Admin: `http://localhost:8000/admin/`
   - OAuth: `http://localhost:8000/o/`

## Comandos Útiles (Scripts)

| Comando | Descripción |
|---------|-------------|
| `python manage.py runserver` | Inicia servidor desarrollo (puerto 8000) |
| `python manage.py migrate` | Aplica migraciones pendientes |
| `python manage.py makemigrations` | Crea migraciones tras cambios en models.py |
| `python manage.py createsuperuser` | Crea usuario admin |
| `python manage.py collectstatic` | Recolecta archivos estáticos (producción) |
| `python manage.py test` | Ejecuta tests |
| `python manage.py shell` | Shell interactivo de Django |

## Flujo de Trabajo Git

Comandos básicos para mantener el versionado al día:

```bash
# Verificar el estado de los archivos modificados
git status

# Agregar todos los cambios al área de preparación
git add .

# Realizar un commit descriptivo (Convencional Commits)
git commit -m "feat: agregar endpoint radio y modelo CancionRadio"

# Enviar los cambios al repositorio remoto
git push
```

**Convención de commits sugerida:**
- `feat:` Nueva funcionalidad
- `fix:` Corrección de bug
- `refactor:` Refactorización de código
- `docs:` Cambios en documentación
- `chore:` Tareas de mantenimiento (deps, configs)

## Panel de Administración (Django Admin)
Accesible en `/admin/`. Modelos registrados:
- **Artistas**: Listado, búsqueda por nombre, filtro por género, edición inline de álbumes.
- **Álbumes**: Listado con artista relacionado, filtro por artista.
- **Canciones Radio**: Gestión de pistas de audio.

## Despliegue en Producción (Checklist)
- [ ] `DEBUG = False`
- [ ] `SECRET_KEY` desde variable de entorno
- [ ] `ALLOWED_HOSTS` configurado con dominio real
- [ ] Base de datos PostgreSQL/MySQL (no SQLite)
- [ ] `CORS_ALLOWED_ORIGINS` con dominios específicos (no `CORS_ALLOW_ALL_ORIGINS`)
- [ ] HTTPS obligatorio (OAuth 2.0 lo requiere)
- [ ] `SECURE_SSL_REDIRECT = True`, `SESSION_COOKIE_SECURE = True`, `CSRF_COOKIE_SECURE = True`
- [ ] Archivos estáticos/media servidos por Nginx/CloudStorage (no Django)
- [ ] Variables de entorno seguras (no commitear `.env`)

## Autor
Matthew Constante