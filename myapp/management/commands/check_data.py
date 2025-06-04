from django.core.management.base import BaseCommand
from myapp.models import City, Hydrometry, River, AbkZanjan, StudyArea

class Command(BaseCommand):
    help = 'Check database data status'

    def handle(self, *args, **options):
        # Check each model's data count
        models = [
            ('City', City),
            ('Hydrometry', Hydrometry),
            ('River', River),
            ('AbkZanjan', AbkZanjan),
            ('StudyArea', StudyArea),
        ]

        self.stdout.write(self.style.SUCCESS('Checking database data...'))
        
        for name, model in models:
            count = model.objects.count()
            self.stdout.write(f'{name}: {count} records')

        self.stdout.write(self.style.SUCCESS('Database check completed!')) 