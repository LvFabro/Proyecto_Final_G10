# Generated by Django 4.2.7 on 2023-12-08 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PublicarLibro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('titulo', models.CharField(max_length=40)),
                ('cuerpo', models.TextField()),
                ('categoria', models.CharField(max_length=30)),
                ('autor', models.CharField(max_length=30)),
            ],
        ),
    ]