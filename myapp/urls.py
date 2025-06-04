from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import ConvertToShapefile, GetStudyArea, GetHydrometry, GetCity, GetRiver
from myapp.views import GetAbkZanjan, welcome
# ایجاد روتری برای ViewSet ها
router = DefaultRouter()
router.register(r'study-area', GetStudyArea, basename='studyarea')
router.register(r'hydrometry', GetHydrometry, basename='hydrometry')
router.register(r'city', GetCity, basename='city')
router.register(r'abkzanjan', GetAbkZanjan, basename='abkzanjan')


# myapp/urls.py
urlpatterns = [
    path('', welcome, name='api-root'),
    path('convert-to-shapefile/', ConvertToShapefile.as_view(), name='convert_shapefile'),
    path('', include(router.urls)),  # اضافه کردن URL های ViewSet ها از طریق روتر
]

""" 
توضیحات:

    DefaultRouter: وقتی از DefaultRouter استفاده می‌کنید، این روتر به طور خودکار مسیرهای مربوط به ViewSet هایی که ثبت کرده‌اید را ایجاد می‌کند. برای مثال:

        router.register(r'study-area', GetStudyArea, basename='studyarea')

    این خط به طور خودکار یک مسیر به نام study-area/ ایجاد می‌کند که از GetStudyArea استفاده می‌کند.

    خودکار ایجاد مسیرها: وقتی که DefaultRouter را استفاده می‌کنید، نیازی نیست که خودتان مسیرها را به صورت دستی برای هر ViewSet وارد کنید. DefaultRouter به طور خودکار مسیرهای RESTful را برای متدهای مختلف (مثل list, create, retrieve, update, destroy) ایجاد می‌کند.

    مزایای استفاده از DefaultRouter:

        کاهش تکرار: وقتی از روتر استفاده می‌کنید، نیاز نیست هر مسیر را به صورت دستی تعریف کنید.

        مدیریت آسان: در آینده اگر بخواهید ViewSet جدیدی اضافه کنید، فقط کافیست آن را به روتر اضافه کنید و نیاز به افزودن مسیرهای دستی ندارید.

نتیجه:

برای شما که از DefaultRouter استفاده می‌کنید، دیگر نیازی به مسیرهای دستی برای GetStudyArea, GetHydrometry, GetCity, و GetRiver نیست. روتر این کار را به طور خودکار انجام می‌دهد.

اگر شما همچنان بخواهید مسیرهای دستی را داشته باشید (مثلاً به دلیل نیاز به تنظیمات خاص)، می‌توانید آن‌ها را نگه دارید، اما معمولاً استفاده از DefaultRouter باعث کاهش پیچیدگی و مدیریت بهتر مسیرها می‌شود.

 """