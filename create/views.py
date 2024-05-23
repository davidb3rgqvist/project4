from django.shortcuts import render, redirect
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from .models import Recipe

@login_required
def create_view(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except Exception as e:
                print(f"Error saving recipe: {e}")
        else:
            print(form.errors)
    else:
        form = RecipeForm()
    return render(request, 'create/create.html', {'form': form})
