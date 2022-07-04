from django.db import models
import datetime

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=30)
    time = models.DateTimeField()

    def __str__(self):
        return self.title



