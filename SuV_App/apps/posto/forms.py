from django import forms
from .models import Posto

class PostoForm(forms.ModelForm):

    class Meta:
        model = Posto
        exclude = ()