from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

class Deal(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100)
    threshold = models.IntegerField(default=10)
