import requests
from requests import Response

from Lab7.http_exception import HttpException
from Lab7.http_method_type import HttpMethod


class HttpClient:

    def __init__(self, base_url: str):
        self.__base_url = base_url

    def get(self, url_params: str = None) -> Response:
        return self.__send_request(method_type=HttpMethod.GET, url_params=url_params)

    def post(self, url_params: str = None, data=None) -> Response:
        return self.__send_request(method_type=HttpMethod.POST, url_params=url_params, data=data)

    def put(self, url_params: str = None, data=None) -> Response:
        return self.__send_request(method_type=HttpMethod.PUT, url_params=url_params, data=data)

    def patch(self, url_params: str = None, data=None) -> Response:
        return self.__send_request(method_type=HttpMethod.PATCH, url_params=url_params, data=data)

    def delete(self, url_params: str = None, data=None) -> Response:
        return self.__send_request(method_type=HttpMethod.DELETE, url_params=url_params, data=data)

    def __send_request(self, method_type: HttpMethod, url_params: str = None, data=None) -> Response:
        request_url = self.__base_url + (url_params or "")

        request_methods = {
            HttpMethod.GET: requests.get,
            HttpMethod.POST: requests.post,
            HttpMethod.PUT: requests.put,
            HttpMethod.PATCH: requests.patch,
            HttpMethod.DELETE: requests.delete,
        }

        if method_type not in request_methods:
            raise ValueError(f"Invalid HttpMethod: {method_type}")

        request_method = request_methods[method_type]
        response = request_method(request_url, data=data)
        if response.ok:
            return response.json()
        raise HttpException(f"Failed to make HTTP request\nHTTP method: {method_type}, Url parameters:{url_params}")