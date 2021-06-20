from django import forms
from .models import Vaccine

class VaccinesForm(forms.ModelForm):

    class Meta:
        model = Vaccine
        exclude = ('created_on' , 'updated_on',)