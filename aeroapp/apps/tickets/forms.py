from django import forms
from .models import Ticket, Flight, TicketPassenger

class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        exclude = ('user', 'flight', 'created_on' , 'updated_on',)

class TicketPassengerForm(forms.ModelForm):
    
    class Meta:
        model = TicketPassenger
        exclude = ('user','ticket', 'created_on' , 'updated_on',)
