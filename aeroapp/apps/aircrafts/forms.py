from django import forms
from .models import Aircraft

class AircraftForm(forms.ModelForm):

    class Meta:
        model = Aircraft
        exclude = ('created_on' , 'updated_on',)