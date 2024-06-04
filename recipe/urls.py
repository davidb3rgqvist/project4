from django.urls import path
from . import views

urlpatterns = [
    path('recipe/<int:rid>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:rid>/like/', views.like_recipe, name='like_recipe'),
    path(
        'recipe/<int:rid>/update/',
        views.update_recipe,
        name='update_recipe'),
    path(
        'recipe/<int:rid>/add_comment/',
        views.add_comment,
        name='add_comment'),
    path(
        'comment/<int:cid>/edit/',
        views.edit_comment,
        name='edit_comment'),
    path(
        'comment/<int:cid>/delete/',
        views.delete_comment,
        name='delete_comment'),
    path(
        'recipe/<int:rid>/save/',
        views.save_to_cookbook,
        name='save_to_cookbook'),
    path(
        'recipe/<int:rid>/unsave/',
        views.unsave_from_cookbook,
        name='unsave_from_cookbook'),
    path('', views.recipe_list, name='recipe_list'),
]
