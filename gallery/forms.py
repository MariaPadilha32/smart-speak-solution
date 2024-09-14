# gallery/forms.py
from django import forms
from .models import PhotosGallery

class GalleryForm(forms.ModelForm):
   class Meta:
       model = PhotosGallery
       fields = ['author', 'title', 'description', 'image']
