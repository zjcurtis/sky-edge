from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rating_edit import RatingEdit
from ...types import UNSET, Response, Unset


def _get_kwargs(
    rating_id: str,
    *,
    body: RatingEdit | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/ratings/{rating_id}".format(
            rating_id=quote(str(rating_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 404:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rating_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RatingEdit | Unset = UNSET,
) -> Response[Any]:
    """Rating (Edit)

     Edits a constituent rating.

    Args:
        rating_id (str):
        body (RatingEdit | Unset): Ratings indicate the estimated wealth of constituents and their
            capacity to give. Ratings information such as overall wealth ratings, suggested ask
            amounts, and total identified assets can help to determine where to focus efforts, whether
            to pursue prospects or major gifts, and how much to ask from donors.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        rating_id=rating_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    rating_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RatingEdit | Unset = UNSET,
) -> Response[Any]:
    """Rating (Edit)

     Edits a constituent rating.

    Args:
        rating_id (str):
        body (RatingEdit | Unset): Ratings indicate the estimated wealth of constituents and their
            capacity to give. Ratings information such as overall wealth ratings, suggested ask
            amounts, and total identified assets can help to determine where to focus efforts, whether
            to pursue prospects or major gifts, and how much to ask from donors.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        rating_id=rating_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
