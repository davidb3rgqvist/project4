from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from login.views import register_view
from home.views import home_view
from recipe.views import (
    recipe_detail, recipe_list, update_recipe, delete_recipe, like_recipe,
    create_recipe, add_comment, save_to_cookbook, unsave_from_cookbook,
    edit_comment, delete_comment
)

# URL patterns for the project
urlpatterns = [
    path(
        'admin/',
        admin.site.urls),
    path(
        'login/',
        LoginView.as_view(template_name='registration/login.html'),
        name='login'),
    path(
        'register/',
        register_view, name='register'),
    path(
        'summernote/',
        include('django_summernote.urls')),
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='logout/logout.html'),
        name='logout'),
    path(
        'recipe/<int:recipe_id>/',
        recipe_detail,
        name='recipe_detail'),
    path(
        'recipe/<int:recipe_id>/update/',
        update_recipe,
        name='update_recipe'),
    path(
        'recipe/<int:recipe_id>/delete/',
        delete_recipe,
        name='delete_recipe'),
    path(
        'recipe/<int:recipe_id>/like/',
        like_recipe,
        name='like_recipe'),
    path(
        'recipe/<int:recipe_id>/comment/',
        add_comment,
        name='add_comment'),
    path(
        'comment/<int:comment_id>/edit/',
        edit_comment,
        name='edit_comment'),
    path(
        'comment/<int:comment_id>/delete/',
        delete_comment,
        name='delete_comment'),
    path(
        'recipe/<int:recipe_id>/save/',
        save_to_cookbook,
        name='save_to_cookbook'),
    path(
        'recipe/<int:recipe_id>/unsave/',
        unsave_from_cookbook,
        name='unsave_from_cookbook'),
    path(
        'recipes/',
        recipe_list,
        name='recipe_list'),
    path(
        '',
        home_view,
        name='home'),
    path(
        'create/',

        create_recipe,
        name='create'),
]
