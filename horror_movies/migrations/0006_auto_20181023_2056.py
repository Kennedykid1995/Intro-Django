# Generated by Django 2.1.2 on 2018-10-23 20:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('horror_movies', '0005_movies_rottentomatoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]