from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# from taggit.managers import TaggableManager
from django.utils import timezone


class Article(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,default='')
    description = models.TextField(default='')
    slug = models.SlugField(max_length=255,default='')
    category = models.CharField(max_length=255, default='blockchain')
    body = models.TextField(default='-')
    image = models.URLField(max_length=200, default='')
    created_at = models.DateTimeField(default=timezone.now)
    # tags = TaggableManager()

    def __str__(self):
        return self.title
