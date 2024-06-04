from django.urls import path
from django.contrib.auth.views import LoginView as LV, LogoutView as LOV
from .views import register_view, auth_view

urlpatterns = [
    # URLs for auth-related views
    path(
        'login/',
        LV.as_view(template_name='registration/login.html'),
        name='login'
    ),
    path(
        'login/register/',
        register_view,
        name='register'
    ),
    path(
        'logout/',
        LOV.as_view(template_name='logout/logout.html'),
        name='logout'
    ),
    path(
        'auth/',
        auth_view,
        name='auth'
    ),
]
