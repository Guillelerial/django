from django.shortcuts import render

from gameplay.models import Game


# Create your views here.
def home(request):
    # Path is relative to the template folder on this app
    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.active()
    return render(request, "player/home.html", {'games': my_games, 'active_games':active_games})
