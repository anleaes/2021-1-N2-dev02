# Generated by Django 3.2.3 on 2021-06-27 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_flight_aircraft'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='cod_flight',
            field=models.CharField(default=1, max_length=50, verbose_name='Codigo do Voo'),
            preserve_default=False,
        ),
    ]
