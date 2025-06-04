import os
import zipfile
import tempfile
import json 
from django.http import JsonResponse
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import GEOSGeometry
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.csrf import csrf_exempt  # Note: Remove this later
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from myapp.utils import convert_geojson_to_shapefile
from django.utils.decorators import method_decorator
from myapp.pagination import NoPagination
from rest_framework.views import APIView
from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view
from myapp.models import StudyArea, City, Hydrometry, River, AbkZanjan
from django.db import connection
from myapp.serializers import StudyAreaSerializer, CitySerializer, HydrometrySerializer, RiverSerializer, AbkZanjanSerializer


from myapp.models import AbkZanjan
from myapp.serializers import AbkZanjanSerializer




################################################################################################################

class NoPagination(PageNumberPagination):
    page_size = None  # Disables pagination by setting no limit
################################################################################################################
#################################################################################################################
################################################################################################################
                    #GetStudyArea
@method_decorator(csrf_exempt, name='dispatch')

class GetStudyArea(viewsets.ModelViewSet):
    queryset = StudyArea.objects.all()
    serializer_class = StudyAreaSerializer
    pagination_class = NoPagination  # Disable pagination
    http_method_names = ['get', 'post']

    def list(self, request, *args, **kwargs):
        # نام لایه را از مدل به طور داینامیک به دست می‌آوریم
        layer_name = self.get_layer_name()

        # سپس نام لایه را به داده‌های پاسخ اضافه می‌کنیم
        response = super().list(request, *args, **kwargs)
        response.data["layer_name"] = layer_name  # اضافه کردن نام لایه به داده‌های پاسخ
        return Response(response.data)

    def get_layer_name(self):
        # دریافت نام مدل به صورت حروف کوچک و بدون فاصله
        return self.queryset.model._meta.model_name

#////////////////////////////////////////////////////////////////////////////////
                    #GetHydrometry
class GetHydrometry(viewsets.ModelViewSet):
    queryset = Hydrometry.objects.all()
    serializer_class = HydrometrySerializer
    pagination_class = NoPagination  # Disable pagination
    http_method_names = ['get', 'post']

    def list(self, request, *args, **kwargs):
        # نام لایه را از مدل به طور داینامیک به دست می‌آوریم
        layer_name = self.get_layer_name()

        # سپس نام لایه را به داده‌های پاسخ اضافه می‌کنیم
        response = super().list(request, *args, **kwargs)
        response.data["layer_name"] = layer_name  # اضافه کردن نام لایه به داده‌های پاسخ
        return Response(response.data)

    def get_layer_name(self):
        # دریافت نام مدل به صورت حروف کوچک و بدون فاصله
        return self.queryset.model._meta.model_name

#////////////////////////////////////////////////////////////////////////////////
                    #GetCity
class GetCity(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    pagination_class = NoPagination  # Disable pagination
    http_method_names = ['get', 'post']

    def list(self, request, *args, **kwargs):
        # نام لایه را از مدل به طور داینامیک به دست می‌آوریم
        layer_name = self.get_layer_name()

        # سپس نام لایه را به داده‌های پاسخ اضافه می‌کنیم
        response = super().list(request, *args, **kwargs)
        response.data["layer_name"] = layer_name  # اضافه کردن نام لایه به داده‌های پاسخ
        return Response(response.data)

    def get_layer_name(self):
        # دریافت نام مدل به صورت حروف کوچک و بدون فاصله
        return self.queryset.model._meta.model_name

#////////////////////////////////////////////////////////////////////////////////
                    #GetRiver
class GetRiver(viewsets.ModelViewSet):
    queryset = River.objects.all()
    serializer_class = RiverSerializer
    pagination_class = NoPagination  # Disable pagination
    http_method_names = ['get', 'post']

    def list(self, request, *args, **kwargs):
        # نام لایه را از مدل به طور داینامیک به دست می‌آوریم
        layer_name = self.get_layer_name()

        # سپس نام لایه را به داده‌های پاسخ اضافه می‌کنیم
        response = super().list(request, *args, **kwargs)
        response.data["layer_name"] = layer_name  # اضافه کردن نام لایه به داده‌های پاسخ
        return Response(response.data)

    def get_layer_name(self):
        # دریافت نام مدل به صورت حروف کوچک و بدون فاصله
        return self.queryset.model._meta.model_name

#///////////////////////////////////////////////////////////////////////
# AbkZanjan
class GetAbkZanjan(viewsets.ModelViewSet):
    queryset = AbkZanjan.objects.all()
    serializer_class = AbkZanjanSerializer
    pagination_class = NoPagination  # Disable pagination
    http_method_names = ['get', 'post']

    def list(self, request, *args, **kwargs):
        # نام لایه را از مدل به طور داینامیک به دست می‌آوریم
        layer_name = self.get_layer_name()

        # سپس نام لایه را به داده‌های پاسخ اضافه می‌کنیم
        response = super().list(request, *args, **kwargs)
        response.data["layer_name"] = layer_name  # اضافه کردن نام لایه به داده‌های پاسخ
        return Response(response.data)

    def get_layer_name(self):
        # دریافت نام مدل به صورت حروف کوچک و بدون فاصله
        return self.queryset.model._meta.model_name





################################################################################################################
################################################################################################################
################################################################################################################
################################################################################################################
################################################################################################################
################################################################################################################
                                #    ConvertToShapefile    ////////////////////  


import traceback  # اضافه در ابتدای فایل

class ConvertToShapefile(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            geojson = data.get('geojson')
            filename = data.get('filename', 'output')

            if not geojson:
                raise ValidationError("GeoJSON data is required")

            # این خط لازم نیست چون geojson دیکشنری است
            # geojson_obj = json.loads(geojson)

            return convert_geojson_to_shapefile(geojson, filename)

        except ValidationError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            import traceback
            print("Exception occurred:", e)
            traceback.print_exc()
            return JsonResponse({"error": str(e)}, status=500)


################################################################################################################

@api_view(['GET'])
def welcome(request):
    return Response({
        "message": "Welcome to WebGIS Backend API",
        "available_endpoints": {
            "cities": "/api/city/",
            "hydrometry": "/api/hydrometry/",
            "abkzanjan": "/api/abkzanjan/",
            "study_area": "/api/study-area/",
            "convert_shapefile": "/api/convert-to-shapefile/",
            "database_status": "/api/db-status/",
            "database_check": "/api/check-database/"
        }
    })

@api_view(['GET'])
def check_database(request):
    """
    بررسی وضعیت دیتابیس و تعداد رکوردها در هر مدل
    """
    try:
        data = {
            'status': 'online',
            'records': {
                'City': City.objects.count(),
                'Hydrometry': Hydrometry.objects.count(),
                'River': River.objects.count(),
                'AbkZanjan': AbkZanjan.objects.count(),
                'StudyArea': StudyArea.objects.count(),
            },
            'database_info': {
                'engine': connection.vendor,
                'name': connection.settings_dict['NAME'],
                'host': connection.settings_dict['HOST'],
            }
        }
        return Response(data)
    except Exception as e:
        return Response({
            'status': 'error',
            'message': str(e)
        }, status=500)

class DatabaseStatusViewSet(viewsets.ViewSet):
    """
    ViewSet برای بررسی وضعیت دیتابیس
    """
    def list(self, request):
        try:
            data = {
                'status': 'online',
                'records': {
                    'City': City.objects.count(),
                    'Hydrometry': Hydrometry.objects.count(),
                    'River': River.objects.count(),
                    'AbkZanjan': AbkZanjan.objects.count(),
                    'StudyArea': StudyArea.objects.count(),
                },
                'database_info': {
                    'engine': connection.vendor,
                    'name': connection.settings_dict['NAME'],
                    'host': connection.settings_dict['HOST'],
                }
            }
            return Response(data)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=500)
