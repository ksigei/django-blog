from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField(max_length=200)
    content = models.TextField()
    image = models.FileField(upload_to='media')

    def __str__(self):
        return self.title
