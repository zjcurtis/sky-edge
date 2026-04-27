from http import HTTPStatus
from typing import Any, cast

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.api_collection_of_duplicate_search_result_read import (
    ApiCollectionOfDuplicateSearchResultRead,
)


def _get_kwargs(
    *,
    last_org_name: str,
    search_individuals: bool | Unset = UNSET,
    search_aliases: bool | Unset = UNSET,
    search_contacts: bool | Unset = UNSET,
    first_name: str | Unset = UNSET,
    middle_name: str | Unset = UNSET,
    suffix: str | Unset = UNSET,
    address_block: str | Unset = UNSET,
    city: str | Unset = UNSET,
    state: str | Unset = UNSET,
    post_code: str | Unset = UNSET,
    email: list[str] | Unset = UNSET,
    phone: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["last_org_name"] = last_org_name

    params["search_individuals"] = search_individuals

    params["search_aliases"] = search_aliases

    params["search_contacts"] = search_contacts

    params["first_name"] = first_name

    params["middle_name"] = middle_name

    params["suffix"] = suffix

    params["address_block"] = address_block

    params["city"] = city

    params["state"] = state

    params["post_code"] = post_code

    json_email: list[str] | Unset = UNSET
    if not isinstance(email, Unset):
        json_email = email

    params["email"] = json_email

    json_phone: list[str] | Unset = UNSET
    if not isinstance(phone, Unset):
        json_phone = phone

    params["phone"] = json_phone

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/constituents/duplicatesearch",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiCollectionOfDuplicateSearchResultRead | None:
    if response.status_code == 200:
        response_200 = ApiCollectionOfDuplicateSearchResultRead.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ApiCollectionOfDuplicateSearchResultRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    last_org_name: str,
    search_individuals: bool | Unset = UNSET,
    search_aliases: bool | Unset = UNSET,
    search_contacts: bool | Unset = UNSET,
    first_name: str | Unset = UNSET,
    middle_name: str | Unset = UNSET,
    suffix: str | Unset = UNSET,
    address_block: str | Unset = UNSET,
    city: str | Unset = UNSET,
    state: str | Unset = UNSET,
    post_code: str | Unset = UNSET,
    email: list[str] | Unset = UNSET,
    phone: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | ApiCollectionOfDuplicateSearchResultRead]:
    """Constituent (Duplicate search)

     Returns possible duplicate records. Searches individual, organization, and related contact records
    and ranks results based on search filters. Records that match multiple filters rank higher as
    potential duplicates.

    Args:
        last_org_name (str):
        search_individuals (bool | Unset):
        search_aliases (bool | Unset):
        search_contacts (bool | Unset):
        first_name (str | Unset):
        middle_name (str | Unset):
        suffix (str | Unset):
        address_block (str | Unset):
        city (str | Unset):
        state (str | Unset):
        post_code (str | Unset):
        email (list[str] | Unset):
        phone (list[str] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOfDuplicateSearchResultRead]
    """

    kwargs = _get_kwargs(
        last_org_name=last_org_name,
        search_individuals=search_individuals,
        search_aliases=search_aliases,
        search_contacts=search_contacts,
        first_name=first_name,
        middle_name=middle_name,
        suffix=suffix,
        address_block=address_block,
        city=city,
        state=state,
        post_code=post_code,
        email=email,
        phone=phone,
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
    last_org_name: str,
    search_individuals: bool | Unset = UNSET,
    search_aliases: bool | Unset = UNSET,
    search_contacts: bool | Unset = UNSET,
    first_name: str | Unset = UNSET,
    middle_name: str | Unset = UNSET,
    suffix: str | Unset = UNSET,
    address_block: str | Unset = UNSET,
    city: str | Unset = UNSET,
    state: str | Unset = UNSET,
    post_code: str | Unset = UNSET,
    email: list[str] | Unset = UNSET,
    phone: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | ApiCollectionOfDuplicateSearchResultRead | None:
    """Constituent (Duplicate search)

     Returns possible duplicate records. Searches individual, organization, and related contact records
    and ranks results based on search filters. Records that match multiple filters rank higher as
    potential duplicates.

    Args:
        last_org_name (str):
        search_individuals (bool | Unset):
        search_aliases (bool | Unset):
        search_contacts (bool | Unset):
        first_name (str | Unset):
        middle_name (str | Unset):
        suffix (str | Unset):
        address_block (str | Unset):
        city (str | Unset):
        state (str | Unset):
        post_code (str | Unset):
        email (list[str] | Unset):
        phone (list[str] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOfDuplicateSearchResultRead
    """

    return sync_detailed(
        client=client,
        last_org_name=last_org_name,
        search_individuals=search_individuals,
        search_aliases=search_aliases,
        search_contacts=search_contacts,
        first_name=first_name,
        middle_name=middle_name,
        suffix=suffix,
        address_block=address_block,
        city=city,
        state=state,
        post_code=post_code,
        email=email,
        phone=phone,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    last_org_name: str,
    search_individuals: bool | Unset = UNSET,
    search_aliases: bool | Unset = UNSET,
    search_contacts: bool | Unset = UNSET,
    first_name: str | Unset = UNSET,
    middle_name: str | Unset = UNSET,
    suffix: str | Unset = UNSET,
    address_block: str | Unset = UNSET,
    city: str | Unset = UNSET,
    state: str | Unset = UNSET,
    post_code: str | Unset = UNSET,
    email: list[str] | Unset = UNSET,
    phone: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | ApiCollectionOfDuplicateSearchResultRead]:
    """Constituent (Duplicate search)

     Returns possible duplicate records. Searches individual, organization, and related contact records
    and ranks results based on search filters. Records that match multiple filters rank higher as
    potential duplicates.

    Args:
        last_org_name (str):
        search_individuals (bool | Unset):
        search_aliases (bool | Unset):
        search_contacts (bool | Unset):
        first_name (str | Unset):
        middle_name (str | Unset):
        suffix (str | Unset):
        address_block (str | Unset):
        city (str | Unset):
        state (str | Unset):
        post_code (str | Unset):
        email (list[str] | Unset):
        phone (list[str] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOfDuplicateSearchResultRead]
    """

    kwargs = _get_kwargs(
        last_org_name=last_org_name,
        search_individuals=search_individuals,
        search_aliases=search_aliases,
        search_contacts=search_contacts,
        first_name=first_name,
        middle_name=middle_name,
        suffix=suffix,
        address_block=address_block,
        city=city,
        state=state,
        post_code=post_code,
        email=email,
        phone=phone,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    last_org_name: str,
    search_individuals: bool | Unset = UNSET,
    search_aliases: bool | Unset = UNSET,
    search_contacts: bool | Unset = UNSET,
    first_name: str | Unset = UNSET,
    middle_name: str | Unset = UNSET,
    suffix: str | Unset = UNSET,
    address_block: str | Unset = UNSET,
    city: str | Unset = UNSET,
    state: str | Unset = UNSET,
    post_code: str | Unset = UNSET,
    email: list[str] | Unset = UNSET,
    phone: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | ApiCollectionOfDuplicateSearchResultRead | None:
    """Constituent (Duplicate search)

     Returns possible duplicate records. Searches individual, organization, and related contact records
    and ranks results based on search filters. Records that match multiple filters rank higher as
    potential duplicates.

    Args:
        last_org_name (str):
        search_individuals (bool | Unset):
        search_aliases (bool | Unset):
        search_contacts (bool | Unset):
        first_name (str | Unset):
        middle_name (str | Unset):
        suffix (str | Unset):
        address_block (str | Unset):
        city (str | Unset):
        state (str | Unset):
        post_code (str | Unset):
        email (list[str] | Unset):
        phone (list[str] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOfDuplicateSearchResultRead
    """

    return (
        await asyncio_detailed(
            client=client,
            last_org_name=last_org_name,
            search_individuals=search_individuals,
            search_aliases=search_aliases,
            search_contacts=search_contacts,
            first_name=first_name,
            middle_name=middle_name,
            suffix=suffix,
            address_block=address_block,
            city=city,
            state=state,
            post_code=post_code,
            email=email,
            phone=phone,
            limit=limit,
            offset=offset,
        )
    ).parsed
