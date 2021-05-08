from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bets/', views.bets_index, name='index'),
    # accounts
    path('accounts/signup/', views.signup, name='signup')
]
