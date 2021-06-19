from django.db import models
from states.models import State

# Create your models here.
class City(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=85)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        ordering =['id']

    def __str__(self):
        return self.name