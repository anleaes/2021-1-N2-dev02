from django.db import models
from aircrafts.models import Aircraft

# Create your models here.
class Flight(models.Model):
    quantity = models.IntegerField('Quantidade de Tickets',null=True, blank=True)
    is_full = models.BooleanField('Voo cheio', default=False)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = 'Voo'
        verbose_name_plural = 'Voos'
        ordering =['id']

    def __str__(self):
        return self.name


class Aircraft(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Aeronave do voo'
        verbose_name_plural = 'Aeronaves do voo'
        ordering =['id']

    def __str__(self):
        return self.aircraft.name