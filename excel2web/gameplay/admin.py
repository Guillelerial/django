from django.contrib import admin

# Register your models here.
from . import models

# Admin superuser is set to guigomcha and pwd to the simple one
# admin.site.register(models.Game)
admin.site.register(models.Move)


# Register with not just default behaviour:
@admin.register(models.Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_player', 'second_player', 'status')
    list_editable = ('status', )
