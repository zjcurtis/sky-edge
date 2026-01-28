import logging
from enum import StrEnum
from typing import Generic, List, Optional, Type, TypeVar

from pydantic import BaseModel
from requests import Response, Session

from .auth import BB_API_SUBSCRIPTION_KEY, get_auth_token

_session = Session()

T = TypeVar("T", bound=BaseModel | str | None)

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename="warn.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s:%(message)s",
)


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


class ContentType(StrEnum):
    TEXT = "text/plain"
    PDF = "application/pdf"
    JSON = "application/json"


class Collection(BaseModel, Generic[T]):
    count: int
    next_link: Optional[str] = None
    value: List[T]

    def fetch_next(self) -> Optional["Collection[T]"] | Response:
        if not self.next_link:
            return None
        else:
            return api_request(
                method=HttpMethods.GET,
                url=self.next_link,
                response_model=Collection[T],
            )


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


def generic_request(
    method: HttpMethods,
    url: str,
    json=None,
    drop_headers: bool = False,
    **kwargs,
) -> Response:
    # Handle headers parameter - can be dict or list of Header objects
    incoming_headers = kwargs.pop("headers", None)

    # Start with default headers
    headers = {
        "authorization": f"Bearer {get_auth_token().access_token}",
        "Bb-Api-Subscription-Key": BB_API_SUBSCRIPTION_KEY,
        "Content-Type": "application/json",
    }
    # If we're asked to drop headers, we'll do it
    if drop_headers:
        headers = dict()
    # Merge incoming headers if provided
    if incoming_headers is not None:
        if drop_headers:
            headers = dict()
        if isinstance(incoming_headers, list):
            # Convert list of Header objects to dict
            for header in incoming_headers:
                if hasattr(header, "name") and hasattr(header, "value"):
                    if header.name and header.value:
                        headers[header.name] = header.value
        elif isinstance(incoming_headers, dict):
            # Merge dict headers
            headers.update(incoming_headers)
    reify = None
    if json is None:
        reify = lambda x: _session.request(
            method=method, url=url, headers=x, **kwargs
        )
    else:
        reify = lambda x: _session.request(
            method=method, url=url, headers=x, json=json, **kwargs
        )
    response = reify(x=headers)
    if 500 > response.status_code > 399:
        logger.info(msg=f"{response.headers} {response.reason} {response.text}")
    if response.status_code == 403:
        headers["authorization"] = f"Bearer {get_auth_token().access_token}"
        return reify(x=headers)
    else:
        return response


def api_request(
    method: HttpMethods,
    url: str,
    response_model: Type[T] | None = None,
    **kwargs,
) -> T | Response:
    response = generic_request(method=method, url=url, **kwargs)
    if str(response.status_code)[0] == "4":
        return response
    elif response.status_code and response_model:
        assert issubclass(response_model, BaseModel)
        return response_model.model_validate_json(json_data=response.text)

    return response
