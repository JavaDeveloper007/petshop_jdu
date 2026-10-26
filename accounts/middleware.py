import time

class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response      # вызывается один раз при старте сервера

    def __call__(self, request):
        start = time.perf_counter()           # до view

        response = self.get_response(request) # передаём запрос дальше (view)

        duration = (time.perf_counter() - start) * 1000
        print(f"[{request.method}] {request.path} -> {response.status_code} | {duration:.2f} ms")

        return response                       # после view