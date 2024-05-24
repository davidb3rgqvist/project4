from django.db import models
from cloudinary.models import CloudinaryField


# class NewRecipe(models.Model):
#     title = models.CharField(max_length=100)
#     ingredients = models.TextField()
#     steps = models.TextField()
#     photo = models.ImageField(upload_to='photos/')
#     tags = models.CharField(max_length=100)
#     is_public = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title
    
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    steps = models.TextField()
    photo = CloudinaryField('image', default='placeholder')
    tags = models.CharField(max_length=100)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title