from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import truncatechars
from django.http import JsonResponse, HttpResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Recipe, Comment, CookbookEntry
from .forms import RecipeForm, CommentForm
from django.urls import reverse


def recipe_detail(request, recipe_id):
    """
    Display details of a recipe including comments and comment form.
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    comments = recipe.comments.all()
    comment_form = CommentForm()
    is_saved = CookbookEntry.objects.filter(user=request.user, recipe=recipe).exists()
    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe, 'comments': comments, 'comment_form': comment_form, 'is_saved': is_saved})


def recipe_list(request):
    """
    Display a list of recipes with optional sorting and filtering.
    """
    sort_order = request.GET.get('sort_order', 'newest')
    letter_filter = request.GET.get('letter', '')

    if letter_filter:
        recipes = Recipe.objects.filter(is_public=True, title__istartswith=letter_filter)
    else:
        recipes = Recipe.objects.filter(is_public=True)

    if sort_order == 'likes':
        recipes = recipes.annotate(num_likes=Count('likes')).order_by('-num_likes')
    else:
        recipes = recipes.order_by('-created_at')

    return render(request, 'recipe/recipe_list.html', {'recipes': recipes, 'sort_order': sort_order})


@login_required
def create_recipe(request):
    """
    Create a new recipe.
    """
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)

        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.user = request.user
            recipe.save()

            CookbookEntry.objects.create(user=request.user, recipe=recipe)
            messages.success(request, 'Recipe created successfully!')

            return redirect('recipe_list')
        else:
            messages.error(request, 'There was an error creating the recipe.')
    else:
        recipe_form = RecipeForm()

    return render(request, 'recipe/create.html', {
        'recipe_form': recipe_form,
    })


@login_required
def update_recipe(request, recipe_id):
    """
    Update an existing recipe.
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if recipe.user != request.user:
        messages.error(request, "You are not authorized to edit this recipe.")
        return redirect('recipe_detail', recipe_id=recipe.id)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recipe updated successfully.')
            return redirect('recipe_detail', recipe_id=recipe.id)
        else:
            messages.error(request, 'There was an error updating the recipe. Please check the form.')
    else:
        form = RecipeForm(instance=recipe)

    if form.instance.photo:
        form.instance.photo.url_truncated = truncatechars(form.instance.photo.url, 5)

    return render(request, 'recipe/create.html', {'recipe_form': form})


@login_required
def delete_recipe(request, recipe_id):
    """
    Delete a recipe.
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if recipe.user != request.user:
        messages.error(request, "You are not authorized to delete this recipe.")
        return redirect('recipe_detail', recipe_id=recipe.id)

    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'recipe/delete.html', {'recipe': recipe})


@login_required
def like_recipe(request, recipe_id):
    """
    Like or unlike a recipe.
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user in recipe.likes.all():
        recipe.likes.remove(request.user)
    else:
        recipe.likes.add(request.user)
    return redirect('recipe_detail', recipe_id=recipe.id)
    

@login_required
def add_comment(request, recipe_id):
    """
    Add a comment to a recipe.
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.recipe = recipe
            comment.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    return redirect('recipe_detail', recipe_id=recipe.id)


@login_required
def edit_comment(request, comment_id):
    """
    Edit a comment on a recipe.
    """
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', recipe_id=comment.recipe.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'recipe_detail.html', {'form': form, 'comment': comment})


@login_required
def delete_comment(request, comment_id):
    """
    Delete a comment on a recipe.
    """
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    recipe_id = comment.recipe.id
    comment.delete()
    return redirect('recipe_detail', recipe_id=recipe_id)


@login_required
def save_to_cookbook(request, recipe_id):
    """
    Save a recipe to the user's cookbook.
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user != recipe.user:
        CookbookEntry.objects.get_or_create(user=request.user, recipe=recipe)
    return redirect('recipe_detail', recipe_id=recipe_id)


@login_required
def unsave_from_cookbook(request, recipe_id):
    """
    Remove a recipe from the user's cookbook.
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    CookbookEntry.objects.filter(user=request.user, recipe=recipe).delete()
    return redirect('recipe_detail', recipe_id=recipe_id)
