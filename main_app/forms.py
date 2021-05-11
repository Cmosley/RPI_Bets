from django.forms import ModelForm
from .models import BetTrack, Bet

class AddTrack(ModelForm):
  class Meta: 
    model = BetTrack
    fields = ['sport']

class AddBet(ModelForm):
  class Meta:
    model = Bet
    fields = '__all__'