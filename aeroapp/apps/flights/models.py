from django.db import models

# Create your models here.

class Flight(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField('Quantidade')
    is_full = models.BooleanField('Cheio', default=False)
    
    class Meta:
        verbose_name = 'Voo'
        verbose_name_plural = 'Voos'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.quantity)