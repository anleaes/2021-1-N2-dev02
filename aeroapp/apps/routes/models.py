from django.db import models
from cities.models import City

# Create your models here.


#  class City(models.Model):
#     city_from = models.ForeignKey(City, on_delete=models.CASCADE)
#     city_to = models.ForeignKey(City, on_delete=models.CASCADE)


class Route(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Rota'
        verbose_name_plural = 'Rotas'
        ordering =['id']

    def __str__(self):
        return self.name