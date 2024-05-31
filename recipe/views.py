from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from .models import Recipe, Comment, CookbookEntry
from .forms import RecipeForm, CommentForm

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    comments = recipe.comments.all()
    comment_form = CommentForm()
    is_saved = CookbookEntry.objects.filter(user=request.user, recipe=recipe).exists()
    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe, 'comments': comments, 'comment_form': comment_form, 'is_saved': is_saved,})


def recipe_list(request):
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
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)

        if recipe_form.is_valid(): # and ingredient_formset.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.user = request.user
            recipe.save()

            CookbookEntry.objects.create(user=request.user, recipe=recipe)

            # for form in ingredient_formset:
            #     ingredient = form.save(commit=False)
            #     ingredient.recipe = recipe
            #     ingredient.save()

            return redirect('recipe_list')
    else:
        recipe_form = RecipeForm()
        # ingredient_formset = IngredientFormSet(prefix='ingredients')

    return render(request, 'recipe/create.html', {
        'recipe_form': recipe_form,
        # 'ingredient_formset': ingredient_formset,
    })


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


@login_required
def like_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    liked = False

    if request.method == 'POST':
        if request.user in recipe.likes.all():
            recipe.likes.remove(request.user)
        else:
            if recipe.user != request.user:
                recipe.likes.add(request.user)
                liked = True

    return redirect('recipe_detail', recipe_id=recipe_id)
    

@login_required
def add_comment(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.recipe = recipe
            comment.save()
    return redirect('recipe_detail', recipe_id=recipe_id)


@login_required
def save_to_cookbook(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user != recipe.user:
        CookbookEntry.objects.get_or_create(user=request.user, recipe=recipe)
    return redirect('recipe_detail', recipe_id=recipe_id)

@login_required
def unsave_from_cookbook(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    CookbookEntry.objects.filter(user=request.user, recipe=recipe).delete()
    return redirect('recipe_detail', recipe_id=recipe_id)