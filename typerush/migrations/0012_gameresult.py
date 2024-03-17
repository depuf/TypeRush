# Generated by Django 2.2.28 on 2024-03-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typerush', '0011_auto_20240311_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct', models.IntegerField(default=0)),
                ('wrong', models.IntegerField(default=0)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]