# Generated by Django 3.2.2 on 2021-05-10 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_bets', models.IntegerField(default=0)),
                ('total_wins', models.IntegerField(default=0)),
                ('bank_roll', models.IntegerField(default=0)),
                ('winnings', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BetTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.CharField(choices=[('MLB', 'Baseball'), ('NHL', 'Hockey')], default='MLB', max_length=3)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('total_bet', models.IntegerField(default=0)),
                ('total_net', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bet_type', models.CharField(choices=[('A', 'A Bet'), ('B', 'B Bet'), ('C', 'C Bet'), ('D', 'D Bet')], default='A', max_length=50)),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateField()),
                ('sport', models.CharField(choices=[('MLB', 'Baseball'), ('NHL', 'Hockey')], default='MLB', max_length=3)),
                ('home_team', models.CharField(max_length=50)),
                ('away_team', models.CharField(max_length=50)),
                ('betting_line', models.IntegerField(default=0)),
                ('bet_amount', models.IntegerField(default=0)),
                ('won', models.CharField(choices=[('Pending', 'Pending'), ('Win', 'Win'), ('Loss', 'Loss')], default='Pending', max_length=50)),
                ('bet_track', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main_app.bettrack')),
            ],
        ),
    ]
