# Generated by Django 2.2.17 on 2024-03-11 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typerush', '0005_auto_20240311_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]