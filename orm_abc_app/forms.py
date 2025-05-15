from django.forms import ModelForm
from .models import Admission

class AdmissionForm(ModelForm):
    class Meta:
        model  = Admission
        fields = ['full_name', 'admission_year', 'program_name']
