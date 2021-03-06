from django.db import models

# Create your models here.

class Passenger(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100) 
    address = models.CharField('Endereco', max_length=200)   
    cell_phone = models.CharField('Telefone celular', max_length=20)
    email = models.EmailField('E-mail',null=False, blank=False)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)
    passport = models.CharField('Passaporte', max_length=8)
    photo = models.ImageField('Foto', upload_to='photos')
    doc = models.FileField('Documentos', upload_to='docs')
    special_needs = models.BooleanField('Atendimento especial?', default=False)
    cargo_allowance = models.IntegerField('Bagagem permitida (KG)',null=True, blank=True,default=0)
    
    class Meta:
        verbose_name = 'Passageiro'
        verbose_name_plural = 'Passageiros'
        ordering =['id']

    def __str__(self):
        return "%s %s" % (self.first_name,self.last_name)
