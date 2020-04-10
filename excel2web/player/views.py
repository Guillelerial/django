from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from gameplay.models import Game

from . import models
from . import forms


@login_required
def home(request):
    # Path is relative to the template folder on this app
    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.active()
    return render(request, "player/home.html", {'games': my_games, 'active_games': active_games})


@login_required
def new_invitation(request):
    if request.method == 'POST':
        # Model on the Form now takes info from the invitation model we are passing
        invitation = models.Invitation(from_user=request.user)
        form = forms.InvitationForm(instance=invitation, data=request.POST)
        if form.is_valid():
            form.save()  # Adds data to the db
            return redirect('player_home')
    else:
        form = forms.InvitationForm()
    # Form will be the same as we received in case validation was not successful
    return render(request, "player/new_invitation_form.html", {'form': form})
