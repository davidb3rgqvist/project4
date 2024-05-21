from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    steps = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    tags = models.CharField(max_length=100)
    is_public = models.BooleanField(default=False)
