from django.db import models
# from cities.models import City

# Create your models here.

class Route(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # city_from = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_from')
    # city_to = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_to')

    class Meta:
        verbose_name = 'Rota'
        verbose_name_plural = 'Rotas'
        ordering =['id']

    def __str__(self):
        return self.name