# Generated by Django 5.0.3 on 2024-03-26 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_disciplinaporcurso_carga_horaria'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplinaporcurso',
            name='carga_horaria',
            field=models.CharField(default='', max_length=100, verbose_name='Carga horaria'),
        ),
    ]
