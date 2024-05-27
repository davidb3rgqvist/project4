from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, PhotoForm
from .models import Recipe, Photo
from django.contrib import messages


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/recipe_list.html', {'recipes': recipes})

@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
           
            new_recipe = Recipe.objects.create(
                title=form.cleaned_data['title'],
                ingredients=form.cleaned_data['ingredients'],
                steps=form.cleaned_data['steps'],
                photo=form.cleaned_data['photo'],
                tags=form.cleaned_data['tags'],
                is_public=form.cleaned_data['is_public']
            )
            
            
            return redirect('recipe_detail', recipe_id=new_recipe.id)
    else:
        form = RecipeForm()
    return render(request, 'recipe/create.html', {'form': form})


def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'upload_photo.html', {'form': form})

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo_list.html', {'photos': photos})
