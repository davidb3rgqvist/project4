from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Model representing a Recipe
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
