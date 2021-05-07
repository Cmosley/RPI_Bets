from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


# Create your models here.



class Profile(models.Model): 
  total_bets: models.IntegerField()
  total_wins: models.IntegerField()
  bank_roll: models.IntegerField()
  winnings: models.DecimalField('winnings', max_digits=10, decimal_places=2)
  user = models.OneToOneField(User, on_delete=models.CASCADE)

 

class Bet(models.Model):
  SPORTS = (
  ('MLB', 'Baseball'),
  ('NHL', 'Hockey')
  )
  BET_TYPES = (
    ('A', 'A Bet'),
    ('B', 'B Bet'),
    ('C', 'C Bet'),
    ('D', 'D Bet'),
  )
  type = models.CharField('type', 
    max_length=50,
    choices=BET_TYPES, 
    default='A'
  )
  start = models.DateTimeField('start', auto_now=False, auto_now_add=True)
  end = models.DateTimeField('end', auto_now=False, auto_now_add=False)
  sport = models.CharField(
    max_length=3, 
    choices=SPORTS, 
    default=SPORTS[0]
  )
  home_team = models.CharField(max_length=50)
  away_team = models.CharField(max_length=50)
  betting_line = models.IntegerField()
  bet_amount = models.DecimalField(max_digits=10, decimal_places=2)

# class BetTrack(models.Model):
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
#   created= models.DateTimeField('created', auto_now=False, auto_now_add=True)


#   def __str__(self):
#       return self.name