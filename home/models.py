from django.db import models
from django.utils import timezone

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title