from django.db import models

# Create your models here.
class Post(models.Model):
    postTag = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery', null=True)

    def __str__(self):
        return self.postTag
