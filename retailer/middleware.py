from .models import Logs


class LogMiddleware(object):
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith('/admin/'):
            Logs.objects.create(path=request.path, method=request.method)
        return self.get_response(request)
