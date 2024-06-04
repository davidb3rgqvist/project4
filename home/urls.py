from django.urls import path
from .views import home_view


# URL patterns for the home app
urlpatterns = [
    path('', home_view, name='home_view'),
]
