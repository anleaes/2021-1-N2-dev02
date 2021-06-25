from django.db import models

# Create your models here.

class Country(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Pais', max_length=50)
    country_code = models.IntegerField('Código do país',null=True, blank=True,default=0)
    
    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        ordering =['id']

    def __str__(self):
        return self.name
