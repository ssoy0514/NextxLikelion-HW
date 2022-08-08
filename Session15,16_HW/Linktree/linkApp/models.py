from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, blank=True,)
    
    def __str__(self):
        return str(self.name)
    
class Link(models.Model):
    link = models.URLField(max_length=1000,blank=True)
    link_name = models.CharField(max_length=500,blank=True)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name='link',default=None, blank=True, null=True)
    memo = models.CharField(max_length=500,blank=True)
    def __str__(self):
        return str(self.link_name)
        