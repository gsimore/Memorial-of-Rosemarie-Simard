from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, default="Untitled")
    text = models.TextField()
    published_date = models.DateTimeField(
        default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save

    def __str__(self):
        return self.title
