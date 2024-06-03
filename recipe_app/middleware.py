from django.urls import reverse, NoReverseMatch
from django.shortcuts import redirect
import logging

logger = logging.getLogger(__name__)

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        try:
            self.excluded_paths = [
                reverse('admin:index'),
                reverse('admin:login'),
                reverse('login'),
                reverse('register'),
            ]
            logger.debug(f"Excluded paths: {self.excluded_paths}")
        except NoReverseMatch as e:
            logger.error(f"Error resolving URL names: {e}")
            self.excluded_paths = []

    def __call__(self, request):
        if not request.user.is_authenticated and not self._is_excluded_path(request.path):
            logger.debug(f"Unauthenticated access attempt to {request.path}. Redirecting to login.")
            return redirect('login')
        return self.get_response(request)

    def _is_excluded_path(self, path):
        logger.debug(f"Checking if path {path} is excluded.")
        return any(path == excluded_path for excluded_path in self.excluded_paths)