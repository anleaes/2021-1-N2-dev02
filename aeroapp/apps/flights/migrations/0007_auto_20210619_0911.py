# Generated by Django 3.2.4 on 2021-06-19 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0006_auto_20210619_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
