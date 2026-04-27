from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_field_category_collection import CustomFieldCategoryCollection
from ...models.get_custom_field_category_list_custom_field_category_record_type import (
    GetCustomFieldCategoryListCustomFieldCategoryRecordType,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    record_type: GetCustomFieldCategoryListCustomFieldCategoryRecordType | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_record_type: str | Unset = UNSET
    if not isinstance(record_type, Unset):
        json_record_type = record_type.value

    params["record_type"] = json_record_type

    params["include_inactive"] = include_inactive

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/re/customfieldcategories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CustomFieldCategoryCollection | None:
    if response.status_code == 200:
        response_200 = CustomFieldCategoryCollection.from_dict(response.json())

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
) -> Response[Any | CustomFieldCategoryCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    record_type: GetCustomFieldCategoryListCustomFieldCategoryRecordType | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | CustomFieldCategoryCollection]:
    """Get custom field category list

     Returns a list of custom field categories.

    Args:
        record_type (GetCustomFieldCategoryListCustomFieldCategoryRecordType | Unset):
        include_inactive (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CustomFieldCategoryCollection]
    """

    kwargs = _get_kwargs(
        record_type=record_type,
        include_inactive=include_inactive,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    record_type: GetCustomFieldCategoryListCustomFieldCategoryRecordType | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | CustomFieldCategoryCollection | None:
    """Get custom field category list

     Returns a list of custom field categories.

    Args:
        record_type (GetCustomFieldCategoryListCustomFieldCategoryRecordType | Unset):
        include_inactive (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CustomFieldCategoryCollection
    """

    return sync_detailed(
        client=client,
        record_type=record_type,
        include_inactive=include_inactive,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    record_type: GetCustomFieldCategoryListCustomFieldCategoryRecordType | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | CustomFieldCategoryCollection]:
    """Get custom field category list

     Returns a list of custom field categories.

    Args:
        record_type (GetCustomFieldCategoryListCustomFieldCategoryRecordType | Unset):
        include_inactive (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CustomFieldCategoryCollection]
    """

    kwargs = _get_kwargs(
        record_type=record_type,
        include_inactive=include_inactive,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    record_type: GetCustomFieldCategoryListCustomFieldCategoryRecordType | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | CustomFieldCategoryCollection | None:
    """Get custom field category list

     Returns a list of custom field categories.

    Args:
        record_type (GetCustomFieldCategoryListCustomFieldCategoryRecordType | Unset):
        include_inactive (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CustomFieldCategoryCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            record_type=record_type,
            include_inactive=include_inactive,
            limit=limit,
            offset=offset,
        )
    ).parsed
