# Generated by Django 4.2.7 on 2023-12-15 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0004_comentarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='posteo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentario', to='publicaciones.publicarlibro'),
        ),
    ]
