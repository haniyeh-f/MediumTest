from django.db import models

# Create your models here.
from django.utils import timezone


class Article(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    slug=models.SlugField(max_length=255)
    category=models.CharField(max_length=255,default='blockchain')
    body = models.TextField(default='-')
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title