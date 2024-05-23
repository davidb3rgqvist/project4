from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from login.views import register_view
from create.views import create_view
from home.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', register_view, name='register'),
    path('logout/', LogoutView.as_view(template_name='logout/logout.html'), name='logout'),
    path('create/', create_view, name='create'),
    path('recipe/', include('recipe.urls')),
]
