from pprint import pprint

from django.core.exceptions import PermissionDenied
import time


class FilterIPMiddleware:

    def __init__(self, get_request):
        self.get_request = get_request
        self._count_request = 0

    def __call__(self, response):
        answer_ips = ['127.0.0.1']
        ip = response.META.get("REMOTE_ADDR")

        print('*' * 50, response.META)

        if ip not in answer_ips:
            raise PermissionDenied

        request = self.get_request(response)
        print('*' * 50, request.status_code)
        return request


class FilterIPMiddlewareCount:

    def __init__(self, get_request):
        self.get_request = get_request
        self._count_request = 0

    def __call__(self, response):

        answer_ips = ['127.0.0.1']
        ip = response.META.get("REMOTE_ADDR")

        if ip not in answer_ips:
            raise PermissionDenied
        else:
            self._count_request += 1
            request = self.get_request(response)

            if self._count_request % 3 == 0:
                time.sleep(3)
                return request
            else:
                return request


class FilterIPMiddlewareCountTime:

    def __init__(self, get_request):
        self.get_request = get_request
        self._count_request = 3
        self._total = 0
        self.dict_session = {}
        self._time_request = time.time()

    def __call__(self, response):

        answer_ips = ['127.0.0.1']
        ip = response.META.get("REMOTE_ADDR")
        if 'pause' not in response.session:
            response.session.set_expiry(1)
            response.session['pause'] = True
        else:
            raise PermissionDenied

        if ip not in answer_ips:
            raise PermissionDenied

        request = self.get_request(response)
        return request
