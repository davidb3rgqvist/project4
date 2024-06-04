from django.contrib import admin
from .models import Recipe, Comment, CookbookEntry

# Registering models with the Django admin site
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(CookbookEntry)
