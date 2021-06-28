from django import forms
from .models import Ticket, Extra

class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        exclude = ('created_on' , 'updated_on')


class ExtraItemForm(forms.ModelForm):
    
    class Meta:
        model = Extra
        exclude = ('created_on' , 'updated_on',)