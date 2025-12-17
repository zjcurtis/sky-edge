from enum import StrEnum
from typing import Type, TypeVar

from pydantic import BaseModel
from requests import Response, Session
from time import sleep

from .auth import BB_API_SUBSCRIPTION_KEY, get_auth_token

_session = Session()

T = TypeVar("T", bound=BaseModel | None)


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


def reify_no_json(
    method: HttpMethods, url: str, headers: dict[str, str], **kwargs
) -> Response:
    return _session.request(method=method, url=url, headers=headers, **kwargs)


def reify_with_json(
    method: HttpMethods, url: str, headers: dict[str, str], json: str, **kwargs
) -> Response:
    return _session.request(
        method=method, url=url, headers=headers, json=json, **kwargs
    )


def generic_request(method: HttpMethods, url: str, json=None, **kwargs) -> Response:
    assert BB_API_SUBSCRIPTION_KEY
    headers: dict[str, str] = {
        "authorization": f"Bearer {get_auth_token().access_token}",
        "Bb-Api-Subscription-Key": BB_API_SUBSCRIPTION_KEY,
        "Content-Type": "application/json",
    }
    match json:
        case None:
            response = reify_no_json(method=method, url=url, headers=headers, **kwargs)
        case _:
            response = reify_with_json(
                method=method, url=url, headers=headers, json=json, **kwargs
            )
    match response.status_code:
        case 403:
            headers["authorization"] = f"Bearer {get_auth_token().access_token}"
            if json is None:
                return reify_no_json(method=method, url=url, headers=headers, **kwargs)
            else:
                return reify_with_json(
                    method=method, url=url, headers=headers, json=json, **kwargs
                )
        case 429:
            sleep_amount = float(response.headers["Retry-After"])
            sleep(sleep_amount)
            if json is None:
                return reify_no_json(method=method, url=url, headers=headers, **kwargs)
            else:
                return reify_with_json(
                    method=method, url=url, headers=headers, json=json, **kwargs
                )

        case _:
            return response


def api_request(
    method: HttpMethods, url: str, response_model: Type[T] | None = None, **kwargs
) -> T | Response:
    response = generic_request(method=method, url=url, **kwargs)
    if str(response.status_code)[0] == "4":
        return response
    elif response.status_code and response_model:
        assert issubclass(response_model, BaseModel)
        return response_model.model_validate_json(json_data=response.text)

    return response
