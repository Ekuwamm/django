from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(blank=True)

    def __str__(self):
        return self.title
    