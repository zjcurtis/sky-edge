from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_collection_of_search_result_read import ApiCollectionOfSearchResultRead
from ...models.search_constituent_search_field import SearchConstituentSearchField
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search_text: str,
    fundraiser_status: list[str] | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    search_field: SearchConstituentSearchField | Unset = UNSET,
    strict_search: bool | Unset = UNSET,
    include_non_constituents: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["search_text"] = search_text

    json_fundraiser_status: list[str] | Unset = UNSET
    if not isinstance(fundraiser_status, Unset):
        json_fundraiser_status = fundraiser_status

    params["fundraiser_status"] = json_fundraiser_status

    params["include_inactive"] = include_inactive

    json_search_field: str | Unset = UNSET
    if not isinstance(search_field, Unset):
        json_search_field = search_field.value

    params["search_field"] = json_search_field

    params["strict_search"] = strict_search

    params["include_non_constituents"] = include_non_constituents

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/constituents/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiCollectionOfSearchResultRead | None:
    if response.status_code == 200:
        response_200 = ApiCollectionOfSearchResultRead.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiCollectionOfSearchResultRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    search_text: str,
    fundraiser_status: list[str] | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    search_field: SearchConstituentSearchField | Unset = UNSET,
    strict_search: bool | Unset = UNSET,
    include_non_constituents: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[ApiCollectionOfSearchResultRead]:
    r"""Constituent (Search)

     Performs a constituent search based on the provided search text. Supports first name, last name,
    preferred name, former name, alias, email address, phone number, address, or lookup ID. Name
    combinations, such as first name and last name or preferred name and last name, are valid, but
    otherwise search only supports one parameter at a time.
    <p />
    By default, searches include results that sound similar to your criteria. For example, searches for
    \"Smith\" include matches for \"Smyth\" and other alternative spellings.
    <p />
    Searching by phone number requires a minimum of 7 digits with no spaces or special characters. This
    search does not support wildcard characters — such as * or ? — used to search in the database view.
    <p />
    If searching on a lookup id, the <code>search_field</code> property should be set to 'lookup_id'.
    This will allow the search results to be returned quicker.
    <p />
    If searching on an email address, the <code>search_field</code> property should be set to
    'email_address'. This will allow the search results to be returned quicker. By default, the results
    include non-constituents.
    <p />
    Search results are limited to 500 records.

    Args:
        search_text (str):
        fundraiser_status (list[str] | Unset):
        include_inactive (bool | Unset):
        search_field (SearchConstituentSearchField | Unset):
        strict_search (bool | Unset):
        include_non_constituents (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiCollectionOfSearchResultRead]
    """

    kwargs = _get_kwargs(
        search_text=search_text,
        fundraiser_status=fundraiser_status,
        include_inactive=include_inactive,
        search_field=search_field,
        strict_search=strict_search,
        include_non_constituents=include_non_constituents,
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
    search_text: str,
    fundraiser_status: list[str] | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    search_field: SearchConstituentSearchField | Unset = UNSET,
    strict_search: bool | Unset = UNSET,
    include_non_constituents: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> ApiCollectionOfSearchResultRead | None:
    r"""Constituent (Search)

     Performs a constituent search based on the provided search text. Supports first name, last name,
    preferred name, former name, alias, email address, phone number, address, or lookup ID. Name
    combinations, such as first name and last name or preferred name and last name, are valid, but
    otherwise search only supports one parameter at a time.
    <p />
    By default, searches include results that sound similar to your criteria. For example, searches for
    \"Smith\" include matches for \"Smyth\" and other alternative spellings.
    <p />
    Searching by phone number requires a minimum of 7 digits with no spaces or special characters. This
    search does not support wildcard characters — such as * or ? — used to search in the database view.
    <p />
    If searching on a lookup id, the <code>search_field</code> property should be set to 'lookup_id'.
    This will allow the search results to be returned quicker.
    <p />
    If searching on an email address, the <code>search_field</code> property should be set to
    'email_address'. This will allow the search results to be returned quicker. By default, the results
    include non-constituents.
    <p />
    Search results are limited to 500 records.

    Args:
        search_text (str):
        fundraiser_status (list[str] | Unset):
        include_inactive (bool | Unset):
        search_field (SearchConstituentSearchField | Unset):
        strict_search (bool | Unset):
        include_non_constituents (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiCollectionOfSearchResultRead
    """

    return sync_detailed(
        client=client,
        search_text=search_text,
        fundraiser_status=fundraiser_status,
        include_inactive=include_inactive,
        search_field=search_field,
        strict_search=strict_search,
        include_non_constituents=include_non_constituents,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    search_text: str,
    fundraiser_status: list[str] | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    search_field: SearchConstituentSearchField | Unset = UNSET,
    strict_search: bool | Unset = UNSET,
    include_non_constituents: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[ApiCollectionOfSearchResultRead]:
    r"""Constituent (Search)

     Performs a constituent search based on the provided search text. Supports first name, last name,
    preferred name, former name, alias, email address, phone number, address, or lookup ID. Name
    combinations, such as first name and last name or preferred name and last name, are valid, but
    otherwise search only supports one parameter at a time.
    <p />
    By default, searches include results that sound similar to your criteria. For example, searches for
    \"Smith\" include matches for \"Smyth\" and other alternative spellings.
    <p />
    Searching by phone number requires a minimum of 7 digits with no spaces or special characters. This
    search does not support wildcard characters — such as * or ? — used to search in the database view.
    <p />
    If searching on a lookup id, the <code>search_field</code> property should be set to 'lookup_id'.
    This will allow the search results to be returned quicker.
    <p />
    If searching on an email address, the <code>search_field</code> property should be set to
    'email_address'. This will allow the search results to be returned quicker. By default, the results
    include non-constituents.
    <p />
    Search results are limited to 500 records.

    Args:
        search_text (str):
        fundraiser_status (list[str] | Unset):
        include_inactive (bool | Unset):
        search_field (SearchConstituentSearchField | Unset):
        strict_search (bool | Unset):
        include_non_constituents (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiCollectionOfSearchResultRead]
    """

    kwargs = _get_kwargs(
        search_text=search_text,
        fundraiser_status=fundraiser_status,
        include_inactive=include_inactive,
        search_field=search_field,
        strict_search=strict_search,
        include_non_constituents=include_non_constituents,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    search_text: str,
    fundraiser_status: list[str] | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    search_field: SearchConstituentSearchField | Unset = UNSET,
    strict_search: bool | Unset = UNSET,
    include_non_constituents: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> ApiCollectionOfSearchResultRead | None:
    r"""Constituent (Search)

     Performs a constituent search based on the provided search text. Supports first name, last name,
    preferred name, former name, alias, email address, phone number, address, or lookup ID. Name
    combinations, such as first name and last name or preferred name and last name, are valid, but
    otherwise search only supports one parameter at a time.
    <p />
    By default, searches include results that sound similar to your criteria. For example, searches for
    \"Smith\" include matches for \"Smyth\" and other alternative spellings.
    <p />
    Searching by phone number requires a minimum of 7 digits with no spaces or special characters. This
    search does not support wildcard characters — such as * or ? — used to search in the database view.
    <p />
    If searching on a lookup id, the <code>search_field</code> property should be set to 'lookup_id'.
    This will allow the search results to be returned quicker.
    <p />
    If searching on an email address, the <code>search_field</code> property should be set to
    'email_address'. This will allow the search results to be returned quicker. By default, the results
    include non-constituents.
    <p />
    Search results are limited to 500 records.

    Args:
        search_text (str):
        fundraiser_status (list[str] | Unset):
        include_inactive (bool | Unset):
        search_field (SearchConstituentSearchField | Unset):
        strict_search (bool | Unset):
        include_non_constituents (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiCollectionOfSearchResultRead
    """

    return (
        await asyncio_detailed(
            client=client,
            search_text=search_text,
            fundraiser_status=fundraiser_status,
            include_inactive=include_inactive,
            search_field=search_field,
            strict_search=strict_search,
            include_non_constituents=include_non_constituents,
            limit=limit,
            offset=offset,
        )
    ).parsed
