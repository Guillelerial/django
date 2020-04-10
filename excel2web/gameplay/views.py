from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from gameplay.models import Game

from . import models


@login_required
def game_detail(request, id):
    game = get_object_or_404(Game, pk=id)
    return render(request, "gameplay/game_detail.html", {'game': game})