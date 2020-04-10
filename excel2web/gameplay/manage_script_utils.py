from . import models

g = models.Game.objects.get(pk=1)  # query by key param
# Update some attr
g.status = 'S'
g.save()
# More advance query
f_g_list = models.Game.objects.filer(status='F')
s_g_list = models.Game.objects.exclude(status='F')

"""
double underscore is a special feature of django
<foreign_key>__<table_to_look_up>
"""
g_list = models.Game.objects.filter(second_player__username='bob')
"""
Here we are using the second_player field (which is on the Game Object) as
a foreign key on the users table.
Fetch all games where bob is the second player
"""

# Make a move
m = models.Move(x=0, y=1, comment="something", by_first_player=True, game=g)
m.save()
"""
The relationship from the move side is one to one but, on the game side is one to many since
we will have multiple moves for the same game.
Since we didn't specify a name for such relationship, django creates move_set
Any model have all the filter, exclude etc methods available. Here as well
"""
moves = g.move_set



