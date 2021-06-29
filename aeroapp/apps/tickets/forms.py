from django import forms
from .models import Ticket, TicketExtra

class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        exclude = ('created_on' , 'updated_on',)

class TicketExtraForm(forms.ModelForm):
    
    class Meta:
        model = TicketExtra
        exclude = ('ticket',)