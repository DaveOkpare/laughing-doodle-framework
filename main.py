class API:
    def __call__(self, environ, start_response):
        response_body = b"Hello World"
        status = "200"
        start_response(status, header=[])
        return iter([response_body])
