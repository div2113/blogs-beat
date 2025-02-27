from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from.models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

class CustomPagination(PageNumberPagination):
    page_size=2  #overide default page size
    page_size_query_param='size' #allow client to set page size with ?size=20
    max_page_size=4


class BlogRetriveApiView(ListAPIView):
    serializer_class=BlogSerializer

    def get_queryset(self):
        return Blog.objects.filter(user=self.request.user)


class BlogListCreateAPIView(ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    pagination_class=CustomPagination
    filter_backends=[filters.OrderingFilter]
    ordering_fields=["id","title","created_at","updated_at"]
    ordering='id'

    def get_permissions(self):
        if(self.request.method=='GET'):
            return [AllowAny()]
        return [IsAuthenticated()]

class BlogRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

    def destroy(self, request, *args, **kwargs):
        if (request.user.id != self.get_object().user.id):
            raise PermissionDenied(detail="You do not have permission to edit this blog") 
        return super().destroy(request, *args, **kwargs)

