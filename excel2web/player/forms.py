from django.forms import ModelForm

from . import models


class InvitationForm(ModelForm):
    # Meta class is common usage on django. This tells what model this form is based on
    class Meta:
        model = models.Invitation
        # from_user is always itself and timestamp should be real timestamp of creation
        exclude = ('from_user', 'timestamp')