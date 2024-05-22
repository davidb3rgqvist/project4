from django.shortcuts import render
from .models import Recipe

def home_view(request):
    recipes = Recipe.objects.filter(is_public=True).order_by('-created_at')[:3]  # Get latest recipes
    print(recipes)  # Print the recipe list for debugging
    context = {'recipes': recipes}
    return render(request, 'home.html', context)