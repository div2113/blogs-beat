from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated

class ProfileRetriveView(RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user

class UserListCreateApiView(ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

    def get_permissions(self):
        if(self.request.method=='POST'):
            return [AllowAny()]
        return [IsAuthenticated()]

class UserRetriveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
