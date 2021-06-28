from django import forms
from .models import Extra

class ExtraForm(forms.ModelForm):

    class Meta:
        model = Extra
        exclude = ('created_on' , 'updated_on',)
