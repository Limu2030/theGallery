from django.db import models



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return self.name

class Location(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.location 

class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.description       
