from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sports/', views.sports, name='sports'),
    path('bets/', views.bets_index, name='index'),
    path('bets/add_track', views.add_track, name='add_track'),
    # path('bets/create', views.add_bet, name='add_bet'),
    path('bets/track', views.bets_track, name='bet_track'),
    path('bets/create', views.BetCreate.as_view(), name='bets_create'),
    path('bettrack/create', views.BetTrackCreate.as_view(), name='bettrack_create'),
    # accounts
    path('accounts/signup/', views.signup, name='signup')
]
