from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

# Create your models here.

GAME_STATUS_MAP = [
    ('F', 'First Player to move'),
    ('S', 'Second player to move'),
    ('W', 'First player wins'),
    ('L', 'Second player wins'),
    ('D', 'Draw')
]


class GamesQuerySet(models.QuerySet):
    """
    Have a QuerySet class allow us to define the 'API' for this app
     and to keep the views.py files as limited as possible to just the calls to render.
    """
    def games_for_user(self, user):
        return self.filter(
            Q(first_player=user) | Q(second_player=user)
        )

    def active(self):
        return self.filter(
            Q(status='F') | Q(status='S')
        )


class Game(models.Model):
    # player --> one to many relationship
    # CASCADE--> If the game is deleted, all moves linked will be as well
    first_player = models.ForeignKey(User, related_name="games_first_player", on_delete=models.CASCADE)
    second_player = models.ForeignKey(User, related_name="games_second_player",  on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    last_time = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=1, default='F', choices=GAME_STATUS_MAP)

    objects = GamesQuerySet.as_manager()

    def __str__(self):
        # This is what will be shown on the UI to represent a Game entry
        return f"{self.first_player} vs {self.second_player}"


class Move(models.Model):
    # Primary key included by default
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField()
    # Many to one relationship
    game = models.ForeignKey(Game,  on_delete=models.CASCADE)
