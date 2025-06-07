import os
import django
from django.conf import settings

# تنظیم محیط Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webgis.settings')
django.setup()

# وارد کردن مدل‌ها
from myapp.models import StudyArea

# بررسی تعداد رکوردها
count = StudyArea.objects.count()
print(f"تعداد رکوردهای StudyArea: {count}")

# نمایش اطلاعات رکوردها
if count > 0:
    print("\nاطلاعات رکوردها:")
    for area in StudyArea.objects.all():
        print(f"نام: {area.name}") 