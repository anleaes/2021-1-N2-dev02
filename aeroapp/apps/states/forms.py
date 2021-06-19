from django import forms
from .models import State

class StateForm(forms.ModelForm):

    class Meta:
        model = State
        exclude = ('created_on' , 'updated_on',)
