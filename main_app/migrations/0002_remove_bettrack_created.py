# Generated by Django 3.2.2 on 2021-05-10 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bettrack',
            name='created',
        ),
    ]
