from django import forms
from .models import Passenger

class PassengerForm(forms.ModelForm):

    class Meta:
        model = Passenger
        exclude = ('created_on' , 'updated_on',)

