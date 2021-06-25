# Generated by Django 3.2.3 on 2021-06-25 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aircrafts', '0001_initial'),
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='aircraft',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='aircrafts.aircraft'),
            preserve_default=False,
        ),
    ]
