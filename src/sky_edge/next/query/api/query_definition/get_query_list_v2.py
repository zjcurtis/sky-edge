import datetime
from http import HTTPStatus
from typing import Any

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.get_query_list_v2_error_codes import GetQueryListV2ErrorCodes
from ...models.get_query_list_v2_module import GetQueryListV2Module
from ...models.get_query_list_v2_product import GetQueryListV2Product
from ...models.get_query_list_v2_response import GetQueryListV2Response
from ...models.problem_details import ProblemDetails
from ...models.query_format import QueryFormat
from ...models.query_list_list_query_filter import QueryListListQueryFilter
from ...models.query_list_sortable_column import QueryListSortableColumn


def _get_kwargs(
    *,
    product: GetQueryListV2Product,
    module: GetQueryListV2Module,
    continuation_token: str | Unset = UNSET,
    category: int | Unset = UNSET,
    limit: int | Unset = 50,
    search_text: str | Unset = UNSET,
    merged_queries_only: bool | Unset = False,
    my_queries_only: bool | Unset = False,
    query_type_ids: list[int] | Unset = UNSET,
    query_format: QueryFormat | Unset = UNSET,
    sort_descending: bool | Unset = False,
    sort_column: QueryListSortableColumn | Unset = UNSET,
    list_queries: QueryListListQueryFilter | Unset = UNSET,
    my_fav_queries_only: bool | Unset = False,
    date_added: datetime.datetime | Unset = UNSET,
    added_by: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_product = product.value
    params["product"] = json_product

    json_module = module.value
    params["module"] = json_module

    params["continuation_token"] = continuation_token

    params["category"] = category

    params["limit"] = limit

    params["search_text"] = search_text

    params["merged_queries_only"] = merged_queries_only

    params["my_queries_only"] = my_queries_only

    json_query_type_ids: list[int] | Unset = UNSET
    if not isinstance(query_type_ids, Unset):
        json_query_type_ids = query_type_ids

    params["query_type_ids"] = json_query_type_ids

    json_query_format: str | Unset = UNSET
    if not isinstance(query_format, Unset):
        json_query_format = query_format.value

    params["query_format"] = json_query_format

    params["sort_descending"] = sort_descending

    json_sort_column: str | Unset = UNSET
    if not isinstance(sort_column, Unset):
        json_sort_column = sort_column.value

    params["sort_column"] = json_sort_column

    json_list_queries: str | Unset = UNSET
    if not isinstance(list_queries, Unset):
        json_list_queries = list_queries.value

    params["list_queries"] = json_list_queries

    params["my_fav_queries_only"] = my_fav_queries_only

    json_date_added: str | Unset = UNSET
    if not isinstance(date_added, Unset):
        json_date_added = date_added.isoformat()
    params["date_added"] = json_date_added

    params["added_by"] = added_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/queries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetQueryListV2ErrorCodes | GetQueryListV2Response | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = GetQueryListV2Response.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetQueryListV2ErrorCodes.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetQueryListV2ErrorCodes | GetQueryListV2Response | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    product: GetQueryListV2Product,
    module: GetQueryListV2Module,
    continuation_token: str | Unset = UNSET,
    category: int | Unset = UNSET,
    limit: int | Unset = 50,
    search_text: str | Unset = UNSET,
    merged_queries_only: bool | Unset = False,
    my_queries_only: bool | Unset = False,
    query_type_ids: list[int] | Unset = UNSET,
    query_format: QueryFormat | Unset = UNSET,
    sort_descending: bool | Unset = False,
    sort_column: QueryListSortableColumn | Unset = UNSET,
    list_queries: QueryListListQueryFilter | Unset = UNSET,
    my_fav_queries_only: bool | Unset = False,
    date_added: datetime.datetime | Unset = UNSET,
    added_by: str | Unset = UNSET,
) -> Response[GetQueryListV2ErrorCodes | GetQueryListV2Response | ProblemDetails]:
    """Query list (V2) (PREVIEW)

     Gets a list of queries leveraging a continuation token for paging results.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        product (GetQueryListV2Product):
        module (GetQueryListV2Module):
        continuation_token (str | Unset):
        category (int | Unset):
        limit (int | Unset):  Default: 50.
        search_text (str | Unset):
        merged_queries_only (bool | Unset):  Default: False.
        my_queries_only (bool | Unset):  Default: False.
        query_type_ids (list[int] | Unset):
        query_format (QueryFormat | Unset): Available formats for
            queries<p>Members:</p><ul><li><i>Dynamic</i> - The query results are obtained by executing
            the query SQL</li><li><i>Static</i> - The IDs of the records found by the query are saved
            to a table</li></ul>
        sort_descending (bool | Unset):  Default: False.
        sort_column (QueryListSortableColumn | Unset): Options for sorting the query list<p>Member
            s:</p><ul><li><i>Name</i></li><li><i>DateLastRun</i></li><li><i>DateChanged</i></li><li><i
            >ElapsedMs</i></li><li><i>DateAdded</i></li><li><i>AddedBy</i></li><li><i>LastChangedBy</i
            ></li><li><i>Records</i></li></ul>
        list_queries (QueryListListQueryFilter | Unset): Options for including or excluding list
            queries. Will eventually support only list queries.<p>Members:</p><ul><li><i>Unset</i> -
            No filtering applied</li><li><i>NoListQueries</i> - Exclude all list queries</li></ul>
        my_fav_queries_only (bool | Unset):  Default: False.
        date_added (datetime.datetime | Unset):
        added_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetQueryListV2ErrorCodes | GetQueryListV2Response | ProblemDetails]
    """

    kwargs = _get_kwargs(
        product=product,
        module=module,
        continuation_token=continuation_token,
        category=category,
        limit=limit,
        search_text=search_text,
        merged_queries_only=merged_queries_only,
        my_queries_only=my_queries_only,
        query_type_ids=query_type_ids,
        query_format=query_format,
        sort_descending=sort_descending,
        sort_column=sort_column,
        list_queries=list_queries,
        my_fav_queries_only=my_fav_queries_only,
        date_added=date_added,
        added_by=added_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    product: GetQueryListV2Product,
    module: GetQueryListV2Module,
    continuation_token: str | Unset = UNSET,
    category: int | Unset = UNSET,
    limit: int | Unset = 50,
    search_text: str | Unset = UNSET,
    merged_queries_only: bool | Unset = False,
    my_queries_only: bool | Unset = False,
    query_type_ids: list[int] | Unset = UNSET,
    query_format: QueryFormat | Unset = UNSET,
    sort_descending: bool | Unset = False,
    sort_column: QueryListSortableColumn | Unset = UNSET,
    list_queries: QueryListListQueryFilter | Unset = UNSET,
    my_fav_queries_only: bool | Unset = False,
    date_added: datetime.datetime | Unset = UNSET,
    added_by: str | Unset = UNSET,
) -> GetQueryListV2ErrorCodes | GetQueryListV2Response | ProblemDetails | None:
    """Query list (V2) (PREVIEW)

     Gets a list of queries leveraging a continuation token for paging results.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        product (GetQueryListV2Product):
        module (GetQueryListV2Module):
        continuation_token (str | Unset):
        category (int | Unset):
        limit (int | Unset):  Default: 50.
        search_text (str | Unset):
        merged_queries_only (bool | Unset):  Default: False.
        my_queries_only (bool | Unset):  Default: False.
        query_type_ids (list[int] | Unset):
        query_format (QueryFormat | Unset): Available formats for
            queries<p>Members:</p><ul><li><i>Dynamic</i> - The query results are obtained by executing
            the query SQL</li><li><i>Static</i> - The IDs of the records found by the query are saved
            to a table</li></ul>
        sort_descending (bool | Unset):  Default: False.
        sort_column (QueryListSortableColumn | Unset): Options for sorting the query list<p>Member
            s:</p><ul><li><i>Name</i></li><li><i>DateLastRun</i></li><li><i>DateChanged</i></li><li><i
            >ElapsedMs</i></li><li><i>DateAdded</i></li><li><i>AddedBy</i></li><li><i>LastChangedBy</i
            ></li><li><i>Records</i></li></ul>
        list_queries (QueryListListQueryFilter | Unset): Options for including or excluding list
            queries. Will eventually support only list queries.<p>Members:</p><ul><li><i>Unset</i> -
            No filtering applied</li><li><i>NoListQueries</i> - Exclude all list queries</li></ul>
        my_fav_queries_only (bool | Unset):  Default: False.
        date_added (datetime.datetime | Unset):
        added_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetQueryListV2ErrorCodes | GetQueryListV2Response | ProblemDetails
    """

    return sync_detailed(
        client=client,
        product=product,
        module=module,
        continuation_token=continuation_token,
        category=category,
        limit=limit,
        search_text=search_text,
        merged_queries_only=merged_queries_only,
        my_queries_only=my_queries_only,
        query_type_ids=query_type_ids,
        query_format=query_format,
        sort_descending=sort_descending,
        sort_column=sort_column,
        list_queries=list_queries,
        my_fav_queries_only=my_fav_queries_only,
        date_added=date_added,
        added_by=added_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    product: GetQueryListV2Product,
    module: GetQueryListV2Module,
    continuation_token: str | Unset = UNSET,
    category: int | Unset = UNSET,
    limit: int | Unset = 50,
    search_text: str | Unset = UNSET,
    merged_queries_only: bool | Unset = False,
    my_queries_only: bool | Unset = False,
    query_type_ids: list[int] | Unset = UNSET,
    query_format: QueryFormat | Unset = UNSET,
    sort_descending: bool | Unset = False,
    sort_column: QueryListSortableColumn | Unset = UNSET,
    list_queries: QueryListListQueryFilter | Unset = UNSET,
    my_fav_queries_only: bool | Unset = False,
    date_added: datetime.datetime | Unset = UNSET,
    added_by: str | Unset = UNSET,
) -> Response[GetQueryListV2ErrorCodes | GetQueryListV2Response | ProblemDetails]:
    """Query list (V2) (PREVIEW)

     Gets a list of queries leveraging a continuation token for paging results.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        product (GetQueryListV2Product):
        module (GetQueryListV2Module):
        continuation_token (str | Unset):
        category (int | Unset):
        limit (int | Unset):  Default: 50.
        search_text (str | Unset):
        merged_queries_only (bool | Unset):  Default: False.
        my_queries_only (bool | Unset):  Default: False.
        query_type_ids (list[int] | Unset):
        query_format (QueryFormat | Unset): Available formats for
            queries<p>Members:</p><ul><li><i>Dynamic</i> - The query results are obtained by executing
            the query SQL</li><li><i>Static</i> - The IDs of the records found by the query are saved
            to a table</li></ul>
        sort_descending (bool | Unset):  Default: False.
        sort_column (QueryListSortableColumn | Unset): Options for sorting the query list<p>Member
            s:</p><ul><li><i>Name</i></li><li><i>DateLastRun</i></li><li><i>DateChanged</i></li><li><i
            >ElapsedMs</i></li><li><i>DateAdded</i></li><li><i>AddedBy</i></li><li><i>LastChangedBy</i
            ></li><li><i>Records</i></li></ul>
        list_queries (QueryListListQueryFilter | Unset): Options for including or excluding list
            queries. Will eventually support only list queries.<p>Members:</p><ul><li><i>Unset</i> -
            No filtering applied</li><li><i>NoListQueries</i> - Exclude all list queries</li></ul>
        my_fav_queries_only (bool | Unset):  Default: False.
        date_added (datetime.datetime | Unset):
        added_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetQueryListV2ErrorCodes | GetQueryListV2Response | ProblemDetails]
    """

    kwargs = _get_kwargs(
        product=product,
        module=module,
        continuation_token=continuation_token,
        category=category,
        limit=limit,
        search_text=search_text,
        merged_queries_only=merged_queries_only,
        my_queries_only=my_queries_only,
        query_type_ids=query_type_ids,
        query_format=query_format,
        sort_descending=sort_descending,
        sort_column=sort_column,
        list_queries=list_queries,
        my_fav_queries_only=my_fav_queries_only,
        date_added=date_added,
        added_by=added_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    product: GetQueryListV2Product,
    module: GetQueryListV2Module,
    continuation_token: str | Unset = UNSET,
    category: int | Unset = UNSET,
    limit: int | Unset = 50,
    search_text: str | Unset = UNSET,
    merged_queries_only: bool | Unset = False,
    my_queries_only: bool | Unset = False,
    query_type_ids: list[int] | Unset = UNSET,
    query_format: QueryFormat | Unset = UNSET,
    sort_descending: bool | Unset = False,
    sort_column: QueryListSortableColumn | Unset = UNSET,
    list_queries: QueryListListQueryFilter | Unset = UNSET,
    my_fav_queries_only: bool | Unset = False,
    date_added: datetime.datetime | Unset = UNSET,
    added_by: str | Unset = UNSET,
) -> GetQueryListV2ErrorCodes | GetQueryListV2Response | ProblemDetails | None:
    """Query list (V2) (PREVIEW)

     Gets a list of queries leveraging a continuation token for paging results.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        product (GetQueryListV2Product):
        module (GetQueryListV2Module):
        continuation_token (str | Unset):
        category (int | Unset):
        limit (int | Unset):  Default: 50.
        search_text (str | Unset):
        merged_queries_only (bool | Unset):  Default: False.
        my_queries_only (bool | Unset):  Default: False.
        query_type_ids (list[int] | Unset):
        query_format (QueryFormat | Unset): Available formats for
            queries<p>Members:</p><ul><li><i>Dynamic</i> - The query results are obtained by executing
            the query SQL</li><li><i>Static</i> - The IDs of the records found by the query are saved
            to a table</li></ul>
        sort_descending (bool | Unset):  Default: False.
        sort_column (QueryListSortableColumn | Unset): Options for sorting the query list<p>Member
            s:</p><ul><li><i>Name</i></li><li><i>DateLastRun</i></li><li><i>DateChanged</i></li><li><i
            >ElapsedMs</i></li><li><i>DateAdded</i></li><li><i>AddedBy</i></li><li><i>LastChangedBy</i
            ></li><li><i>Records</i></li></ul>
        list_queries (QueryListListQueryFilter | Unset): Options for including or excluding list
            queries. Will eventually support only list queries.<p>Members:</p><ul><li><i>Unset</i> -
            No filtering applied</li><li><i>NoListQueries</i> - Exclude all list queries</li></ul>
        my_fav_queries_only (bool | Unset):  Default: False.
        date_added (datetime.datetime | Unset):
        added_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetQueryListV2ErrorCodes | GetQueryListV2Response | ProblemDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            product=product,
            module=module,
            continuation_token=continuation_token,
            category=category,
            limit=limit,
            search_text=search_text,
            merged_queries_only=merged_queries_only,
            my_queries_only=my_queries_only,
            query_type_ids=query_type_ids,
            query_format=query_format,
            sort_descending=sort_descending,
            sort_column=sort_column,
            list_queries=list_queries,
            my_fav_queries_only=my_fav_queries_only,
            date_added=date_added,
            added_by=added_by,
        )
    ).parsed
