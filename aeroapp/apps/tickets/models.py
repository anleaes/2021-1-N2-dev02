from django.db import models
from flights.models import Flight
from passengers.models import Passenger
from django.contrib.auth.models import User

# Create your models here.
class Ticket(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    total_price = models.FloatField('Preco Total', null=True, blank=True, default=0.0)
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Em andamento')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    ticket_passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        ordering =['-created_on']

    def __str__(self):
        return "%s" % (self.total_price) 


class TicketPassenger(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    seat = models.CharField('Assento',max_length=4,null=True, blank=True,default=0)
    unitary_price = models.FloatField('Preco unitario',null=True, blank=True, default=0.0)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Passageiro do ticket'
        verbose_name_plural = 'Passageiros do ticket'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.passenger) 

