from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from login.views import register_view
from home.views import home_view
from recipe.views import recipe_detail, recipe_list, update_recipe, delete_recipe
from recipe.views import create_recipe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', register_view, name='register'),
    path('logout/', LogoutView.as_view(template_name='logout/logout.html'), name='logout'),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('recipe/<int:recipe_id>/update/', update_recipe, name='update_recipe'),
    path('recipe/<int:recipe_id>/delete/', delete_recipe, name='delete_recipe'),
    path('recipes/', recipe_list, name='recipe_list'),
    path('', home_view, name='home'),
    path('create/', create_recipe, name='create'),
]