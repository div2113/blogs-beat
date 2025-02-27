from rest_framework import serializers
from django.contrib.auth.models import User

class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email"]

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model= User
        fields=["id","username","email","password","date_joined"]
        read_only_fields=["id","date_joined"]

    def create(self, validated_data):
        user=User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self,instance,validated_data):
        instance.username=validated_data.get('username',instance.username)
        instance.email=validated_data.get('email',instance.email)
        password=validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.save()
        return instance