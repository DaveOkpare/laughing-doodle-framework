from typing import Dict, Callable, Any


class API:
    def __call__(self, environ: Dict, start_response: Callable[..., Any]):
        response_body = b"Hello World"
        status = "200"
        start_response(status, header=[])
        return iter([response_body])


app = API()
