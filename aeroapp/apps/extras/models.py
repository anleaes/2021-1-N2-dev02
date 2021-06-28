from django.db import models

# Create your models here.
class Extra(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    price = models.FloatField('Preco',null=True, blank=True, default=0.0)
    
    class Meta:
        verbose_name = 'Extra'
        verbose_name_plural = 'Extras'
        ordering =['id']

    def __str__(self):
        return self.name
