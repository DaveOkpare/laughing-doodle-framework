from typing import Dict, Callable, Any

from webob import Request, Response
from parse import parse


class API:
    def __init__(self):
        self.routes = {}

    def __call__(self, environ: Dict, start_response: Callable[..., Any]):
        """
        Overrides the class callable method and takes two parameters to return a WSGI-compatible response.
        """
        request = Request(environ)
        response = self.handle_request(request)

        return response(environ, start_response)

    def handle_request(self, request):
        """
        This method handles the response of a given request.
        """
        response = Response()

        handler, kwargs = self.find_handler(request_path=request.path)

        if handler is not None:
            handler(request, response, **kwargs)
        else:
            self.default_response(response)

        return response

    def find_handler(self, request_path):
        """
        This method maps the requested path to the handler function.
        """
        for path, handler in self.routes.items():
            parsed_path = parse(path, request_path)
            if parsed_path is not None:
                return handler, parsed_path.named

        return None, None

    @staticmethod
    def default_response(response):
        """
        This method provides a default text and status_code for unknown paths.
        """
        response.text = "Not Found"
        response.status_code = 404

    def route(self, path):
        """
        A decorator that wraps a function to map a path name and method with wrapped function.
        """
        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper
