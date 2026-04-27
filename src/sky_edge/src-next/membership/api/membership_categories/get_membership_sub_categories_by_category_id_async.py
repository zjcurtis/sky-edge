from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_membership_sub_categories_by_category_id_async_sort_direction import (
    GetMembershipSubCategoriesByCategoryIdAsyncSortDirection,
)
from ...models.membership_sub_category_collection import MembershipSubCategoryCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    membership_category_id: str,
    *,
    search: str | Unset = UNSET,
    sort_direction: GetMembershipSubCategoriesByCategoryIdAsyncSortDirection
    | Unset = GetMembershipSubCategoriesByCategoryIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["search"] = search

    json_sort_direction: str | Unset = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sort_direction"] = json_sort_direction

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/memberships/categories/{membership_category_id}/subcategories".format(
            membership_category_id=quote(str(membership_category_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MembershipSubCategoryCollection | None:
    if response.status_code == 200:
        response_200 = MembershipSubCategoryCollection.from_dict(response.json())

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
) -> Response[Any | MembershipSubCategoryCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    membership_category_id: str,
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = UNSET,
    sort_direction: GetMembershipSubCategoriesByCategoryIdAsyncSortDirection
    | Unset = GetMembershipSubCategoriesByCategoryIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Response[Any | MembershipSubCategoryCollection]:
    """Get membership subcategory list based on category.

     Returns a list of membership subcategories by category ID.

    Args:
        membership_category_id (str):
        search (str | Unset):
        sort_direction (GetMembershipSubCategoriesByCategoryIdAsyncSortDirection | Unset):
            Default: GetMembershipSubCategoriesByCategoryIdAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MembershipSubCategoryCollection]
    """

    kwargs = _get_kwargs(
        membership_category_id=membership_category_id,
        search=search,
        sort_direction=sort_direction,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    membership_category_id: str,
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = UNSET,
    sort_direction: GetMembershipSubCategoriesByCategoryIdAsyncSortDirection
    | Unset = GetMembershipSubCategoriesByCategoryIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Any | MembershipSubCategoryCollection | None:
    """Get membership subcategory list based on category.

     Returns a list of membership subcategories by category ID.

    Args:
        membership_category_id (str):
        search (str | Unset):
        sort_direction (GetMembershipSubCategoriesByCategoryIdAsyncSortDirection | Unset):
            Default: GetMembershipSubCategoriesByCategoryIdAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MembershipSubCategoryCollection
    """

    return sync_detailed(
        membership_category_id=membership_category_id,
        client=client,
        search=search,
        sort_direction=sort_direction,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    membership_category_id: str,
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = UNSET,
    sort_direction: GetMembershipSubCategoriesByCategoryIdAsyncSortDirection
    | Unset = GetMembershipSubCategoriesByCategoryIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Response[Any | MembershipSubCategoryCollection]:
    """Get membership subcategory list based on category.

     Returns a list of membership subcategories by category ID.

    Args:
        membership_category_id (str):
        search (str | Unset):
        sort_direction (GetMembershipSubCategoriesByCategoryIdAsyncSortDirection | Unset):
            Default: GetMembershipSubCategoriesByCategoryIdAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MembershipSubCategoryCollection]
    """

    kwargs = _get_kwargs(
        membership_category_id=membership_category_id,
        search=search,
        sort_direction=sort_direction,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    membership_category_id: str,
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = UNSET,
    sort_direction: GetMembershipSubCategoriesByCategoryIdAsyncSortDirection
    | Unset = GetMembershipSubCategoriesByCategoryIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Any | MembershipSubCategoryCollection | None:
    """Get membership subcategory list based on category.

     Returns a list of membership subcategories by category ID.

    Args:
        membership_category_id (str):
        search (str | Unset):
        sort_direction (GetMembershipSubCategoriesByCategoryIdAsyncSortDirection | Unset):
            Default: GetMembershipSubCategoriesByCategoryIdAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MembershipSubCategoryCollection
    """

    return (
        await asyncio_detailed(
            membership_category_id=membership_category_id,
            client=client,
            search=search,
            sort_direction=sort_direction,
            limit=limit,
            offset=offset,
        )
    ).parsed
