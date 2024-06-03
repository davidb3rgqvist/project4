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
        # Check if the user is unauthenticated and the requested path is not excluded
        if not request.user.is_authenticated and not self._is_excluded_path(request.path):
            return redirect('login')
        return self.get_response(request)

    def _is_excluded_path(self, path):
        """
        Check if the given path is in the list of excluded paths.
        """
        return any(path.startswith(reverse(namespace + ':')) for namespace in EXCLUDED_NAMESPACES)