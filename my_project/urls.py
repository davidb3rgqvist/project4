"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hello_world import views as index_views
from about import views as about_views
from create import views as create_views
from recipe import views as recipe_views
from find import views as find_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', create_views.create_recipe, name='create'),
    path('about/', about_views.about_me, name='about'),
    path('recipe/', recipe_views.recipe_view, name='recipe'),
    path('find/', find_views.find_recipe, name='find'),
    path('', index_views.index, name='index'),
]
