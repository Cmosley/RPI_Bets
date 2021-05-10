from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bets/', views.bets_index, name='index'),
    path('bets/create', views.BetCreate.as_view(), name='bets_create'),
    # accounts
    path('accounts/signup/', views.signup, name='signup')
]
