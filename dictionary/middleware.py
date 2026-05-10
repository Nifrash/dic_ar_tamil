from django.http import JsonResponse
from django.shortcuts import render

class BlockInvalidURLsMiddleware:

    ALLOWED_PREFIXES = [
        '/api/',
        '/admin/',
        '/static/',
        '/media/',
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        path = request.path

        if not any(path.startswith(prefix) for prefix in self.ALLOWED_PREFIXES):

            # API requests -> JSON
            if path.startswith('/api/'):
                return render(request, '403.html', status=403)

            # Website requests -> HTML
            return render(request, '403.html', status=403)

        response = self.get_response(request)
        return response