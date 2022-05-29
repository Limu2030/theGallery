from django.shortcuts import render

# Create your views here.

def gallery(request):
    return render(request, 'pics/gallery.html')

def viewPhoto(request):
    return render(request, 'pics/photo.html')

def addPhoto(request):
    return render(request, 'pics/add.html')


