from django.shortcuts import render
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Recipe


def create_view(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('home_view')  
            except Exception as e:
                print(f"Error saving recipe: {e}")
               
        else:
            print(form.errors)
    else:
        form = RecipeForm()
    return render(request, 'create/create.html', {'form': form})