from django.urls import path
from .views import *

urlpatterns = [
    path("",BlogListCreateAPIView.as_view()),
    path("<int:pk>",BlogRetrieveUpdateDestroyAPIView.as_view()),
     path("self/",BlogRetriveApiView.as_view())

]