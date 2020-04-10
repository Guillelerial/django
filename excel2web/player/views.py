from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from gameplay.models import Game

from . import models
from . import forms


@login_required
def home(request):
    # Path is relative to the template folder on this app
    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.active()
    invitations = request.user.invitations_received.all()
    return render(request, "player/home.html",
                  {
                      'games': my_games,
                      'active_games': active_games,
                      'invitations': invitations
                   })


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


@login_required
def accept_invitation(request, id):
    invitation = get_object_or_404(models.Invitation, pk=id)
    if not request.user == invitation.to_user:
        raise PermissionDenied
    if request.method == 'POST' and "accept" in request.POST:
        game = Game.objects.create(
            first_player=invitation.to_user,
            second_player=invitation.from_user
        )
        # game.save() is not implicit on the create call
        invitation.delete()
        return redirect('player_home')

    return render(request, "player/accept_invitation_form.html", {'invitation': invitation})
