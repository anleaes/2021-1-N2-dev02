from django.db import models
from passengers.models import Passenger
from flights.models import Flight
from extras.models import Extra
from django.contrib.auth.models import User

# Create your models here.

class Ticket(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Em andamento')
    total_price = models.FloatField('Preco Total', null=True, blank=True, default=0.0)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=True)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    ticket_extra = models.ManyToManyField(Extra, through='TicketExtra', blank=True)
    
    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        ordering =['-created_on']

    def __str__(self):
        return "%s" % (self.total_price) 



class TicketExtra(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True)
    extra = models.ForeignKey(Extra, on_delete=models.CASCADE, null=True)
        
    class Meta:
        verbose_name = 'Extra'
        verbose_name_plural = 'Extras'
        ordering =['id']
