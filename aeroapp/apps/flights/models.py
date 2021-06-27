from django.db import models
from aircrafts.models import Aircraft

# Create your models here.

class Flight(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    cod_flight = models.CharField('Codigo do Voo', max_length=50)
    quantity = models.IntegerField('Quantidade', null=True, blank=True, default=0)
    is_full = models.BooleanField('Voo cheio', default=False)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Voo'
        verbose_name_plural = 'Voos'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.cod_flight)
