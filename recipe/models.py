from django.db import models

class NewRecipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    steps = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    tags = models.CharField(max_length=100)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Recipe(models.Model):
    # Define fields and methods for the Recipe model
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    steps = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    tags = models.CharField(max_length=100)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title