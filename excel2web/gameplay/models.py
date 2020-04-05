from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Game(models.Model):
    # player --> one to many relationship
    # CASCADE--> If the game is deleted, all moves linked will be as well
    first_player = models.ForeignKey(User, related_name="games_first_player", on_delete=models.CASCADE)
    second_player = models.ForeignKey(User, related_name="games_second_player",  on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    last_time = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=1, default='F')


class Move(models.Model):
    # Primary key included by default
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField()
    # Many to one relationship
    game = models.ForeignKey(Game,  on_delete=models.CASCADE)
