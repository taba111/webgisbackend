import os
from pathlib import Path
import dj_database_url

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# GDAL and PROJ Setup for Windows
if os.name == 'nt':
    try:
        VENV_BASE = os.environ['VIRTUAL_ENV']
        os.environ['PATH'] = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo\\') + ';' + os.environ['PATH']
        os.environ['PROJ_LIB'] = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo\\data\\proj\\') + ';' + os.environ['PATH']
    except KeyError:
        raise Exception("Virtual environment is not activated or 'VIRTUAL_ENV' is not set.")

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

DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

# ALLOWED_HOSTS configuration
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
ALLOWED_HOSTS = [
    'webgis-backend-taba.onrender.com',
    'localhost',
    '127.0.0.1',
    '*',  # This is for development only, remove in production
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
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
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
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://webgis_db_user:o1UikokIgyghbfN2LcCeXb91d0c76FiO@dpg-d0uroi6mcj7s73ab5d60-a.frankfurt-postgres.render.com/webgis_db')

DATABASES = {
    'default': dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=600,
        engine='django.contrib.gis.db.backends.postgis'
    )
}

if os.environ.get('DEVELOPMENT'):
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

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static and Media Files
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Simplified static file serving
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default Primary Key Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS Settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://webgis-taba.netlify.app",
]

# Allow all origins for testing (remove in production)
CORS_ALLOW_ALL_ORIGINS = True

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
APPEND_SLASH = True





