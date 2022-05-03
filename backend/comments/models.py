from django.db import models
from backend import comments


# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(comments, blank=True, null=True, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=50)
    comment_text = models.CharField(max_length=250)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

<<<<<<< HEAD
class Reply(models.Model):
    user = models.ForeignKey(Comment, blank=True, null=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, blank=True, null=True, on_delete=models.CASCADE)
    reply_text = models.CharField(max_length=250)
=======
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=30)
    texts = models.CharField(max_length=100)
    likes = models.IntegerField()
    dislikes = models.IntegerField()

class Replies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    

>>>>>>> d882f103683b1b1e2d3ab5de97fe524b778b0120
