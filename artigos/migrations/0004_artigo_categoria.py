# Generated by Django 4.1.2 on 2022-10-12 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0003_artigo_id_do_artigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='categoria',
            field=models.CharField(choices=[('0', '---'), ('1', 'ANGULAR'), ('2', 'AUTOMAÇÃO E PERFORMANCE'), ('3', 'FRAMEWORK MVC'), ('4', 'HTML E CSS'), ('5', 'JAVASCRIPT'), ('6', 'JQUERY'), ('7', 'REACT'), ('8', 'WORDPRESS')], default='0', max_length=1),
        ),
    ]
