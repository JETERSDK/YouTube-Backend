from django.urls import path
from . import views


urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),

    path('comments/reply/', views.ReplyList.as_view()),
    path('comments/reply/<int:comment>/', views.ReplyDetail.as_view()),

    path('comments/<int:pk>/<str:video_id>/1/', views.CommentLike.as_view()),
    path('comments/<int:pk>/<str:video_id>/2/', views.CommentDislike.as_view()),
]