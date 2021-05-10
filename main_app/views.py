from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
# Import the login_required decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bet, BetTrack
from .forms import AddTrack

# Create your views here.

def home(request):
  return render(request, 'home.html')

@login_required
def bets_index(request):
  tracks = BetTrack.objects.filter(user=request.user)
  add_track = AddTrack()
  # bets = Bet.objects.filter(user=request.user)
  # betTrack = BetTrack.objects.filter(user=request.user)
  return render(request, 'bets/index.html', {
    'add_track': add_track,
    'tracks': tracks,
    })

def add_track(request): 
  form = AddTrack(request.POST)
  if form.is_valid():
    new_track = form.save(commit=False)
    new_track.user = request.user 
    # new_track.active = True
    # new_track.total_bet = 0
    # new_track.total_net = 0
    new_track.save()
  return redirect('index')

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

class BetCreate(CreateView):
  model = Bet 
  fields = ['bet_type', 'end', 'sport','home_team', 
  'away_team','betting_line', 'bet_amount','won' ] 

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


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