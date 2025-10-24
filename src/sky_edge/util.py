from enum import StrEnum

from requests import Response, request

from .auth import BB_API_SUBSCRIPTION_KEY, AppTokens


class HttpMethods(StrEnum):
    GET = "GET"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


def generic_request(
    method: HttpMethods, url: str, apptokens: AppTokens, **kwargs
) -> Response:
    headers = {
        "authorization": f"Bearer {apptokens.access_token}",
        "Bb-Api-Subscription-Key": BB_API_SUBSCRIPTION_KEY,
        "Content-Type": "application/json",
    }
    return request(method=method, url=url, headers=headers, **kwargs)
