from django import forms
from .models import City

class CityForm(forms.ModelForm):

    class Meta:
        model = City
        exclude = ('created_on' , 'updated_on',)
