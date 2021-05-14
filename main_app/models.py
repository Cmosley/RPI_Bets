from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

from decimal import Decimal
# Create your models here.

SPORTS = (
  ('MLB', 'Baseball'),
  )

class Profile(models.Model): 
  total_bets = models.IntegerField(default=0)
  total_wins = models.IntegerField(default=0)
  bank_roll = models.IntegerField(default=0)
  # winnings = models.DecimalField(default=Decimal(0), max_digits=10, decimal_places=2)
  winnings = models.IntegerField(default=0)
  user = models.OneToOneField(User, on_delete=models.CASCADE)

class BetTrack(models.Model):
  sport = models.CharField(
    max_length=3, 
    choices=SPORTS, 
    default=SPORTS[0][0]
  )
  active = models.BooleanField(default=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  # created = models.DateTimeField('created', auto_now=False, auto_now_add=True)
  # total_bet = models.DecimalField(default=Decimal(0), max_digits=10, decimal_places=2)
  total_bet = models.IntegerField(default=0)
  # total_net = models.DecimalField(default=Decimal(0), max_digits=10, decimal_places=2)
  total_net = models.IntegerField(default=0)
  
  
 

  def get_absolute_url(self):
      return reverse("bettrack_create")
 

class Bet(models.Model):
  
  BET_TYPES = (
    ('A', 'A Bet'),
    ('B', 'B Bet'),
    ('C', 'C Bet'),
    ('D', 'D Bet'),
  )
  BET_RESULT = (
    ('Pending', 'Pending'),
    ('Win', 'Win'),
    ('Loss', 'Loss'),
  )
  bet_type = models.CharField( 
    max_length=50,
    choices=BET_TYPES, 
    default=BET_TYPES[0][0]
  )
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now=False, auto_now_add=False)
  sport = models.CharField(
    max_length=3, 
    choices=SPORTS, 
    default=SPORTS[0][0]
  )
  home_team = models.CharField(max_length=50)
  away_team = models.CharField(max_length=50)
  betting_line = models.IntegerField(default=0)
  bet_amount = models.IntegerField(default=0)
  # bet_amount = models.DecimalField(default=Decimal(0), max_digits=10, decimal_places=2)
  won = models.CharField(
    choices=BET_RESULT,
    max_length=50,
    default=BET_RESULT[0][0]
  )

  def __str__(self):
      return self.bet_type
  
  def get_absolute_url(self):
      return reverse("bets_create")
  

  # bet_track = models.ForeignKey(BetTrack, default='', on_delete=models.CASCADE)




