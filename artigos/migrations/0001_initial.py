# Generated by Django 4.0.6 on 2024-03-19 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('conteudo', models.TextField()),
                ('autor', models.CharField(max_length=255)),
                ('data_publicacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]