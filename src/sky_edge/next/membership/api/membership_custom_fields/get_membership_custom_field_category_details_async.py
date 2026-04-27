from http import HTTPStatus
from typing import Any, cast

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import Response

from ...models.custom_field_category_details_collection import (
    CustomFieldCategoryDetailsCollection,
)


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/memberships/customfields/categories/details",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CustomFieldCategoryDetailsCollection | None:
    if response.status_code == 200:
        response_200 = CustomFieldCategoryDetailsCollection.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CustomFieldCategoryDetailsCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | CustomFieldCategoryDetailsCollection]:
    """Get membership custom field category details (PREVIEW)

     Returns list of membership custom field category details.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CustomFieldCategoryDetailsCollection]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Any | CustomFieldCategoryDetailsCollection | None:
    """Get membership custom field category details (PREVIEW)

     Returns list of membership custom field category details.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CustomFieldCategoryDetailsCollection
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | CustomFieldCategoryDetailsCollection]:
    """Get membership custom field category details (PREVIEW)

     Returns list of membership custom field category details.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CustomFieldCategoryDetailsCollection]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Any | CustomFieldCategoryDetailsCollection | None:
    """Get membership custom field category details (PREVIEW)

     Returns list of membership custom field category details.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CustomFieldCategoryDetailsCollection
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
