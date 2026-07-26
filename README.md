# 🎵 Backend Catálogo Musical - Django

## 📖 Descripción General

Esta aplicación backend, construida con **Django y Django REST Framework**, constituye el servidor para la gestión de un catálogo musical. Diseñada como proyecto integrador, la plataforma proporciona interfaces para la gestión de Artistas, Álbumes y una sección de Radio (Canciones), implementando un flujo completo de autenticación OAuth 2.0 mediante `django-oauth-toolkit`.

El proyecto destaca por su arquitectura limpia y modular, siguiendo las mejores prácticas de Django REST Framework con **ViewSets** y **Routers** para generar automáticamente las rutas CRUD completas. Implementa autenticación basada en tokens OAuth 2.0, protección de rutas mediante permisos de autenticación, y configuración CORS para permitir el consumo desde el frontend (React/Vite).

---

## ✨ Características Principales

- **Gestión de Catálogo (CRUD Completo):** Rutas para Artistas, Álbumes y Canciones de Radio con operaciones Create, Read, Update, Delete.
- **Autenticación Segura OAuth 2.0:** Implementación completa con `django-oauth-toolkit`, emisión de tokens de acceso (Bearer Tokens), refresh tokens y protección de rutas mediante `IsAuthenticated`.
- **Relaciones de Base de Datos:** Modelo relacional Artista (1) → Álbumes (N) con ForeignKey y `related_name` para consultas inversas eficientes.
- **Servicio de Archivos Multimedia:** Configuración de `MEDIA_URL` y `MEDIA_ROOT` para servir imágenes (portadas, fotos de artistas) y archivos de audio (radio) en desarrollo.
- **Panel de Administración Django:** Modelos registrados en Django Admin para gestión visual de datos.
- **CORS Habilitado:** Configuración `CORS_ALLOW_ALL_ORIGINS = True` para desarrollo frontend desacoplado.
- **Interfaz Navegable (Browsable API):** Interfaz web interactiva de DRF para probar las rutas directamente desde el navegador.

---

## 🛠️ Tecnologías Utilizadas

- **Core:** Python 3.x, Django 6.0.7, Django REST Framework 3.17.1
- **Autenticación:** django-oauth-toolkit 3.3.0 (OAuth 2.0), oauthlib 3.3.1
- **Base de Datos:** SQLite3 (desarrollo), compatible con PostgreSQL/MySQL (producción)
- **Archivos Multimedia:** Pillow 12.3.0 (procesamiento de imágenes)
- **CORS:** django-cors-headers 4.9.0
- **Utilidades:** cryptography, jwcrypto (JWT/OAuth), requests

---

## 📂 Estructura del Proyecto

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
├── .env.example                  # Archivo de referencia para variables de entorno
├── .gitignore                    # Archivos ignorados por Git
├── manage.py                     # Script de gestión Django
└── requirements.txt              # Dependencias del proyecto
```

---

## 📊 Modelos de Datos

### Artista
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | AutoField | Identificador único (PK) |
| nombre | CharField(150) | Nombre del artista |
| genero | CharField(100) | Género musical |
| biografia | TextField | Biografía (opcional) |
| foto | ImageField | Imagen subida a `media/artistas/` (opcional) |

### Album
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | AutoField | Identificador único (PK) |
| titulo | CharField(150) | Título del álbum |
| fecha_lanzamiento | DateField | Fecha opcional (null=True, blank=True) |
| portada | ImageField | Imagen subida a `media/albumes/` (opcional) |
| artista | ForeignKey | Relación Many-to-One con Artista |

### CancionRadio
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | AutoField | Identificador único (PK) |
| titulo | CharField(200) | Título de la canción |
| artista | CharField(200) | Nombre del artista (default: "MeloVerse Stream") |
| archivo_audio | FileField | Archivo de audio subido a `media/musica_radio/` |

---

## 🔌 Endpoints de la API (REST)

La API está versionada bajo el prefijo `/api/` y utiliza `DefaultRouter` para generar rutas estándar:

| Recurso | Método | Endpoint | Descripción |
|---------|--------|----------|-------------|
| **Artistas** | GET/POST | `/api/artistas/` | Listar todos / Crear nuevo |
| **Artistas** | GET/PUT/PATCH/DELETE | `/api/artistas/{id}/` | Detalle / Actualizar / Eliminar |
| **Álbumes** | GET/POST | `/api/albumes/` | Listar todos / Crear nuevo |
| **Álbumes** | GET/PUT/PATCH/DELETE | `/api/albumes/{id}/` | Detalle / Actualizar / Eliminar |
| **Radio** | GET/POST | `/api/radio/` | Listar canciones / Subir nueva |
| **Radio** | GET/PUT/PATCH/DELETE | `/api/radio/{id}/` | Detalle / Actualizar / Eliminar |

> **Nota:** Todos los endpoints CRUD requieren autenticación OAuth 2.0 (Header: `Authorization: Bearer <access_token>`).

### Códigos de Respuesta HTTP

| Código | Significado | Descripción |
|--------|------------|-------------|
| 200 | OK | Solicitud exitosa (GET, PUT, PATCH) |
| 201 | Created | Recurso creado exitosamente (POST) |
| 204 | No Content | Eliminado exitosamente (DELETE) |
| 400 | Bad Request | Datos inválidos en la solicitud |
| 401 | Unauthorized | Token expirado, inválido o no proporcionado |
| 403 | Forbidden | Usuario sin permisos (debe estar autenticado) |
| 404 | Not Found | Recurso no existe |
| 500 | Server Error | Error interno del servidor Django |

---

## 🔐 Autenticación y Permisos

Todos los endpoints CRUD en `/api/` requieren:
1. **Bearer Token válido:** Obtenido en `/o/token/`
2. **Header `Authorization`:** `Authorization: Bearer <access_token>`
3. **Token no expirado:** Si expira, obtén uno nuevo

**Respuesta sin autenticación:**
```json
{
  "detail": "Authentication credentials were not provided."
}
```

---

## 🔑 Endpoints de Autenticación (OAuth 2.0)

Prefijo: `/o/`

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/o/authorize/` | GET | Página de autorización (consentimiento) |
| `/o/token/` | POST | Obtener Access Token + Refresh Token |
| `/o/revoke_token/` | POST | Revocar token |
| `/o/introspect/` | POST | Introspección de token |

### Obtener Token con cURL

```bash
curl -X POST http://localhost:8000/o/token/ \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials&client_id=TU_CLIENT_ID&client_secret=TU_CLIENT_SECRET"
```

**Usar token en endpoints protegidos:**

```bash
curl -H "Authorization: Bearer TU_ACCESS_TOKEN" http://localhost:8000/api/artistas/
```

---

## 📮 Usando Postman para obtener y usar tokens

### 1️⃣ Obtener Access Token

- Crea un nuevo request **POST** en Postman
- URL: `http://localhost:8000/o/token/`
- Tab **Body** → Select **x-www-form-urlencoded**
- Agrega estos parámetros:
  - `grant_type`: `client_credentials`
  - `client_id`: `TU_CLIENT_ID` (del Django Admin)
  - `client_secret`: `TU_CLIENT_SECRET` (del Django Admin)
- Click **Send**
- Copia el valor de `access_token` de la respuesta JSON

### 2️⃣ Usar el Token en Requests Protegidos

- Abre cualquier request de la API
- Tab **Authorization**
- Type: **Bearer Token**
- Token: Pega el `access_token`
- Click **Send**

### 3️⃣ Alternativa: Variables de Entorno en Postman

**Pre-request Script** (en el token request):
```javascript
var jsonData = pm.response.json();
pm.environment.set("access_token", jsonData.access_token);
```

Luego en otros requests, usa: `{{access_token}}`

### 4️⃣ Ejemplos CRUD con Postman

| Acción | Método | URL | Body |
|--------|--------|-----|------|
| Listar artistas | GET | `/api/artistas/` | - |
| Crear artista | POST | `/api/artistas/` | `{"nombre": "Coldplay", "genero": "Rock"}` |
| Obtener artista | GET | `/api/artistas/1/` | - |
| Actualizar artista | PUT | `/api/artistas/1/` | `{"nombre": "Coldplay", "genero": "Pop Rock"}` |
| Eliminar artista | DELETE | `/api/artistas/1/` | - |
| Listar álbumes | GET | `/api/albumes/` | - |
| Crear álbum | POST | `/api/albumes/` | `{"titulo": "Parachutes", "artista": 1}` |

> **Tip:** En requests con archivos, cambia **Body** a **form-data** en lugar de JSON.

---

## ⚙️ Variables de Entorno (.env)

Crea un archivo `.env` en la raíz del proyecto (junto a `manage.py`):

```env
# Configuración Django
SECRET_KEY=tu_clave_secreta_django_muy_larga_y_segura
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Base de datos (SQLite por defecto)
# DATABASE_URL=postgres://user:pass@localhost:5432/dbname

# OAuth 2.0
OAUTH2_CLIENT_ID=tu_client_id
OAUTH2_CLIENT_SECRET=tu_client_secret

# CORS
CORS_ALLOW_ALL_ORIGINS=True
```

> **⚠️ Notas Importantes:**
> - `SECRET_KEY` debe leerse de variables de entorno en producción
> - `ALLOWED_HOSTS` debe incluir `localhost` y `127.0.0.1` para desarrollo local
> - Las credenciales OAuth 2.0 se obtienen después de registrar la aplicación en Django Admin

---

## 🚀 Requisitos Previos e Instalación

### Requisitos

- Python 3.10+
- pip y virtualenv (recomendado)
- Git
- **Postman** (para probar la API y obtener tokens OAuth)

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
   pip install python-dotenv  # Recomendado (no incluido en requirements.txt)
   ```

4. **Configurar variables de entorno:**
   ```bash
   cp .env.example .env  # O crear .env manualmente
   ```

5. **Ejecutar migraciones:**
   ```bash
   python manage.py migrate
   ```

6. **Crear superusuario:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Registrar aplicación OAuth 2.0:**
   - Inicia el servidor: `python manage.py runserver`
   - Ve a: `http://localhost:8000/admin/`
   - OAuth2 Provider > Applications > Add Application
   - Completa:
     - **Name:** `Frontend Catalogo`
     - **Client type:** `Confidential`
     - **Authorization grant type:** `Resource owner password-based` o `Client credentials`
     - **Redirect uris:** `http://localhost:5173/callback` (tu frontend)
   - Guarda y copia **Client ID** y **Client Secret**

8. **Ejecutar servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

9. **Verificar acceso:**
   - API: `http://localhost:8000/api/`
   - Admin: `http://localhost:8000/admin/`
   - OAuth: `http://localhost:8000/o/`
   - Postman: Importa los endpoints o crea requests manualmente

---

## 💻 Comandos Útiles (Scripts)

| Comando | Descripción |
|---------|-------------|
| `python manage.py runserver` | Inicia servidor desarrollo (puerto 8000) |
| `python manage.py migrate` | Aplica migraciones pendientes |
| `python manage.py makemigrations` | Crea migraciones tras cambios en models.py |
| `python manage.py createsuperuser` | Crea usuario admin |
| `python manage.py collectstatic` | Recolecta archivos estáticos (producción) |
| `python manage.py test` | Ejecuta tests |
| `python manage.py shell` | Shell interactivo de Django |

---

## 🌿 Flujo de Trabajo Git

Comandos básicos para mantener el versionado al día:

```bash
# Verificar estado de cambios
git status

# Agregar cambios al área de preparación
git add .

# Realizar commit descriptivo
git commit -m "feat: agregar endpoint radio y modelo CancionRadio"

# Enviar cambios al repositorio remoto
git push
```

**Convención de commits sugerida:**
- `feat:` Nueva funcionalidad
- `fix:` Corrección de bug
- `refactor:` Refactorización de código
- `docs:` Cambios en documentación
- `chore:` Tareas de mantenimiento

---

## 🛑 Troubleshooting Común

### ❌ "ModuleNotFoundError: No module named 'python_dotenv'"
```bash
pip install python-dotenv
```

### ❌ "OperationalError: no such table: api_artista"
```bash
python manage.py migrate
```

### ❌ "ImproperlyConfigured: ALLOWED_HOSTS is empty"
Verifica que `ALLOWED_HOSTS` esté configurado en `settings.py` o `.env`:
```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
```

### ❌ "No module named 'rest_framework'"
```bash
pip install -r requirements.txt
```

### ❌ Los tokens de Postman no funcionan
1. Verifica que registraste la aplicación OAuth 2.0 en Django Admin
2. Usa **Bearer Token** type (no "Basic Auth") en Postman
3. Verifica que el token sea válido (no expirado)
4. Obtén uno nuevo en `/o/token/` si es necesario

### ❌ "CORS policy: blocked request" desde el frontend
Verifica que en `settings.py` esté:
```python
CORS_ALLOW_ALL_ORIGINS = True  # Desarrollo
CORS_ALLOWED_ORIGINS = ['http://localhost:5173']  # Producción
```

---

## 📋 Despliegue en Producción

- [ ] `DEBUG = False`
- [ ] `SECRET_KEY` desde variable de entorno
- [ ] `ALLOWED_HOSTS` con dominio real
- [ ] Base de datos PostgreSQL/MySQL
- [ ] `CORS_ALLOWED_ORIGINS` con dominios específicos
- [ ] HTTPS obligatorio (OAuth 2.0)
- [ ] `SECURE_SSL_REDIRECT = True`
- [ ] Archivos estáticos/media por Nginx/S3
- [ ] Variables de entorno seguras (no commitear `.env`)

---

**Autor:** Nicolás Diaz
