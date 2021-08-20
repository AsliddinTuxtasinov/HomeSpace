# Generated by Django 3.2.5 on 2021-08-20 12:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='baths',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='batheroom'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='beds',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='badroom'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='garages',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='garages'),
        ),
    ]
