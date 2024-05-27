from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm
from .models import Recipe
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
                user = request.user,
                tags=form.cleaned_data['tags'],
                is_public=form.cleaned_data['is_public'],
            )


            return redirect('recipe_detail', recipe_id=new_recipe.id)
    else:
        form = RecipeForm()
    return render(request, 'recipe/create.html', {'form': form})



# def upload_photo(request):
#     if request.method == 'POST':
#         form = PhotoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('photo_list')
#     else:
#         form = PhotoForm()
#     return render(request, 'upload_photo.html', {'form': form})

# def photo_list(request):
#     photos = Photo.objects.all()
#     return render(request, 'photo_list.html', {'photos': photos})


@login_required
def update_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if recipe.user != request.user:
        messages.error(request, "You are not authorized to edit this recipe.")
        return redirect('recipe_detail', recipe_id=recipe.id)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe/update_recipe.html', {'form': form, 'recipe': recipe})

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if recipe.user != request.user:
        messages.error(request, "You are not authorized to delete this recipe.")
        return redirect('recipe_detail', recipe_id=recipe.id)

    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'recipe/delete.html', {'recipe': recipe})
