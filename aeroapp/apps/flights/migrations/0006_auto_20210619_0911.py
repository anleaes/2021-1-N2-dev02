# Generated by Django 3.2.4 on 2021-06-19 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_aircraft'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='created_on',
            field=models.DateTimeField(default='2021-06-13 17:17:10'),
        ),
        migrations.AddField(
            model_name='flight',
            name='updated_on',
            field=models.DateTimeField(default='2021-06-13 17:17:10'),
        ),
        migrations.DeleteModel(
            name='Aircraft',
        ),
    ]