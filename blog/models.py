from django.db import models
from taggit.managers import TaggableManager

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.caption

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    gallery = models.ManyToManyField(Image, related_name='posts')

    def __str__(self):
        return self.title
