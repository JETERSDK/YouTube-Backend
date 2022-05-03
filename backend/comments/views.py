from django.shortcuts import render
from .models import Comment
from .models import Reply
from .serializers import CommentSerializer
from .serializers import ReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.
class CommentList(APIView):
    def get(self, request):
        try:
            comment = Comment.objects.all()
            serializer = CommentSerializer(comment, many=True)
            return Response(serializer.data)
        except Comment.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            comment = self.get_object(pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        except Comment.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReplyList(APIView):
    def get(self, request):
        try:
            reply = Reply.objects.all()
            serializer = ReplySerializer(reply, many=True)
            return Response(serializer.data)
        except Reply.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReplyDetail(APIView):

    def get_object(self, comment):
        try:
            return Reply.objects.filter(comment=comment)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, comment):
        try:
            reply = self.get_object(comment)
            serializer = ReplySerializer(reply, many=True)
            return Response(serializer.data)
        except Comment.DoesNotExist:
            raise Http404

    def put(self, request, comment):
        comment = self.get_object(comment)
        serializer = ReplySerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, comment):
        reply = self.get_object(comment)
        reply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentLike(APIView):

    def get_object(self, pk, video_id):
        try:
            return Comment.objects.get(pk=pk, video_id=video_id)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk, video_id):
        try:
            comment = self.get_object(pk, video_id=video_id)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        except Comment.DoesNotExist:
            raise Http404

    def patch(self, request, pk, video_id):
        try:
            comment = self.get_object(pk, video_id=video_id)
            data = {"like": comment.like + int(1)}
            serializer = CommentSerializer(comment, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Comment.DoesNotExist:
            raise Http404


class CommentDislike(APIView):

    def get_object(self, pk, video_id):
        try:
            return Comment.objects.get(pk=pk, video_id=video_id)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk, video_id):
        try:
            comment = self.get_object(pk=pk, video_id=video_id)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        except Comment.DoesNotExist:
            raise Http404

    def patch(self, request, pk, video_id):
        try:
            comment = self.get_object(pk=pk, video_id=video_id)
            data = {"dislike": comment.dislike + int(1)}
            serializer = CommentSerializer(comment, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Comment.DoesNotExist:
            raise Http404


# Create your views here.
