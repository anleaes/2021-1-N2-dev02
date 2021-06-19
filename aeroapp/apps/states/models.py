from django.db import models
from countries.models import Country

# Create your models here.
class State(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering =['id']

    def __str__(self):
        return self.name
