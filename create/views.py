from django.shortcuts import render
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def create_view(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_view')
    else:
        form = RecipeForm()
    return render(request, 'create/create.html', {'form': form})
