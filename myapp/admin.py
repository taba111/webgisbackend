# Register your models here.
from django.contrib import admin
from .models import StudyArea


@admin.register(StudyArea)
class StudyAreaAdmin(admin.ModelAdmin):
    list_display = ('mah_name', 'hoze30name')

