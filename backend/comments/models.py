from django.db import models
from backend import comments

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(comments, blank=True, null=True, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=50)
    comment_text = models.CharField(max_length=250)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

class Reply(models.Model):
    user = models.ForeignKey(Comment, blank=True, null=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, blank=True, null=True, on_delete=models.CASCADE)
    reply_text = models.CharField(max_length=250)
