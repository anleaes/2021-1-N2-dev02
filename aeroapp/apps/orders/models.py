from django.db import models
from products.models import Product
from clients.models import Client

# Create your models here.
class Order(models.Model):
    quantity = models.IntegerField('Quantidade',null=True, blank=True)
    price = models.FloatField('Preco',null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering =['id']

    def __str__(self):
        return self.product.name