from django.shortcuts import redirect


def redirect_authenticated_user(view_func):
    """
    Decorator for views that redirects authenticated users to the 'home' page.
    """
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper
