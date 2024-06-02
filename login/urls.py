from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view

urlpatterns = [
    # URLs for auth-related views
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', register_view, name='register'),
    path('logout/', LogoutView.as_view(template_name='logout/logout.html'), name='logout'),
]

