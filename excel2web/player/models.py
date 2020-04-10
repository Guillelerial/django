from django.db import models
from django.contrib.auth.models import User


class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name="invitations_sent", on_delete=models.CASCADE,
                                  verbose_name="user to invite", help_text="some extra help text")
    to_user = models.ForeignKey(User, related_name="invitations_received", on_delete=models.CASCADE)
    message = models.CharField(max_length=300, blank=True, verbose_name="Optional message",
                               help_text="some extra help text")
    timestamp = models.DateTimeField(auto_now_add=True)
