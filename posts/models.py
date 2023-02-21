from django.db import models
from django.contrib.auth.models import User
# inheritance
# Create your models here.
class Post(models.Model):
    title = models.TextField(max_length=200)
    content = models.TextField()
    image = models.FileField(upload_to='media')
    # author
    # author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Comment(models.Model):
    # post = pass
    # content = pass

  