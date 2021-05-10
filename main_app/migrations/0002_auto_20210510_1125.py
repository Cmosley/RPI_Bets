# Generated by Django 3.2.2 on 2021-05-10 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bet',
            name='type',
        ),
        migrations.AddField(
            model_name='bet',
            name='bet_type',
            field=models.CharField(choices=[('A', 'A Bet'), ('B', 'B Bet'), ('C', 'C Bet'), ('D', 'D Bet')], default='A', max_length=50),
        ),
        migrations.AlterField(
            model_name='bet',
            name='end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='bet',
            name='start',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]