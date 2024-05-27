from cloudinary.utils import cloudinary_url
from recipe.models import Recipe
from django.shortcuts import render


def home_view(request):
    recipes = Recipe.objects.order_by('-created_at')[:3]
    for recipe in recipes:
        if recipe.photo:
            recipe.photo_url, options = cloudinary_url(recipe.photo.public_id, width=400, height=300, crop="fill")
        else:
            recipe.photo_url = None
    context = {
        'recipes': recipes
    }
    return render(request, 'home/home.html', context)