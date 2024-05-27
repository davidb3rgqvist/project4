from django.urls import path
from . import login_view, register_view, logout_view, home_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home_view, name='home_view'),
]


# from django.urls import path
# from .views import login_view, register_view, logout_view

# urlpatterns = [
#     path('login/', login_view, name='login_view'),
#     path('register/', register_view, name='register_view'),
#     path('logout/', logout_view, name='logout_view'),
# ]