# Generated by Django 3.2.5 on 2021-08-22 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('announcement', '0001_initial'),
        ('authusers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribeEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Your email')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactWithAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authusers.agents')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announcement.posts')),
            ],
            options={
                'verbose_name': 'Contac tWith Agent',
                'verbose_name_plural': 'Contacts',
                'ordering': ['-created_at'],
            },
        ),
    ]
