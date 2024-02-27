from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Post
from api.models import Comment

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'comments']

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'user', 'comments']

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='username.username')
    class Meta:
        model = Comment
        fields = ['id', 'body', 'username', 'post']