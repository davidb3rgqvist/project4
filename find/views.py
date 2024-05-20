from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def find_recipe(request):
    return HttpResponse("This would be the find recipe page")

