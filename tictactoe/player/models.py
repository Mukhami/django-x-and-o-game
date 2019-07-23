from django.db import models
from django.contrib.auth.models import User


class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name="invitation_sent", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="invitation_received", verbose_name="User to Invite", help_text="Select user you want to play against", on_delete=models.CASCADE)
    message = models.CharField(max_length=300, blank=True, verbose_name="Optional Message", help_text="Add an optional friendly message")
    timestamp = models.DateTimeField(auto_now_add=True)
