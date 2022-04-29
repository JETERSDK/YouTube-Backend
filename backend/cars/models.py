from cgitb import text
from django.db import models
from authentication.models import User

# Create your models here.

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=30)
    text = models.CharField(max_length=100)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    
    
class Reply(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     comment = models.ForeignKey(User, on_delete=models.CASCADE)
     text = models.CharField(max_length=100)   
