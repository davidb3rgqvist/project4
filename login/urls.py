from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, auth_view

urlpatterns = [
    # URLs for auth-related views
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('login/register/', register_view, name='register'),
    path('logout/', LogoutView.as_view(template_name='logout/logout.html'), name='logout'),
    path('auth/', auth_view, name='auth'),
]

