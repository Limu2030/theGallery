from django.contrib import admin

# Register your models here.

from .models import Category, Location, Photo

admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Location)