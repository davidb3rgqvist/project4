from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    steps = models.TextField()
    photo = CloudinaryField('image', default='recipes/default.jpg', blank=True)
    tags = models.CharField(max_length=200, blank=True)
    is_public = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    

class Photo(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=100)
    description = models.TextField()

