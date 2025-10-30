from enum import StrEnum

from requests import Response, request
from pydantic import BaseModel

from .auth import BB_API_SUBSCRIPTION_KEY, AppTokens


class HttpMethods(StrEnum):
    GET = "GET"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


class FuzzyDate(BaseModel):
    # for API compatibility the single letter attributes are used for day, month, year
    d: int | None = None
    m: int | None = None
    y: int | None = None


def generic_request(
    method: HttpMethods, url: str, apptokens: AppTokens, json = None, **kwargs
) -> Response:
    headers = {
        "authorization": f"Bearer {apptokens.access_token}",
        "Bb-Api-Subscription-Key": BB_API_SUBSCRIPTION_KEY,
        "Content-Type": "application/json",
    }
    if json == None:
        return request(method=method, url=url, headers=headers, **kwargs)
    else:
        return request(method=method, url=url, headers=headers,json=json,**kwargs)
