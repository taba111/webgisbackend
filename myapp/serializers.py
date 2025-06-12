from rest_framework import serializers
from .models import  StudyArea,City,Hydrometry,River
from .models import  AbkZanjan

# Serializer for Employee model
""" class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'phone', 'email'] """

# Serializer for StudyArea model
# class StudyAreaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StudyArea
#         fields = ['name', 'geom',  'get_area', 'get_cost']

from rest_framework_gis.serializers import GeoFeatureModelSerializer

class StudyAreaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = StudyArea
        fields = '__all__'
        geo_field = 'geom'  # This field specifies the geometry field

   #////////////////////////////////////////////////////////////////////////////
class CitySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
        geo_field = 'geom'  # This field specifies the geometry field
   #////////////////////////////////////////////////////////////////////////////
class HydrometrySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Hydrometry
        fields = '__all__'
        geo_field = 'geom'  # This field specifies the geometry field
   #////////////////////////////////////////////////////////////////////////////
class RiverSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = River
        fields = '__all__'
        geo_field = 'geom'  # This field specifies the geometry field

   #////////////////////////////////////////////////////////////////////////////
class AbkZanjanSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = AbkZanjan
        fields = '__all__'  # نمایش همه فیلدها
        geo_field = 'geom'  # This field specifies the geometry field

   #////////////////////////////////////////////////////////////////////////////
    