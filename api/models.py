from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

class Comment(models.Model):
    body = models.TextField(blank=False)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    comments = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)
    posts = models.ManyToManyField('Post', related_name='categories', blank=True)