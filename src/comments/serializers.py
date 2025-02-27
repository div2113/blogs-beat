from rest_framework import serializers
from .models import Comment
from django.contrib.auth.models import User
from blog.models import Blog
from user.serializers import UserResponseSerializer
from blog.serializers import BlogResponseSerializer
from rest_framework.exceptions import ValidationError

class CommentSerializer(serializers.ModelSerializer):
    blog_id=serializers.IntegerField(write_only=True)
    user=UserResponseSerializer(read_only=True)
    blog=BlogResponseSerializer(read_only=True)

    class Meta:
        model=Comment
        fields=["id","content","user","blog","blog_id","created_at"]
        read_only_fields=["id","user","blog"]

    
    def validate_blog_id(self,value):
        try:
            Blog.objects.get(id=value)
        except Blog.DoesNotExist:
            raise ValidationError({f"message: user with user_id:{value} not found."})
        return value
    

    def create(self, validated_data):
        user=self.context.get("request").user
        blog_id=validated_data.pop("blog_id")
        blog=Blog.objects.get(id=blog_id)

        validated_data["user"]=user
        validated_data["blog"]=blog
        return super().create(validated_data)
    
    def delete(self,user_id,comment_id):
        try:
           user= User.objects.get(id=user_id)
           comment=Comment.objects.get(id=comment_id,user=user)
           comment.delete()
           return {"message":"Comment deleted successfully"}
        except User.DoesNotExist as e:
            raise ValidationError({"message":f"user with id {user_id} not found"})
        except Comment.DoesNotExist as e:
            raise ValidationError({"message":f"user with id {comment_id} not found"})
       