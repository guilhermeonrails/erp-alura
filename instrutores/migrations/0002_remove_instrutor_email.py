# Generated by Django 4.1.2 on 2022-10-11 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrutores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrutor',
            name='email',
        ),
    ]
