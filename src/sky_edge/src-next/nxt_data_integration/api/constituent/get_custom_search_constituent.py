from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.constituent_collection import ConstituentCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    first_name: str | Unset = UNSET,
    last_name: str | Unset = UNSET,
    alias_type: str | Unset = UNSET,
    lookup_id: str | Unset = UNSET,
    address_lines: str | Unset = UNSET,
    city: str | Unset = UNSET,
    state: str | Unset = UNSET,
    post_code: str | Unset = UNSET,
    email: str | Unset = UNSET,
    phone_number: str | Unset = UNSET,
    include_maiden_name: bool | Unset = UNSET,
    include_alias: bool | Unset = UNSET,
    record_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["first_name"] = first_name

    params["last_name"] = last_name

    params["alias_type"] = alias_type

    params["lookup_id"] = lookup_id

    params["address_lines"] = address_lines

    params["city"] = city

    params["state"] = state

    params["post_code"] = post_code

    params["email"] = email

    params["phone_number"] = phone_number

    params["include_maiden_name"] = include_maiden_name

    params["include_alias"] = include_alias

    json_record_ids: list[str] | Unset = UNSET
    if not isinstance(record_ids, Unset):
        json_record_ids = record_ids

    params["record_ids"] = json_record_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/re/constituents/customsearch",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ConstituentCollection | None:
    if response.status_code == 200:
        response_200 = ConstituentCollection.from_dict(response.json())

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
) -> Response[Any | ConstituentCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    first_name: str | Unset = UNSET,
    last_name: str | Unset = UNSET,
    alias_type: str | Unset = UNSET,
    lookup_id: str | Unset = UNSET,
    address_lines: str | Unset = UNSET,
    city: str | Unset = UNSET,
    state: str | Unset = UNSET,
    post_code: str | Unset = UNSET,
    email: str | Unset = UNSET,
    phone_number: str | Unset = UNSET,
    include_maiden_name: bool | Unset = UNSET,
    include_alias: bool | Unset = UNSET,
    record_ids: list[str] | Unset = UNSET,
) -> Response[Any | ConstituentCollection]:
    """Get constituent list (search)

     Searches for constituent records using the given filter criteria.

    Args:
        limit (int | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        alias_type (str | Unset):
        lookup_id (str | Unset):
        address_lines (str | Unset):
        city (str | Unset):
        state (str | Unset):
        post_code (str | Unset):
        email (str | Unset):
        phone_number (str | Unset):
        include_maiden_name (bool | Unset):
        include_alias (bool | Unset):
        record_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConstituentCollection]
    """

    kwargs = _get_kwargs(
        limit=limit,
        first_name=first_name,
        last_name=last_name,
        alias_type=alias_type,
        lookup_id=lookup_id,
        address_lines=address_lines,
        city=city,
        state=state,
        post_code=post_code,
        email=email,
        phone_number=phone_number,
        include_maiden_name=include_maiden_name,
        include_alias=include_alias,
        record_ids=record_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    first_name: str | Unset = UNSET,
    last_name: str | Unset = UNSET,
    alias_type: str | Unset = UNSET,
    lookup_id: str | Unset = UNSET,
    address_lines: str | Unset = UNSET,
    city: str | Unset = UNSET,
    state: str | Unset = UNSET,
    post_code: str | Unset = UNSET,
    email: str | Unset = UNSET,
    phone_number: str | Unset = UNSET,
    include_maiden_name: bool | Unset = UNSET,
    include_alias: bool | Unset = UNSET,
    record_ids: list[str] | Unset = UNSET,
) -> Any | ConstituentCollection | None:
    """Get constituent list (search)

     Searches for constituent records using the given filter criteria.

    Args:
        limit (int | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        alias_type (str | Unset):
        lookup_id (str | Unset):
        address_lines (str | Unset):
        city (str | Unset):
        state (str | Unset):
        post_code (str | Unset):
        email (str | Unset):
        phone_number (str | Unset):
        include_maiden_name (bool | Unset):
        include_alias (bool | Unset):
        record_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConstituentCollection
    """

    return sync_detailed(
        client=client,
        limit=limit,
        first_name=first_name,
        last_name=last_name,
        alias_type=alias_type,
        lookup_id=lookup_id,
        address_lines=address_lines,
        city=city,
        state=state,
        post_code=post_code,
        email=email,
        phone_number=phone_number,
        include_maiden_name=include_maiden_name,
        include_alias=include_alias,
        record_ids=record_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    first_name: str | Unset = UNSET,
    last_name: str | Unset = UNSET,
    alias_type: str | Unset = UNSET,
    lookup_id: str | Unset = UNSET,
    address_lines: str | Unset = UNSET,
    city: str | Unset = UNSET,
    state: str | Unset = UNSET,
    post_code: str | Unset = UNSET,
    email: str | Unset = UNSET,
    phone_number: str | Unset = UNSET,
    include_maiden_name: bool | Unset = UNSET,
    include_alias: bool | Unset = UNSET,
    record_ids: list[str] | Unset = UNSET,
) -> Response[Any | ConstituentCollection]:
    """Get constituent list (search)

     Searches for constituent records using the given filter criteria.

    Args:
        limit (int | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        alias_type (str | Unset):
        lookup_id (str | Unset):
        address_lines (str | Unset):
        city (str | Unset):
        state (str | Unset):
        post_code (str | Unset):
        email (str | Unset):
        phone_number (str | Unset):
        include_maiden_name (bool | Unset):
        include_alias (bool | Unset):
        record_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConstituentCollection]
    """

    kwargs = _get_kwargs(
        limit=limit,
        first_name=first_name,
        last_name=last_name,
        alias_type=alias_type,
        lookup_id=lookup_id,
        address_lines=address_lines,
        city=city,
        state=state,
        post_code=post_code,
        email=email,
        phone_number=phone_number,
        include_maiden_name=include_maiden_name,
        include_alias=include_alias,
        record_ids=record_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    first_name: str | Unset = UNSET,
    last_name: str | Unset = UNSET,
    alias_type: str | Unset = UNSET,
    lookup_id: str | Unset = UNSET,
    address_lines: str | Unset = UNSET,
    city: str | Unset = UNSET,
    state: str | Unset = UNSET,
    post_code: str | Unset = UNSET,
    email: str | Unset = UNSET,
    phone_number: str | Unset = UNSET,
    include_maiden_name: bool | Unset = UNSET,
    include_alias: bool | Unset = UNSET,
    record_ids: list[str] | Unset = UNSET,
) -> Any | ConstituentCollection | None:
    """Get constituent list (search)

     Searches for constituent records using the given filter criteria.

    Args:
        limit (int | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        alias_type (str | Unset):
        lookup_id (str | Unset):
        address_lines (str | Unset):
        city (str | Unset):
        state (str | Unset):
        post_code (str | Unset):
        email (str | Unset):
        phone_number (str | Unset):
        include_maiden_name (bool | Unset):
        include_alias (bool | Unset):
        record_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConstituentCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            first_name=first_name,
            last_name=last_name,
            alias_type=alias_type,
            lookup_id=lookup_id,
            address_lines=address_lines,
            city=city,
            state=state,
            post_code=post_code,
            email=email,
            phone_number=phone_number,
            include_maiden_name=include_maiden_name,
            include_alias=include_alias,
            record_ids=record_ids,
        )
    ).parsed
