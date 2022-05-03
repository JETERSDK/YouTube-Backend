from rest_framework import serializers
from .models import Car
from .models import Reply
from .models import Comment



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'id', 'video_id', 'comment_text', 'like', 'dislike']


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['comment', 'reply_text']  