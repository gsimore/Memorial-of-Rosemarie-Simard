from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, default="Untitled")
    text = models.TextField()
    image = models.ImageField(blank=True, null=True)
    has_image = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField(
        default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        if self.image != none:
            self.has_image = True
        else:
            self.has_image = False
        self.save

    def __str__(self):
        return self.title
