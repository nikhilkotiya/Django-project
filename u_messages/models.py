from django.db import models

# Create your models here.
from users.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender",on_delete=models.CASCADE)
    receiver = models.ManyToManyField(User, related_name="receiver")
    message_file = models.FileField(upload_to='mails/')
    timestamp = models.DateTimeField(auto_now_add=True)
    unread = models.BooleanField(default = True)