from django.contrib import admin
from .models import PhotosGalleryNew


class PhotosGalleryNewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'author',
        'image',
    )

    ordering = ('title',)


admin.site.register(PhotosGalleryNew, PhotosGalleryNewAdmin)

