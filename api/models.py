from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)