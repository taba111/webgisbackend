"""
URL configuration for webgis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def health_check(request):
    return JsonResponse({
        "status": "healthy",
        "debug": True,
        "api_root": "/api/",
        "admin_root": "/admin/",
        "message": "اگر این پیام را می‌بینید، سرور در حال کار است"
    })

@csrf_exempt
def root_redirect(request):
    return JsonResponse({
        "message": "به API وب‌جی‌آی‌اس خوش آمدید",
        "endpoints": {
            "api": "/api/",
            "admin": "/admin/",
            "health": "/health/"
        }
    })

urlpatterns = [
    path('', root_redirect, name='root'),
    path('health/', health_check, name='health_check'),
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
]
