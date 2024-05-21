from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login')),
    path('register/', include('login.urls')),
    path('login/', include('login.urls')),
    path('logout/', include('login.urls')),
    path('home/', include('home.urls')), 
]
