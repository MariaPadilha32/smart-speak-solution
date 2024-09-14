# gallery/admin.py
from django.contrib import admin
from .models import PhotosGallery

class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'author',
        'image',
    )

    ordering = ('title',)


admin.site.register(PhotosGallery, GalleryAdmin)
