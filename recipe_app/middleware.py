from django.urls import reverse
from django.shortcuts import redirect

# List of paths that do not require authentication
EXCLUDED_PATHS = [
    reverse('admin:index'),
    reverse('admin:login'),
    reverse('login'),
    reverse('register'),
]

class LoginRequiredMiddleware:
    """
    Middleware to redirect unauthenticated users to the login page.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in EXCLUDED_PATHS:
            return redirect('login')
        return self.get_response(request)