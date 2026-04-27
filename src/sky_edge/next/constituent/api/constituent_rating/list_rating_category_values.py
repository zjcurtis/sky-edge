from http import HTTPStatus
from typing import Any, cast

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.api_collection_of_string import ApiCollectionOfString


def _get_kwargs(
    *,
    category_name: str | Unset = UNSET,
    source_name: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["category_name"] = category_name

    params["source_name"] = source_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ratings/categories/values",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiCollectionOfString | None:
    if response.status_code == 200:
        response_200 = ApiCollectionOfString.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ApiCollectionOfString]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    category_name: str | Unset = UNSET,
    source_name: str | Unset = UNSET,
) -> Response[Any | ApiCollectionOfString]:
    """Rating category values

     Returns a list of rating values for code table categories.

    Args:
        category_name (str | Unset):
        source_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOfString]
    """

    kwargs = _get_kwargs(
        category_name=category_name,
        source_name=source_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    category_name: str | Unset = UNSET,
    source_name: str | Unset = UNSET,
) -> Any | ApiCollectionOfString | None:
    """Rating category values

     Returns a list of rating values for code table categories.

    Args:
        category_name (str | Unset):
        source_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOfString
    """

    return sync_detailed(
        client=client,
        category_name=category_name,
        source_name=source_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    category_name: str | Unset = UNSET,
    source_name: str | Unset = UNSET,
) -> Response[Any | ApiCollectionOfString]:
    """Rating category values

     Returns a list of rating values for code table categories.

    Args:
        category_name (str | Unset):
        source_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOfString]
    """

    kwargs = _get_kwargs(
        category_name=category_name,
        source_name=source_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    category_name: str | Unset = UNSET,
    source_name: str | Unset = UNSET,
) -> Any | ApiCollectionOfString | None:
    """Rating category values

     Returns a list of rating values for code table categories.

    Args:
        category_name (str | Unset):
        source_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOfString
    """

    return (
        await asyncio_detailed(
            client=client,
            category_name=category_name,
            source_name=source_name,
        )
    ).parsed
