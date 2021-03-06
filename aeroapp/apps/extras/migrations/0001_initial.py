# Generated by Django 3.2.4 on 2021-06-29 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('price', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Preco')),
            ],
            options={
                'verbose_name': 'Extra',
                'verbose_name_plural': 'Extras',
                'ordering': ['id'],
            },
        ),
    ]
