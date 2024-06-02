from cloudinary.utils import cloudinary_url
from recipe.models import Recipe, CookbookEntry
from django.shortcuts import render
from django.db.models import Count

def home_view(request):
    """
    Add the users recipes to the cookbook, created and saved. the three latest recipes is displayed as a feature.
    """
    recipes = Recipe.objects.filter(is_public=True).order_by('-created_at')[:3]

    cookbook_recipes = []
    sort_order = request.GET.get('sort_order', 'newest')
    letter_filter = request.GET.get('letter', '')

    if request.user.is_authenticated:
        cookbook_entries = CookbookEntry.objects.filter(user=request.user)
        if letter_filter:
            cookbook_entries = cookbook_entries.filter(recipe__title__istartswith=letter_filter)
        
        if sort_order == 'likes':
            cookbook_entries = cookbook_entries.annotate(num_likes=Count('recipe__likes')).order_by('-num_likes')
        else:
            cookbook_entries = cookbook_entries.order_by('-recipe__created_at')

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
        'sort_order': sort_order
    }
    return render(request, 'home/home.html', context)