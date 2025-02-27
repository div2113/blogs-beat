from django.urls import path
from .views import *

urlpatterns = [
    path("",CommentListCreateAPIView.as_view()),
    path("blogs/<int:blog_id>",CommentsBlogApiView.as_view()),
    path("<int:comment_id>",CommentDeleteApiView.as_view())
   
]

