# Generated by Django 4.1.2 on 2022-10-13 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0004_alter_curso_id_do_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='pasta_do_curso',
            field=models.URLField(blank=True, null=True),
        ),
    ]
