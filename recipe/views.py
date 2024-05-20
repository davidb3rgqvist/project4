from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def recipe_view(request):
    return HttpResponse("This would be the view recipe page")

