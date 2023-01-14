from typing import Dict, Callable, Any


class API:
    def __call__(self, environ: Dict, start_response: Callable[..., Any]):
        """
        A callable object that expects two parameters and returns a WSGI-compatible response.

        :param environ: Stores info about request e.g request_method, url, query_params, headers etc.
        :param start_response: Starts the response
        :return: Response body
        """
        response_body = b"Hello World"
        status = "200"
        start_response(status, header=[])
        return iter([response_body])


app = API()
