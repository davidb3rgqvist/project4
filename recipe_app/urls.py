from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from login.views import register_view
from home.views import home_view
from recipe.views import recipe_detail, recipe_list, update_recipe, delete_recipe, like_recipe, add_comment, save_to_cookbook, unsave_from_cookbook
from recipe.views import create_recipe

# URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),  # Login URL
    path('register/', register_view, name='register'),  # Register URL
    path('summernote/', include('django_summernote.urls')),  # Summernote URL
    path('logout/', auth_views.LogoutView.as_view(template_name='logout/logout.html'), name='logout'),  # Logout URL
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),  # Recipe detail URL
    path('recipe/<int:recipe_id>/update/', update_recipe, name='update_recipe'),  # Recipe update URL
    path('recipe/<int:recipe_id>/delete/', delete_recipe, name='delete_recipe'),  # Recipe delete URL
    path('recipe/<int:recipe_id>/like/', like_recipe, name='like_recipe'),  # Like recipe URL
    path('recipe/<int:recipe_id>/comment/', add_comment, name='add_comment'),  # Add comment URL
    path('recipe/<int:recipe_id>/save/', save_to_cookbook, name='save_to_cookbook'),  # Save recipe to cookbook URL
    path('recipe/<int:recipe_id>/unsave/', unsave_from_cookbook, name='unsave_from_cookbook'),  # Unsave recipe from cookbook URL
    path('recipes/', recipe_list, name='recipe_list'),  # Recipe list URL
    path('', home_view, name='home'),  # Home URL
    path('create/', create_recipe, name='create'),  # Create recipe URL
]
