# Generated by Django 4.0.6 on 2024-06-11 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banda',
            name='idbanda',
            field=models.IntegerField(default=1),
        ),
    ]