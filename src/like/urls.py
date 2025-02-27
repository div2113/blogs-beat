from django.urls import path
from .views import *

urlpatterns = [
    path("",LikeListCreateAPIView.as_view()),
    path("<int:like_id>/",LikeDeleteView.as_view()),
    path("blog/<int:blog_id>",LikeGetByBlogView.as_view())
]