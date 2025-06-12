from django.contrib.gis.db import models

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
""" 
class WorldBorder(models.Model):
    fips = models.CharField(max_length=2)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    un = models.IntegerField()
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.BigIntegerField()
    region = models.IntegerField()
    subregion = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    mpoly = models.MultiPolygonField(srid=3256)


# Auto-generated `LayerMapping` dictionary for WorldBorder model
worldborder_mapping = {
    'fips': 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'mpoly': 'MULTIPOLYGON',
} """
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////
# StudyArea Model for storing the uploaded boundary

class StudyArea(models.Model):
    perimeter = models.FloatField()
    area = models.FloatField()
    os_moteval = models.CharField(max_length=30)
    mah_code = models.FloatField()
    mah_name = models.CharField(max_length=38)
    hoze30code = models.IntegerField()
    hoze30name = models.CharField(max_length=37)
    hoze6code = models.IntegerField()
    hoze6name = models.CharField(max_length=32)
    geom = models.PolygonField(srid=4326)

    def __str__(self):
        return self.name

#    """  @property
#     def get_area(self):
#         """Calculate the area in hectares."""
#         return self.geom.area / 1000000  # Convert m² to km2
    
#     @property
#     def get_cost(self):
#         """Calculate the cost based on area in square kilometers."""
#         area_in_km2 = self.geom.area / 1_000_000  # Convert m² to km²
#         return area_in_km2 * 1000  # Price is 1000 per km²
    
#      """

# Auto-generated `LayerMapping` dictionary for StudyArea model
studyarea_mapping = {
    'perimeter': 'Perimeter',
    'area': 'Area',
    'os_moteval': 'os_moteval',
    'mah_code': 'Mah_code',
    'mah_name': 'Mah_Name',
    'hoze30code': 'Hoze30Code',
    'hoze30name': 'Hoze30Name',
    'hoze6code': 'Hoze6Code',
    'hoze6name': 'Hoze6Name',
    'geom': 'POLYGON',
}

#//////////////////////////////////////////////////////////////////////////////////////////////////////////
class City(models.Model):
    ostan_code = models.IntegerField()
    name = models.CharField(max_length=19)
    jameiyat = models.IntegerField()
    tamab_code = models.IntegerField()
    basin_code = models.IntegerField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.PolygonField(srid=4326)

city_mapping = {
    'ostan_code': 'OSTAN_CODE',
    'name': 'NAME',
    'jameiyat': 'JAMEIYAT',
    'tamab_code': 'TAMAB_CODE',
    'basin_code': 'BASIN_CODE',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'POLYGON',
}
#//////////////////////////////////////////////////////////////////////////////////////////////////////////    
class River(models.Model):
    drainiran = models.CharField(max_length=3, null=True, blank=True)
    geom = models.LineStringField(srid=4326)


# Auto-generated `LayerMapping` dictionary for River model
river_mapping = {
    'drainiran': 'DRAINIRAN',
    'geom': 'LINESTRING',
}
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Hydrometry(models.Model):
    province = models.CharField(max_length=27)
    code = models.CharField(max_length=16)
    station = models.CharField(max_length=36)
    river = models.CharField(max_length=31)
    tool = models.CharField(max_length=18)
    longtitude = models.FloatField()
    arz = models.CharField(max_length=18)
    latitude = models.FloatField()
    height = models.FloatField()
    data_from = models.FloatField()
    degree = models.FloatField()
    mahdode_co = models.FloatField()
    mahdode_na = models.CharField(max_length=34)
    hoze30_cod = models.FloatField()
    hoze30_nam = models.CharField(max_length=40)
    hoze6_code = models.FloatField()
    hoze6_name = models.CharField(max_length=32)
    areakm2 = models.FloatField()
    geom = models.PointField(srid=4326)


# Auto-generated `LayerMapping` dictionary for Hydrometry model
hydrometry_mapping = {
    'province': 'Province',
    'code': 'Code',
    'station': 'Station',
    'river': 'River',
    'tool': 'tool',
    'longtitude': 'Longtitude',
    'arz': 'Arz',
    'latitude': 'Latitude',
    'height': 'Height',
    'data_from': 'Data_From',
    'degree': 'Degree',
    'mahdode_co': 'Mahdode_Co',
    'mahdode_na': 'Mahdode_Na',
    'hoze30_cod': 'Hoze30_Cod',
    'hoze30_nam': 'Hoze30_Nam',
    'hoze6_code': 'Hoze6_Code',
    'hoze6_name': 'Hoze6_Name',
    'areakm2': 'Areakm2',
    'geom': 'POINT',
}
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////               ABKAN-ZANJAN                  ///////////////////////////////////////////////////////////////////////////////////////

class AbkZanjan(models.Model):
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.BigIntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    clamped = models.IntegerField()
    extruded = models.IntegerField()
    snippet = models.CharField(max_length=254,blank=True, null=True)
    popupinfo = models.CharField(max_length=254,blank=True, null=True)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.PolygonField(srid=4326)


# Auto-generated `LayerMapping` dictionary for AbkZanjan model
abkzanjan_mapping = {
    'name': 'Name',
    'folderpath': 'FolderPath',
    'symbolid': 'SymbolID',
    'altmode': 'AltMode',
    'base': 'Base',
    'clamped': 'Clamped',
    'extruded': 'Extruded',
    'snippet': 'Snippet',
    'popupinfo': 'PopupInfo',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'POLYGON25D',
}
