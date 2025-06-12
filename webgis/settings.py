import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, '.env'))

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# GDAL and PROJ Setup for Windows

if os.name == 'nt':
    try:
        # Get the project root directory (two levels up from settings.py)
        PROJECT_ROOT = BASE_DIR.parent
        # Set the virtual environment path relative to project root
        VENV_BASE = os.path.join(PROJECT_ROOT, 'env')
        
        # Add osgeo to system path
        osgeo_path = os.path.join(VENV_BASE, 'Lib', 'site-packages', 'osgeo')
        if os.path.exists(osgeo_path):
            os.environ['PATH'] = osgeo_path + ';' + os.environ['PATH']
            
            # Set PROJ_LIB path
            proj_lib_path = os.path.join(osgeo_path, 'data', 'proj')
            if os.path.exists(proj_lib_path):
                os.environ['PROJ_LIB'] = proj_lib_path
                
            # Set GDAL and GEOS library paths
            GDAL_LIBRARY_PATH = os.path.join(osgeo_path, 'gdal304.dll')
            GEOS_LIBRARY_PATH = os.path.join(osgeo_path, 'geos_c.dll')
            
            # Verify the DLL files exist
            if not os.path.exists(GDAL_LIBRARY_PATH):
                raise Exception(f"GDAL library not found at: {GDAL_LIBRARY_PATH}")
            if not os.path.exists(GEOS_LIBRARY_PATH):
                raise Exception(f"GEOS library not found at: {GEOS_LIBRARY_PATH}")
        else:
            raise Exception(f"OSGeo directory not found at: {osgeo_path}")
            
    except Exception as e:
        print(f"Error setting up GDAL: {str(e)}")
        raise Exception("Error setting up GDAL environment variables.")

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# Security
SECRET_KEY = 'django-insecure-)o@zt3m3vv-07#+t%hj=r1zof136=5w7n^10v-6-wz++%fs9*e'

# Debug configuration
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

if os.environ.get('RUN_MAIN') == 'true':
    print(f"DEVELOPMENT mode is: {os.environ.get('DEVELOPMENT')}")
    print(f"DEBUG mode is: {DEBUG}")

# ALLOWED_HOSTS configuration
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
ALLOWED_HOSTS = [
    'webgisbackend-zivl.onrender.com',
    'localhost',
    '127.0.0.1',
    
]

# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'rest_framework',
    'rest_framework_gis',
    'corsheaders',
    'myapp',
    'django_extensions',  # Use only in development
]

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Should be as high as possible
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL Configurations
ROOT_URLCONF = 'webgis.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI Application
WSGI_APPLICATION = 'webgis.wsgi.application'

# Database
if os.environ.get('DEVELOPMENT', '').lower() == 'true':
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'webgis',
            'USER': 'postgres',
            'PASSWORD': '123456',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
else:
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://webgis_db_user:o1UikokIgyghbfN2LcCeXb91d0c76FiO@dpg-d0uroi6mcj7s73ab5d60-a.frankfurt-postgres.render.com/webgis_db')
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            engine='django.contrib.gis.db.backends.postgis'
        )
    }

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static and Media Files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Simplified static file serving
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# WhiteNoise configuration
WHITENOISE_USE_FINDERS = True
WHITENOISE_MANIFEST_STRICT = False
WHITENOISE_ALLOW_ALL_ORIGINS = True

# Default Primary Key Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS Settings


# CORS Settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # پورت پیش‌فرض Vite
    "http://127.0.0.1:5173",
    "http://localhost:3000",  # پورت Create React App
    "http://127.0.0.1:3000",
    "https://webgisbackend-zivl.onrender.com",
    "https://webgistabatabaei.netlify.app"
]





# Allow all origins for testing (remove in production)
CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

CORS_ALLOW_CREDENTIALS = True

# Append Slash
APPEND_SLASH = False





