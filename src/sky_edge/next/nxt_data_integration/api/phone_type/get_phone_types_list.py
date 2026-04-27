from http import HTTPStatus
from typing import Any, cast

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.get_phone_types_list_phone_format import GetPhoneTypesListPhoneFormat
from ...models.get_phone_types_list_phone_number_type import (
    GetPhoneTypesListPhoneNumberType,
)
from ...models.phone_type_collection import PhoneTypeCollection


def _get_kwargs(
    *,
    description: str | Unset = UNSET,
    type_: GetPhoneTypesListPhoneNumberType | Unset = UNSET,
    format_: GetPhoneTypesListPhoneFormat | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["description"] = description

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params["include_inactive"] = include_inactive

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/re/phonetypes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PhoneTypeCollection | None:
    if response.status_code == 200:
        response_200 = PhoneTypeCollection.from_dict(response.json())

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
) -> Response[Any | PhoneTypeCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    description: str | Unset = UNSET,
    type_: GetPhoneTypesListPhoneNumberType | Unset = UNSET,
    format_: GetPhoneTypesListPhoneFormat | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | PhoneTypeCollection]:
    """Get phone types list

     Returns a list of phone types.

    Args:
        description (str | Unset):
        type_ (GetPhoneTypesListPhoneNumberType | Unset):
        format_ (GetPhoneTypesListPhoneFormat | Unset):
        include_inactive (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PhoneTypeCollection]
    """

    kwargs = _get_kwargs(
        description=description,
        type_=type_,
        format_=format_,
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
    description: str | Unset = UNSET,
    type_: GetPhoneTypesListPhoneNumberType | Unset = UNSET,
    format_: GetPhoneTypesListPhoneFormat | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | PhoneTypeCollection | None:
    """Get phone types list

     Returns a list of phone types.

    Args:
        description (str | Unset):
        type_ (GetPhoneTypesListPhoneNumberType | Unset):
        format_ (GetPhoneTypesListPhoneFormat | Unset):
        include_inactive (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PhoneTypeCollection
    """

    return sync_detailed(
        client=client,
        description=description,
        type_=type_,
        format_=format_,
        include_inactive=include_inactive,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    description: str | Unset = UNSET,
    type_: GetPhoneTypesListPhoneNumberType | Unset = UNSET,
    format_: GetPhoneTypesListPhoneFormat | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | PhoneTypeCollection]:
    """Get phone types list

     Returns a list of phone types.

    Args:
        description (str | Unset):
        type_ (GetPhoneTypesListPhoneNumberType | Unset):
        format_ (GetPhoneTypesListPhoneFormat | Unset):
        include_inactive (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PhoneTypeCollection]
    """

    kwargs = _get_kwargs(
        description=description,
        type_=type_,
        format_=format_,
        include_inactive=include_inactive,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    description: str | Unset = UNSET,
    type_: GetPhoneTypesListPhoneNumberType | Unset = UNSET,
    format_: GetPhoneTypesListPhoneFormat | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | PhoneTypeCollection | None:
    """Get phone types list

     Returns a list of phone types.

    Args:
        description (str | Unset):
        type_ (GetPhoneTypesListPhoneNumberType | Unset):
        format_ (GetPhoneTypesListPhoneFormat | Unset):
        include_inactive (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PhoneTypeCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            description=description,
            type_=type_,
            format_=format_,
            include_inactive=include_inactive,
            limit=limit,
            offset=offset,
        )
    ).parsed
