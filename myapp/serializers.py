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
        fields = ['name']  # Add any other fields you need
        geo_field = 'geom'  # This field specifies the geometry field

   #////////////////////////////////////////////////////////////////////////////
class CitySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = City
        fields = ['ostan_code','name','jameiyat','tamab_code','basin_code','shape_leng']  # Add any other fields you need
        geo_field = 'geom'  # This field specifies the geometry field
   #////////////////////////////////////////////////////////////////////////////
class HydrometrySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Hydrometry
        fields = ['rank','rank_of_pr','province','code','station','river','tool','longtitude','arz','latitude',
                  'height','data_from','degree','mahdode_co','mahdode_na','hoze30_cod','hoze30_nam','hoze6_code',
                   'hoze6_name','mahdodeh_t','hozeh30_t','hozeh6_t' ]  # Add any other fields you need
        geo_field = 'geom'  # This field specifies the geometry field
   #////////////////////////////////////////////////////////////////////////////
class RiverSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = River
        fields = ['name']  # Add any other fields you need
        geo_field = 'geom'  # This field specifies the geometry field

   #////////////////////////////////////////////////////////////////////////////
class AbkZanjanSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = AbkZanjan
        fields = '__all__'  # نمایش همه فیلدها
        geo_field = 'geom'  # This field specifies the geometry field

   #////////////////////////////////////////////////////////////////////////////
    