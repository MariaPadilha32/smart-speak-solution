# gallery/models.py
from django.db import models

class PhotosGallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/')
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title