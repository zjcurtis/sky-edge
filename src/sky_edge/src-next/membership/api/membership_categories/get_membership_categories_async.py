from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_membership_categories_async_membership_category_sort_fields import (
    GetMembershipCategoriesAsyncMembershipCategorySortFields,
)
from ...models.get_membership_categories_async_sort_direction import GetMembershipCategoriesAsyncSortDirection
from ...models.membership_category_collection import MembershipCategoryCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include_inactive: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: GetMembershipCategoriesAsyncMembershipCategorySortFields | Unset = UNSET,
    sort_direction: GetMembershipCategoriesAsyncSortDirection
    | Unset = GetMembershipCategoriesAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_inactive"] = include_inactive

    params["search"] = search

    json_sort_by: str | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sort_by"] = json_sort_by

    json_sort_direction: str | Unset = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sort_direction"] = json_sort_direction

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/memberships/categories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MembershipCategoryCollection | None:
    if response.status_code == 200:
        response_200 = MembershipCategoryCollection.from_dict(response.json())

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
) -> Response[Any | MembershipCategoryCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_inactive: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: GetMembershipCategoriesAsyncMembershipCategorySortFields | Unset = UNSET,
    sort_direction: GetMembershipCategoriesAsyncSortDirection
    | Unset = GetMembershipCategoriesAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Response[Any | MembershipCategoryCollection]:
    """Get membership category list

     Returns a membership category list.

    Args:
        include_inactive (bool | Unset):
        search (str | Unset):
        sort_by (GetMembershipCategoriesAsyncMembershipCategorySortFields | Unset):
        sort_direction (GetMembershipCategoriesAsyncSortDirection | Unset):  Default:
            GetMembershipCategoriesAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MembershipCategoryCollection]
    """

    kwargs = _get_kwargs(
        include_inactive=include_inactive,
        search=search,
        sort_by=sort_by,
        sort_direction=sort_direction,
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
    include_inactive: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: GetMembershipCategoriesAsyncMembershipCategorySortFields | Unset = UNSET,
    sort_direction: GetMembershipCategoriesAsyncSortDirection
    | Unset = GetMembershipCategoriesAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Any | MembershipCategoryCollection | None:
    """Get membership category list

     Returns a membership category list.

    Args:
        include_inactive (bool | Unset):
        search (str | Unset):
        sort_by (GetMembershipCategoriesAsyncMembershipCategorySortFields | Unset):
        sort_direction (GetMembershipCategoriesAsyncSortDirection | Unset):  Default:
            GetMembershipCategoriesAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MembershipCategoryCollection
    """

    return sync_detailed(
        client=client,
        include_inactive=include_inactive,
        search=search,
        sort_by=sort_by,
        sort_direction=sort_direction,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_inactive: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: GetMembershipCategoriesAsyncMembershipCategorySortFields | Unset = UNSET,
    sort_direction: GetMembershipCategoriesAsyncSortDirection
    | Unset = GetMembershipCategoriesAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Response[Any | MembershipCategoryCollection]:
    """Get membership category list

     Returns a membership category list.

    Args:
        include_inactive (bool | Unset):
        search (str | Unset):
        sort_by (GetMembershipCategoriesAsyncMembershipCategorySortFields | Unset):
        sort_direction (GetMembershipCategoriesAsyncSortDirection | Unset):  Default:
            GetMembershipCategoriesAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MembershipCategoryCollection]
    """

    kwargs = _get_kwargs(
        include_inactive=include_inactive,
        search=search,
        sort_by=sort_by,
        sort_direction=sort_direction,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    include_inactive: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: GetMembershipCategoriesAsyncMembershipCategorySortFields | Unset = UNSET,
    sort_direction: GetMembershipCategoriesAsyncSortDirection
    | Unset = GetMembershipCategoriesAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Any | MembershipCategoryCollection | None:
    """Get membership category list

     Returns a membership category list.

    Args:
        include_inactive (bool | Unset):
        search (str | Unset):
        sort_by (GetMembershipCategoriesAsyncMembershipCategorySortFields | Unset):
        sort_direction (GetMembershipCategoriesAsyncSortDirection | Unset):  Default:
            GetMembershipCategoriesAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MembershipCategoryCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            include_inactive=include_inactive,
            search=search,
            sort_by=sort_by,
            sort_direction=sort_direction,
            limit=limit,
            offset=offset,
        )
    ).parsed
