from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Diary(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, models.CASCADE, related_name="posts")

    def __Str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    author = models.ForeignKey(User, models.CASCADE, related_name="comments")

    def __str__(self):
        return self.content

