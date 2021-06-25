# Generated by Django 3.2.3 on 2021-06-25 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('socialnetworks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=100, verbose_name='Sobrenome')),
                ('address', models.CharField(max_length=200, verbose_name='Endereco')),
                ('cell_phone', models.CharField(max_length=20, verbose_name='Telefone celular')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1, verbose_name='Genero')),
                ('passport', models.CharField(max_length=8, verbose_name='Passaporte')),
                ('photo', models.ImageField(upload_to='photos', verbose_name='Foto')),
                ('doc', models.FileField(upload_to='docs', verbose_name='Documentos')),
                ('special_needs', models.BooleanField(default=False, verbose_name='Atendimento especial?')),
                ('cargo_allowance', models.IntegerField(blank=True, default=0, null=True, verbose_name='Bagagem permitida (KG)')),
                ('socialnetwork', models.ManyToManyField(to='socialnetworks.Socialnetwork')),
            ],
            options={
                'verbose_name': 'Passageiro',
                'verbose_name_plural': 'Passageiros',
                'ordering': ['id'],
            },
        ),
    ]
