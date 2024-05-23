from django.urls import path
from . import views

urlpatterns = [
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('', views.recipe_list, name='recipe_list'),
]
