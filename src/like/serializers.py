from rest_framework import serializers
from .models import Like
from django.contrib.auth.models import User
from blog.models import *
from rest_framework.exceptions import ValidationError
from user.serializers import UserResponseSerializer
from blog.serializers import BlogResponseSerializer


class LikeSerializer(serializers.ModelSerializer):
    blog_id=serializers.IntegerField(write_only=True)
    user=UserResponseSerializer(read_only=True)
    blog=BlogResponseSerializer(read_only=True)

    class Meta:
        model=Like
        fields=["id","blog_id","user","blog"]
        read_only_fields=["id","user","blog"]

    
    def validate_blog_id(self,value):
        if not Blog.objects.filter(id=value).exists():
            raise ValidationError("Blog not found.")
        return value
    
    def create(self, validated_data):
        blog_id=validated_data.pop("blog_id")
        user=self.context.get("request").user
        blog=Blog.objects.get(id=blog_id)
        validated_data["user"]=user
        validated_data["blog"]=blog 

        if Like.objects.filter(user=user,blog=blog).exists():
            raise ValidationError({"message":"User has already liked this blog."})
        like=Like.objects.create(**validated_data)
        blog.like_count+=1
        blog.save()
        return like
     
    def delete(self,user_id,like_id):
        try:
            like=Like.objects.get(id=like_id,user_id=user_id)
        except Like.DoesNotExist:
            raise ValidationError("Like not found.")
        
        blog=like.blog
        like.delete()
        blog.like_count-=1
        blog.save()
        return {"message":"Like deleted successfully."}