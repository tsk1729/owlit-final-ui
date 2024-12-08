import requests

from constants import RequestType


def make_request(method, url, payload=None, headers=None):
    default_headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    if headers:
        final_headers = {**default_headers, **headers}
    else:
        final_headers = default_headers

    if method.upper() == RequestType.GET:
        return requests.get(url, headers=final_headers)
    elif method.upper() == RequestType.POST:
        return requests.post(url, json=payload, headers=final_headers)
    elif method.upper() == RequestType.PUT:
        return requests.put(url, json=payload, headers=final_headers)
    elif method.upper() == RequestType.DELETE:
        return requests.delete(url, headers=final_headers)



