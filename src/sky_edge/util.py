from enum import StrEnum

from pydantic import BaseModel
from requests import Response, request

from .auth import BB_API_SUBSCRIPTION_KEY, AppTokens, request_token


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
    method: HttpMethods, url: str, apptokens: AppTokens, json=None, **kwargs
) -> Response:
    headers = {
        "authorization": f"Bearer {apptokens.access_token}",
        "Bb-Api-Subscription-Key": BB_API_SUBSCRIPTION_KEY,
        "Content-Type": "application/json",
    }
    reify = None
    if json == None:
        reify = lambda x: request(method=method, url=url, headers=x, **kwargs)
    else:
        reify = lambda x: request(
            method=method, url=url, headers=x, json=json, **kwargs
        )
    response = reify(x=headers)
    if response.status_code == 403:
        fresh_tokens = request_token(input=apptokens)
        headers["authorization"] = f"Bearer {fresh_tokens.access_token}"
        return reify(x=headers)
    else:
        return response
