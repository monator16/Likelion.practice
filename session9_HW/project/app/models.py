from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    content = models.TextField()
