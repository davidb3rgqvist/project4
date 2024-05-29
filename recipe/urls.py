from django.urls import path
from . import views

urlpatterns = [
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:recipe_id>/like/', views.like_recipe, name='like_recipe'),
    path('recipe/<int:recipe_id>/update/', views.update_recipe, name='update_recipe'),
    path('add_comment/<int:recipe_id>/',  views.add_comment, name='add_comment'),
    path('recipe/<int:recipe_id>/save/', views.save_to_cookbook, name='save_to_cookbook'),
    path('recipe/<int:recipe_id>/unsave/', views.unsave_from_cookbook, name='unsave_from_cookbook'),
    path('', views.recipe_list, name='recipe_list'),
]