from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
# Import the login_required decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bet, BetTrack
from .forms import AddTrack, AddBet
from datetime import date
import requests
import os 
from dotenv import load_dotenv
import dateutil.parser

#  API INFO 
load_dotenv()
key = os.environ['API_KEY']

url = "https://therundown-therundown-v1.p.rapidapi.com/"
headers = {
  'x-rapidapi-host': "therundown-therundown-v1.p.rapidapi.com",
  'x-rapidapi-key': key
  }
# Endpoints
sports = "sports"
mlb_events = "sports/3/events/"

# get current day
today = date.today()
urlToday = today.strftime("%Y-%m-%d")
crazydate = "2021-05-13T00:10:00Z"
normaldate = dateutil.parser.isoparse(crazydate)
# Create your views here.

def home(request):
  date = normaldate
  return render(request, 'home.html', {'date': date})

def get_lines(line_periods):
  bets = {}
  bets["moneylines"] = []
  bets["spreads"] = []
  bets["totals"] = []
  for line_index in line_periods:
      line = line_periods[line_index]['period_full_game']
      affiliate = line['affiliate']['affiliate_name']

      bets["moneylines"].append("{0} : {1} {2}".format((line['moneyline']['moneyline_home_delta']-line['moneyline']['moneyline_home']), (line['moneyline']['moneyline_away']-line['moneyline']['moneyline_away_delta']), affiliate))

      bets["spreads"].append("{0} : {1} {2}".format((line['spread']['point_spread_home_delta']-line['spread']['point_spread_home']), (line['spread']['point_spread_away']-line['spread']['point_spread_away_delta']), affiliate))

      bets["totals"].append("over/under {0} - {1} ".format((line['total']['total_over']-line['total']['total_over_delta']), affiliate))
  return bets

def sports(request):
  querystring = {"include":["all_periods","scores"]}
  response = requests.get(url + mlb_events + urlToday, headers=headers, params=querystring).json()
  events = []
  for event in response['events']:
      event_data = {}
      event_data['time'] = dateutil.parser.isoparse(event['event_date'])    
      event_data['place'] =  "{0}, {1}".format(event['score']['venue_name'], event['score']['venue_location'])
      event_data['teams'] = "{0} - {1}".format(event['teams'][1]['name'], event['teams'][0]['name'])
      event_data['bets'] = get_lines(event['line_periods'])
      events.append(event_data)
  return render(request, 'sports.html', {'events' : events})



@login_required
def bets_index(request):
  bets = Bet.objects.filter(user=request.user)
  tracks = BetTrack.objects.filter(user=request.user)
  add_track = AddTrack()
  add_bet = AddBet()
  # bets = Bet.objects.filter(user=request.user)
  # betTrack = BetTrack.objects.filter(user=request.user)
  return render(request, 'bets/index.html', {
    'add_track': add_track,
    'add_bet': add_bet,
    'tracks': tracks,
    'bets': bets,
    })

def add_track(request): 
  form = AddTrack(request.POST)
  if form.is_valid():
    new_track = form.save(commit=False)
    new_track.user = request.user 
    new_track.save()
  return redirect('index')

# def add_bet(request, bet_track_id):
#   form = AddBet(request.POST)
#   tracks = BetTrack.objects.filter(user=request.user)
#   if form.is_valid():
#     new_bet = form.save(commit=False)
#     new_bet.bet_track = bet_track_id
#     new_bet.save()
#   return render(request, 'bet_form.html', {'form':form, 'tracks':tracks})

@login_required
def bets_track(request):
  tracks = BetTrack.objects.filter(user=request.user)
  # track = BetTrack.objects.get(id=)
  return render(request, 'bets/track.html', {'tracks': tracks})

class BetTrackCreate(CreateView):
  model = BetTrack
  fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class BetCreate(LoginRequiredMixin, CreateView, ):
  model = Bet 
  fields = ['bet_type', 'date', 'sport','home_team', 
  'away_team','betting_line', 'bet_amount','won' ]
  extra_context={'tracks': BetTrack.objects.all()}
  success_url = '/bets/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class BetUpdate(LoginRequiredMixin, UpdateView):
  model = Bet
  fields = ['won']

class BetDelete(LoginRequiredMixin, DeleteView):
  model = Bet
  success_url = '/bets/'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)