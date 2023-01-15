from typing import Dict, Callable, Any, List, Optional
from webob import Request, Response


class API:
    def __init__(self):
        self.routes = {}

    def __call__(self, environ: Dict, start_response: Callable[..., Any]):
        """
        A callable object that expects two parameters and returns a WSGI-compatible response.

        :param environ: stores info about request e.g request_method, url, query_params, headers etc.
        :param start_response: starts the response
        :return: response
        """
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def route(self, path: str):
        """
        A decorator that wraps a function to map a path name and method with wrapped function.
        :param path: url path passed as argument in decorator
        :return:
        """

        def wrapper(handler):
            if path not in self.routes:
                self.routes[path] = handler
            return handler

        return wrapper

    def find_handler(self, request_path):
        for path, handler in self.routes.items():
            if path == request_path:
                return handler

    @staticmethod
    def default_response(response):
        response.status_code = 404
        response.text = "Not Found."

    def handle_request(self, request):
        response = Response()

        handler = self.find_handler(request_path=request.path)

        if handler is not None:
            handler(request, response)
        else:
            self.default_response(response)

        return response


app = API()


@app.route("/home")
def home(request, response):
    response.text = "I'm Home"


@app.route("/about")
def home(request, response):
    response.text = "I'm moving about in this space."
