# Generated by Django 4.2.7 on 2023-12-20 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0007_rename_posteo_comentarios_publicacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicarlibro',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagen_publicacion'),
        ),
    ]