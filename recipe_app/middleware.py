from django.urls import reverse
from django.shortcuts import redirect

EXCLUDED_PATHS = [
    reverse('admin:index'),
    reverse('admin:login'),
    reverse('login'),
    reverse('register'),
]

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in EXCLUDED_PATHS:
            return redirect('login')
        return self.get_response(request)