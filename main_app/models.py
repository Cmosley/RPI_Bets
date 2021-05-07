from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model): 
  total_bets: models.IntegerField()
  total_wins: models.IntegerField()
  bank_roll: models.IntegerField()
  winnings: models.DecimalField(_(""), max_digits=10, decimal_places=2)


