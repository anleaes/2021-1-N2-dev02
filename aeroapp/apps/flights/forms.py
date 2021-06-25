from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):

    class Meta:
        model = Flight
        exclude = ('created_on' , 'updated_on',)
    