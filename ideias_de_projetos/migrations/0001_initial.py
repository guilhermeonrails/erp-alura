# Generated by Django 4.1.2 on 2022-10-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ideia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ideia_em_poucas_palavras', models.CharField(max_length=20)),
                ('detalhes', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Tem uma ideia? Que tal anotar!',
            },
        ),
    ]
