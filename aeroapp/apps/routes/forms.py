from django import forms
from .models import Route

class RouteForm(forms.ModelForm):

    class Meta:
        model = Route
        exclude = ('created_on' , 'updated_on',)
