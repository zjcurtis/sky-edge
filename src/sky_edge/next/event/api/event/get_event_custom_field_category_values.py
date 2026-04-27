from http import HTTPStatus
from typing import Any

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.custom_field_category_values_collection import (
    CustomFieldCategoryValuesCollection,
)
from ...models.service_error import ServiceError


def _get_kwargs(
    *,
    category_name: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["category_name"] = category_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/events/customfields/categories/values",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CustomFieldCategoryValuesCollection | list[ServiceError] | None:
    if response.status_code == 200:
        response_200 = CustomFieldCategoryValuesCollection.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = []
        _response_404 = response.json()
        for response_404_item_data in _response_404:
            response_404_item = ServiceError.from_dict(response_404_item_data)

            response_404.append(response_404_item)

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CustomFieldCategoryValuesCollection | list[ServiceError]]:
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
) -> Response[CustomFieldCategoryValuesCollection | list[ServiceError]]:
    """Returns event custom field category values (PREVIEW)

     Returns event custom field category values.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        category_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldCategoryValuesCollection | list[ServiceError]]
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
) -> CustomFieldCategoryValuesCollection | list[ServiceError] | None:
    """Returns event custom field category values (PREVIEW)

     Returns event custom field category values.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        category_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldCategoryValuesCollection | list[ServiceError]
    """

    return sync_detailed(
        client=client,
        category_name=category_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    category_name: str | Unset = UNSET,
) -> Response[CustomFieldCategoryValuesCollection | list[ServiceError]]:
    """Returns event custom field category values (PREVIEW)

     Returns event custom field category values.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        category_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldCategoryValuesCollection | list[ServiceError]]
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
) -> CustomFieldCategoryValuesCollection | list[ServiceError] | None:
    """Returns event custom field category values (PREVIEW)

     Returns event custom field category values.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        category_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldCategoryValuesCollection | list[ServiceError]
    """

    return (
        await asyncio_detailed(
            client=client,
            category_name=category_name,
        )
    ).parsed
