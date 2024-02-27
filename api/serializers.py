from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.usernmame')
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'user']