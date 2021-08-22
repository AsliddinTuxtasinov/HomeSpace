# Generated by Django 3.2.5 on 2021-08-22 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('announcement', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authusers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='diller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authusers.agents'),
        ),
        migrations.AddField(
            model_name='posts',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announcement.districts'),
        ),
        migrations.AddField(
            model_name='posts',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='posts',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announcement.regions'),
        ),
        migrations.AddField(
            model_name='postcomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postcomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='announcement.postcomment'),
        ),
        migrations.AddField(
            model_name='postcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announcement.posts'),
        ),
        migrations.AddField(
            model_name='districts',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announcement.regions'),
        ),
    ]
