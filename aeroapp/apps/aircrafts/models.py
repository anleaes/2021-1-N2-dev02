from django.db import models

# Create your models here.
class Aircraft(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100) 
    date_fabrication = models.DateField('Data de fabricacao', auto_now=False, auto_now_add=False)
    quantity_pax = models.IntegerField('Quantidade de passageiros',null=True, blank=True)
    is_active = models.BooleanField('Ativo', default=False)
    
    class Meta:
        verbose_name = 'Aeronave'
        verbose_name_plural = 'Aeronaves'
        ordering =['id']

    def __str__(self):
        return self.name