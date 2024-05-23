from django.shortcuts import render
from recipe.models import Recipe

def home_view(request):
    recipes = Recipe.objects.filter(is_public=True).order_by('-created_at')[:3]
    context = {'recipes': recipes}
    return render(request, 'home/home.html', context)
