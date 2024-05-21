from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_recipe(request):
    return HttpResponse("This would be the find home page")

