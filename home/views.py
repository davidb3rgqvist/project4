from cloudinary.utils import cloudinary_url
from recipe.models import Recipe, CookbookEntry
from django.shortcuts import render

def home_view(request):
    recipes = Recipe.objects.filter(is_public=True).order_by('-created_at')[:3]
    
    cookbook_recipes = []
    if request.user.is_authenticated:
        cookbook_entries = CookbookEntry.objects.filter(user=request.user)
        for entry in cookbook_entries:
            recipe = entry.recipe
            if recipe.photo:
                recipe.photo_url, options = cloudinary_url(recipe.photo.public_id, width=400, height=300, crop="fill")
            else:
                recipe.photo_url = None
            cookbook_recipes.append(recipe)

    context = {
        'recipes': recipes,
        'cookbook_recipes': cookbook_recipes,
    }
    return render(request, 'home/home.html', context)