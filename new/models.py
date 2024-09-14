from django.db import models
from django.contrib.auth.models import User

class PhotosGalleryNew(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/')
    author = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return self.title

    def get_display_name(self):
        return self.title