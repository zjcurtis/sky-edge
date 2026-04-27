from http import HTTPStatus
from typing import Any

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.api_collection_string import ApiCollectionString


def _get_kwargs(
    *,
    category_name: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["category_name"] = category_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/campaigns/customfields/categories/values",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiCollectionString | None:
    if response.status_code == 200:
        response_200 = ApiCollectionString.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiCollectionString]:
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
) -> Response[ApiCollectionString]:
    """Campaign custom field category values

     Gets the list of custom field category values.

    Args:
        category_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiCollectionString]
    """

    kwargs = _get_kwargs(
        category_name=category_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    category_name: str | Unset = UNSET,
) -> ApiCollectionString | None:
    """Campaign custom field category values

     Gets the list of custom field category values.

    Args:
        category_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiCollectionString
    """

    return sync_detailed(
        client=client,
        category_name=category_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    category_name: str | Unset = UNSET,
) -> Response[ApiCollectionString]:
    """Campaign custom field category values

     Gets the list of custom field category values.

    Args:
        category_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiCollectionString]
    """

    kwargs = _get_kwargs(
        category_name=category_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    category_name: str | Unset = UNSET,
) -> ApiCollectionString | None:
    """Campaign custom field category values

     Gets the list of custom field category values.

    Args:
        category_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiCollectionString
    """

    return (
        await asyncio_detailed(
            client=client,
            category_name=category_name,
        )
    ).parsed
