from django.utils import timezone
from django.conf import settings


class PersistentLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            request.session.set_expiry(settings.SESSION_COOKIE_AGE)
        return self.get_response(request)