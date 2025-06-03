from django.conf import settings
from django.shortcuts import redirect
from django.urls import resolve

EXEMPT_URLS = [
    'users:login',
    'users:logout',
    'users:sign-up',
    'admin:login',
    'admin:logout',
    'admin:register',
    'core:welcome'
]

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        resolver_match = resolve(request.path)
        view_name = resolver_match.view_name

        if view_name in EXEMPT_URLS:
            return self.get_response(request)

        if not request.user.is_authenticated:
            return redirect(f'{settings.LOGIN_URL}?next={request.path}')

        return self.get_response(request)


class RoleAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            resolver_match = resolve(request.path)
            view_name = resolver_match.view_name

            user_role = request.user.groups.all()[0].name

            if user_role == 'admin':
                return self.get_response(request)
            elif view_name == 'users:user-list' and user_role != 'admin':
                return redirect('core:products')
            elif user_role == 'guest':
                if view_name == 'core:about' or view_name in EXEMPT_URLS:
                    return self.get_response(request)
                return redirect('core:welcome')

        return self.get_response(request)
