from django.contrib import admin
from .models import Admission

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display  = ('full_name', 'admission_year', 'program_name', 'date_submitted')
    list_filter   = ('admission_year', 'program_name')
    search_fields = ('full_name',)
