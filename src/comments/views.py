from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,GenericAPIView
from .serializers import CommentSerializer
from .models import Comment
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from blog.models import Blog


class CommentListCreateAPIView(ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer



class CommentsBlogApiView(GenericAPIView):
    serializer_class=CommentSerializer

    def get(self,request,*args,**kwargs):
        blog_id=kwargs.get("blog_id")

        try:
            blog=Blog.objects.get(id=blog_id)
            comments=Comment.objects.filter(blog=blog)
            serializers= self.get_serializer(comments,many=True)
            return Response(serializers.data)
        except Blog.DoesNotExist:
            return Response({"meaasage":f"Blog with id:{blog_id} not found."},status=404)
          

class CommentDeleteApiView(GenericAPIView):
    serializer_class=CommentSerializer

    def delete(self,request,*args,**kwargs):
        user_id=kwargs.get("user_id")
        comment_id=kwargs.get("comment_id")
        serializer=self.get_serializer()
        response_data=serializer.delete(request.user.id,comment_id)
        return Response(response_data)
           