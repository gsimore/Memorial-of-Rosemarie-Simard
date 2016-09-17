from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, default="Untitled")
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True,)
    has_image = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        if self.image == None:
            self.has_image == False
        else:
            self.has_image == True
        self.published_date = timezone.now()
        self.save

    def __str__(self):
        return self.title
