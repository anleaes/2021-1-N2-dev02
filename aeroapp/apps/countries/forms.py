from django import forms
from .models import Country

class CountryForm(forms.ModelForm):

    class Meta:
        model = Country
        exclude = ('created_on' , 'updated_on',)
