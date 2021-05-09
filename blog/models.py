from django.db import models
from users.models import User
# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=20)
    description = models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

     