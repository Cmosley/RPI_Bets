from django.contrib import admin
from .models import Profile, Bet, BetTrack
# Register your models here.

admin.site.register(Profile)
admin.site.register(Bet)
admin.site.register(BetTrack)