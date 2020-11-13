from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=150)

class Post(models.Model):
    subject = models.CharField(max_length=100)
    created_user = models.ForeignKey(User, related_name='created_posts', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='posts_in_category', on_delete=models.CASCADE)
    message = models.TextField(max_length=4000)
     
