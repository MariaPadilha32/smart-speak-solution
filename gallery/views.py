# gallery/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import PhotosGallery
from .forms import GalleryForm

def gallery(request):
    photos = Gallery.objects.all()
    #total = photos.count() # SELECT COUNT(*) FROM TALE
    if (photos is None):
        print(True)
    else:
        print(False)
    #total = total.count
    total = Gallery.objects.values_list()

    list_photos = []    
    if total.count > 0:
        for photo in range(0, total):
            list_photos.append(photos[photo])
    return render(request, 'gallery/gallery.html', {'photos': photos, 'total' : total, 'post_list' : list_photos})

def new_photo(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
        else:
            print(form.errors)
            #return redirect('home')
    else:
        form = GalleryForm()
    return render(request, 'gallery/new_photo.html', {'form': form})

def edit_photo(request, pk):
    photo = get_object_or_404(Gallery, pk=pk)
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = GalleryForm(instance=photo)
    return render(request, 'gallery/edit_photo.html', {'form': form})

def delete_photo(request, pk):
    photo = get_object_or_404(Gallery, pk=pk)
    if request.method == 'POST':
        photo.delete()
        return redirect('gallery')
    return render(request, 'gallery/delete_photo.html', {'photo': photo})
