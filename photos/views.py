from django.shortcuts import render
from .models import Category, Photo

# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()

    context = {'categories': categories, 'photos': photos}
    return render(request, 'pics/gallery.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'pics/photo.html', {'photo': photo})

def addPhoto(request):
    return render(request, 'pics/add.html')


