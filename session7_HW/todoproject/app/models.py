from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    now_date = models.DateField(auto_now=True)
    end_date = models.DateField()
    

    def __str__(self):
        return self.title   