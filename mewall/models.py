from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, default="Untitled")
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    has_image = models.BooleanField(default=False)
    published_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        import pdb; pdb.set_trace()
        if self.image == None:
            self.has_image = False
        elif self.image != None:
            self.has_image = True

        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
