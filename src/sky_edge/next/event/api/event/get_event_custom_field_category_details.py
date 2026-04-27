from http import HTTPStatus
from typing import Any

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import Response

from ...models.custom_field_category_details_collection import (
    CustomFieldCategoryDetailsCollection,
)
from ...models.service_error import ServiceError


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/events/customfields/categories/details",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CustomFieldCategoryDetailsCollection | list[ServiceError] | None:
    if response.status_code == 200:
        response_200 = CustomFieldCategoryDetailsCollection.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ServiceError.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400

    if response.status_code == 403:
        response_403 = []
        _response_403 = response.json()
        for response_403_item_data in _response_403:
            response_403_item = ServiceError.from_dict(response_403_item_data)

            response_403.append(response_403_item)

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CustomFieldCategoryDetailsCollection | list[ServiceError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[CustomFieldCategoryDetailsCollection | list[ServiceError]]:
    """Get event custom field category details (PREVIEW)

     Returns a list of event custom field category details.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldCategoryDetailsCollection | list[ServiceError]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> CustomFieldCategoryDetailsCollection | list[ServiceError] | None:
    """Get event custom field category details (PREVIEW)

     Returns a list of event custom field category details.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldCategoryDetailsCollection | list[ServiceError]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[CustomFieldCategoryDetailsCollection | list[ServiceError]]:
    """Get event custom field category details (PREVIEW)

     Returns a list of event custom field category details.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldCategoryDetailsCollection | list[ServiceError]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> CustomFieldCategoryDetailsCollection | list[ServiceError] | None:
    """Get event custom field category details (PREVIEW)

     Returns a list of event custom field category details.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldCategoryDetailsCollection | list[ServiceError]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
