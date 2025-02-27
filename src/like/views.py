from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView,GenericAPIView
from rest_framework import status

class LikeListCreateAPIView(ListCreateAPIView):
    serializer_class=LikeSerializer

    def get_queryset(self):
        user=self.request.user
        return Like.objects.filter(user=user)

class LikeDeleteView(GenericAPIView):
    serializer_class=LikeSerializer

    def delete(self,request,*args,**kwargs):
        like_id=kwargs.get("like_id")

        serializer=self.get_serializer()
        try:
            response= serializer.delete(request.user.id,like_id)
            return Response(response,status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)

class LikeGetByBlogView(GenericAPIView):
    serializer_class=LikeSerializer

    def get(self,request,*args,**kwargs):
        blog_id= kwargs.get("blog_id")
        try:
            blog=Blog.objects.get(id=blog_id)
            likes=Like.objects.filter(blog=blog)
            serializers=self.get_serializer(likes,many=True)
            return Response(serializers.data)
        except Blog.DoesNotExist:
            return Response({"meaasage":f"Blog with id:{blog_id} not found."},status=404)