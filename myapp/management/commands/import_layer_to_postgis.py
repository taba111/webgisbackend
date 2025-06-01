from django.core.management.base import BaseCommand
from django.contrib.gis.utils import LayerMapping
from myapp.models import StudyArea, studyarea_mapping  # Adjust to your app name
from myapp.models import AbkZanjan, abkzanjan_mapping  # Adjust to your app name


""" class Command(BaseCommand):
    help = 'Import studyarea from shapefile'

    def handle(self, *args, **kwargs):
        shapefile_path = 'G:/webgis_edareh_map/ut/addition/gis_data/studyarea.shp'  # Path to your shapefile

        lm = LayerMapping(
            StudyArea,
            shapefile_path,
            studyarea_mapping,
            transform=False  # Set to True if you want to transform coordinates
        )

        lm.save(strict=True, verbose=True)
        self.stdout.write(self.style.SUCCESS('Data imported successfully.')) """
#////////////////


class Command(BaseCommand):
    help = 'Import AbkZanjan from shapefile'

    def handle(self, *args, **kwargs):
        shapefile_path = 'D:/test/data/abk_zanjan.shp'  # Path to your shapefile

        lm = LayerMapping(
            AbkZanjan,
            shapefile_path,
            abkzanjan_mapping,
            transform=False  # Set to True if you want to transform coordinates
        )

        lm.save(strict=True, verbose=True)
        self.stdout.write(self.style.SUCCESS('Data imported successfully.'))

        
