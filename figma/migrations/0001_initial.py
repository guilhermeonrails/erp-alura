# Generated by Django 4.1.2 on 2022-10-10 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Figma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField(max_length=450)),
                ('link_figma', models.URLField()),
                ('mobile', models.CharField(choices=[('SIM', 'SIM'), ('NAO', 'NAO')], default='NAO', max_length=3)),
            ],
        ),
    ]
