from django.db import models
#from .models import Aircraft

# Create your models here.
class Flight(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100) 
    
    #aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Voo'
        verbose_name_plural = 'Voos'
        ordering =['id']

    def __str__(self):
        return self.name
