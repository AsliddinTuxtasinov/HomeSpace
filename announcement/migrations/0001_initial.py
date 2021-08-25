# Generated by Django 3.2.5 on 2021-08-25 11:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'District',
                'verbose_name_plural': 'Districts',
            },
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='your comment:')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('home_type', models.CharField(choices=[('resturant', 'resturant'), ('market', 'market'), ('float', 'float'), ('yard', 'yard')], default='float', max_length=20)),
                ('type', models.CharField(choices=[('buy', 'Buy'), ('rent', 'Rent')], default='buy', max_length=20)),
                ('price', models.FloatField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='price ($)')),
                ('year_build', models.PositiveIntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('more_info', models.TextField(default='more info ...', verbose_name='more info')),
                ('area', models.FloatField(default=1, verbose_name='area (m.kv)')),
                ('picture', models.ImageField(upload_to='announcement/%Y/%m/%d/announcement')),
                ('picture2', models.ImageField(upload_to='announcement/%Y/%m/%d/announcement')),
                ('picture3', models.ImageField(upload_to='announcement/%Y/%m/%d/announcement')),
                ('beds', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='badroom')),
                ('baths', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='batheroom')),
                ('garages', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='garages')),
                ('tel_num', models.CharField(default='+998', max_length=40, verbose_name='telefon number:')),
                ('adress', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=255)),
                ('is_publish', models.BooleanField(default=False)),
                ('is_send_mail', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
            },
        ),
    ]