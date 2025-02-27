from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError,NotFound,PermissionDenied
from blog.models import Blog
import hashlib
import datetime
import os

class BlogResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=["id","title","like_count"]


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model=Blog
        fields=["id","title","description","image","created_at","updated_at","like_count","user"]
        read_only_fields=["id","like_count","user"]

    def generate_unique_image_name(self,original_image,prefix='img'):
        current_time=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        unique_string=f"{prefix}_{current_time}"
        hash_object=hashlib.sha256(unique_string.encode())
        unique_hash=hash_object.hexdigest()

        #extract original file extension
        extension=os.path.splitext(original_image)[1]
        unique_name=f"{prefix}_{unique_hash[:16]}{extension}"
        return unique_name

    def create(self, validated_data):
        
        user=self.context.get("request").user

        if 'image' in validated_data:
            image=validated_data.pop('image')
            unique_image_name=self.generate_unique_image_name(image.name)
            image.name=unique_image_name
            validated_data['image']=image

        blog=Blog.objects.create(user=user,**validated_data)
        return blog

    def update(self, instance, validated_data):

        user=self.context.get("request").user
        if instance.user.id != user.id:
            raise PermissionDenied(detail="You do not have permission to edit this blog")

        if 'image' in validated_data:
            image=validated_data.pop('image')
            unique_image_name=self.generate_unique_image_name(image.name)
            image.name=unique_image_name
            instance.image=image

        instance.title=validated_data.get('title',instance.title)
        instance.description=validated_data.get('description',instance.description)
        instance.save()
        return instance


    