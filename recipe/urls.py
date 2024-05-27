from django.urls import path
from . import views

urlpatterns = [
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:recipe_id>/like/', views.like_recipe, name='like_recipe'),
    path('recipe/<int:recipe_id>/update/', views.update_recipe, name='update_recipe'),
    path('', views.recipe_list, name='recipe_list'),
]