from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    # Apply resizing transformation to the photo field
    photo = CloudinaryField(
        'image',
        default='recipes/default.jpg',
        blank=True,
        transformation={'width': 1000, 'height': 800, 'crop': 'limit'}
    )
    tags = models.CharField(max_length=200, blank=True)
    is_public = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='liked_recipes', blank=True)

    def __str__(self):
        return self.title


# class Ingredient(models.Model):
#     name = models.CharField(max_length=100)
#     quantity = models.CharField(max_length=50)
#     recipe = models.ForeignKey(Recipe, related_name='ingredient_list', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name


class Photo(models.Model):
    image = CloudinaryField(
        'image',
        transformation={'width': 800, 'height': 600, 'crop': 'limit'}
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
