# Generated by Django 4.2.7 on 2023-12-17 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0005_alter_comentarios_posteo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='posteo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comentario', to='publicaciones.publicarlibro'),
            preserve_default=False,
        ),
    ]