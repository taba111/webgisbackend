import os
import tempfile
import zipfile
import json
from django.http import FileResponse, JsonResponse
from osgeo import ogr

def convert_geojson_to_shapefile(geojson_data, filename='output'):
    try:
        # ایجاد یک پوشه موقت
        temp_dir = tempfile.mkdtemp()
        shp_path = os.path.join(temp_dir, f'{filename}.shp')

        # انتخاب درایور shapefile
        driver = ogr.GetDriverByName("ESRI Shapefile")

        geojson_obj = geojson_data  # ورودی JSON به صورت دیکشنری پایتون است

        # تعیین نوع هندسه
        geometry_type = geojson_obj['features'][0]['geometry']['type'].upper()
        geom_type_map = {
            'POINT': ogr.wkbPoint,
            'LINESTRING': ogr.wkbLineString,
            'POLYGON': ogr.wkbPolygon
        }
        ogr_geom_type = geom_type_map.get(geometry_type, ogr.wkbUnknown)

        # ساخت لایه با تعیین ENCODING=UTF-8 برای پشتیبانی از حروف فارسی
        data_source = driver.CreateDataSource(shp_path)
        layer = data_source.CreateLayer(
            filename,
            geom_type=ogr_geom_type,
            options=['ENCODING=UTF-8']  # 👈 مهم‌ترین خط برای پشتیبانی از فارسی
        )

        # تعریف فیلدها
        properties = geojson_obj['features'][0]['properties']
        for key in properties.keys():
            field = ogr.FieldDefn(key, ogr.OFTString)
            layer.CreateField(field)

        # افزودن فیچرها
        for feature in geojson_obj['features']:
            ogr_feature = ogr.Feature(layer.GetLayerDefn())

            for key, value in feature['properties'].items():
                ogr_feature.SetField(key, str(value))  # تبدیل همه مقادیر به رشته

            geom = ogr.CreateGeometryFromJson(json.dumps(feature['geometry']))
            ogr_feature.SetGeometry(geom)
            layer.CreateFeature(ogr_feature)
            ogr_feature = None

        data_source = None  # ذخیره و بستن فایل shapefile

        # ساخت فایل فشرده (zip)
        zip_path = os.path.join(temp_dir, f'{filename}.zip')
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for ext in ['shp', 'shx', 'dbf', 'prj', 'cpg']:
                filepath = os.path.join(temp_dir, f'{filename}.{ext}')
                if os.path.exists(filepath):
                    zipf.write(filepath, arcname=f'{filename}.{ext}')

        return FileResponse(open(zip_path, 'rb'), as_attachment=True, filename=f'{filename}.zip')

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
