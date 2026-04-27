import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.api_collection_of_constituent_list_item import (
    ApiCollectionOfConstituentListItem,
)


def _get_kwargs(
    *,
    constituent_code: list[str] | Unset = UNSET,
    constituent_id: list[str] | Unset = UNSET,
    custom_field_category: list[str] | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    fundraiser_status: list[str] | Unset = UNSET,
    include_deceased: bool | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    list_id: str | Unset = UNSET,
    postal_code: list[str] | Unset = UNSET,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_constituent_code: list[str] | Unset = UNSET
    if not isinstance(constituent_code, Unset):
        json_constituent_code = constituent_code

    params["constituent_code"] = json_constituent_code

    json_constituent_id: list[str] | Unset = UNSET
    if not isinstance(constituent_id, Unset):
        json_constituent_id = constituent_id

    params["constituent_id"] = json_constituent_id

    json_custom_field_category: list[str] | Unset = UNSET
    if not isinstance(custom_field_category, Unset):
        json_custom_field_category = custom_field_category

    params["custom_field_category"] = json_custom_field_category

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    json_fundraiser_status: list[str] | Unset = UNSET
    if not isinstance(fundraiser_status, Unset):
        json_fundraiser_status = fundraiser_status

    params["fundraiser_status"] = json_fundraiser_status

    params["include_deceased"] = include_deceased

    params["include_inactive"] = include_inactive

    params["list_id"] = list_id

    json_postal_code: list[str] | Unset = UNSET
    if not isinstance(postal_code, Unset):
        json_postal_code = postal_code

    params["postal_code"] = json_postal_code

    json_date_added: str | Unset = UNSET
    if not isinstance(date_added, Unset):
        json_date_added = date_added.isoformat()
    params["date_added"] = json_date_added

    json_last_modified: str | Unset = UNSET
    if not isinstance(last_modified, Unset):
        json_last_modified = last_modified.isoformat()
    params["last_modified"] = json_last_modified

    params["sort_token"] = sort_token

    json_sort: list[str] | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/constituents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiCollectionOfConstituentListItem | None:
    if response.status_code == 200:
        response_200 = ApiCollectionOfConstituentListItem.from_dict(response.json())

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
) -> Response[Any | ApiCollectionOfConstituentListItem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    constituent_code: list[str] | Unset = UNSET,
    constituent_id: list[str] | Unset = UNSET,
    custom_field_category: list[str] | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    fundraiser_status: list[str] | Unset = UNSET,
    include_deceased: bool | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    list_id: str | Unset = UNSET,
    postal_code: list[str] | Unset = UNSET,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | ApiCollectionOfConstituentListItem]:
    """Constituent list

     Returns a paginated list of constituents.
    <p />
    The default sorting behavior is to list constituents in ascending alphabetical order based on the
    full name of organizations and the last name of individuals. However, some parameters override the
    default sorting behavior. The <code>sort</code> parameter sorts based on the fields that it
    specifies, and the <code>sort_token</code> parameter sorts based on the next stable-sorted list of
    results. (These parameters cannot be provided together.) If the <code>sort</code> and
    <code>sort_token</code> parameters are not provided, then the <code>last_modified</code> parameter
    sorts constituents in ascending order based on when they were last modified and the
    <code>date_added</code> parameter sorts constituents in ascending order based on when they were
    created. (If the <code>last_modified</code> and <code>date_added</code> parameters are both
    specified, sorting is based on the last-modified date.)
    <p />
    Some parameters also add the <code>sort_token</code> parameter to the <code>next_link</code> URL to
    ensure that constituents are stably sorted and that the order persists even if changes occur while
    working through a paginated list. The <code>last_modified</code>, <code>date_added</code>, and
    <code>sort</code> parameters all add the <code>sort_token</code> parameter to the
    <code>next_link</code> URL, although the <code>sort</code> parameter only adds the
    <code>sort_token</code> parameter when it sorts by just the <code>date_added</code> field or just
    the <code>date_modified</code> field.
    <p /><b>Note:</b> This endpoint returns data with an average latency of about 30 minutes.

    Args:
        constituent_code (list[str] | Unset):
        constituent_id (list[str] | Unset):
        custom_field_category (list[str] | Unset):
        fields (list[str] | Unset):
        fundraiser_status (list[str] | Unset):
        include_deceased (bool | Unset):
        include_inactive (bool | Unset):
        list_id (str | Unset):
        postal_code (list[str] | Unset):
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        sort_token (str | Unset):
        sort (list[str] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOfConstituentListItem]
    """

    kwargs = _get_kwargs(
        constituent_code=constituent_code,
        constituent_id=constituent_id,
        custom_field_category=custom_field_category,
        fields=fields,
        fundraiser_status=fundraiser_status,
        include_deceased=include_deceased,
        include_inactive=include_inactive,
        list_id=list_id,
        postal_code=postal_code,
        date_added=date_added,
        last_modified=last_modified,
        sort_token=sort_token,
        sort=sort,
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
    constituent_code: list[str] | Unset = UNSET,
    constituent_id: list[str] | Unset = UNSET,
    custom_field_category: list[str] | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    fundraiser_status: list[str] | Unset = UNSET,
    include_deceased: bool | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    list_id: str | Unset = UNSET,
    postal_code: list[str] | Unset = UNSET,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | ApiCollectionOfConstituentListItem | None:
    """Constituent list

     Returns a paginated list of constituents.
    <p />
    The default sorting behavior is to list constituents in ascending alphabetical order based on the
    full name of organizations and the last name of individuals. However, some parameters override the
    default sorting behavior. The <code>sort</code> parameter sorts based on the fields that it
    specifies, and the <code>sort_token</code> parameter sorts based on the next stable-sorted list of
    results. (These parameters cannot be provided together.) If the <code>sort</code> and
    <code>sort_token</code> parameters are not provided, then the <code>last_modified</code> parameter
    sorts constituents in ascending order based on when they were last modified and the
    <code>date_added</code> parameter sorts constituents in ascending order based on when they were
    created. (If the <code>last_modified</code> and <code>date_added</code> parameters are both
    specified, sorting is based on the last-modified date.)
    <p />
    Some parameters also add the <code>sort_token</code> parameter to the <code>next_link</code> URL to
    ensure that constituents are stably sorted and that the order persists even if changes occur while
    working through a paginated list. The <code>last_modified</code>, <code>date_added</code>, and
    <code>sort</code> parameters all add the <code>sort_token</code> parameter to the
    <code>next_link</code> URL, although the <code>sort</code> parameter only adds the
    <code>sort_token</code> parameter when it sorts by just the <code>date_added</code> field or just
    the <code>date_modified</code> field.
    <p /><b>Note:</b> This endpoint returns data with an average latency of about 30 minutes.

    Args:
        constituent_code (list[str] | Unset):
        constituent_id (list[str] | Unset):
        custom_field_category (list[str] | Unset):
        fields (list[str] | Unset):
        fundraiser_status (list[str] | Unset):
        include_deceased (bool | Unset):
        include_inactive (bool | Unset):
        list_id (str | Unset):
        postal_code (list[str] | Unset):
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        sort_token (str | Unset):
        sort (list[str] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOfConstituentListItem
    """

    return sync_detailed(
        client=client,
        constituent_code=constituent_code,
        constituent_id=constituent_id,
        custom_field_category=custom_field_category,
        fields=fields,
        fundraiser_status=fundraiser_status,
        include_deceased=include_deceased,
        include_inactive=include_inactive,
        list_id=list_id,
        postal_code=postal_code,
        date_added=date_added,
        last_modified=last_modified,
        sort_token=sort_token,
        sort=sort,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    constituent_code: list[str] | Unset = UNSET,
    constituent_id: list[str] | Unset = UNSET,
    custom_field_category: list[str] | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    fundraiser_status: list[str] | Unset = UNSET,
    include_deceased: bool | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    list_id: str | Unset = UNSET,
    postal_code: list[str] | Unset = UNSET,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | ApiCollectionOfConstituentListItem]:
    """Constituent list

     Returns a paginated list of constituents.
    <p />
    The default sorting behavior is to list constituents in ascending alphabetical order based on the
    full name of organizations and the last name of individuals. However, some parameters override the
    default sorting behavior. The <code>sort</code> parameter sorts based on the fields that it
    specifies, and the <code>sort_token</code> parameter sorts based on the next stable-sorted list of
    results. (These parameters cannot be provided together.) If the <code>sort</code> and
    <code>sort_token</code> parameters are not provided, then the <code>last_modified</code> parameter
    sorts constituents in ascending order based on when they were last modified and the
    <code>date_added</code> parameter sorts constituents in ascending order based on when they were
    created. (If the <code>last_modified</code> and <code>date_added</code> parameters are both
    specified, sorting is based on the last-modified date.)
    <p />
    Some parameters also add the <code>sort_token</code> parameter to the <code>next_link</code> URL to
    ensure that constituents are stably sorted and that the order persists even if changes occur while
    working through a paginated list. The <code>last_modified</code>, <code>date_added</code>, and
    <code>sort</code> parameters all add the <code>sort_token</code> parameter to the
    <code>next_link</code> URL, although the <code>sort</code> parameter only adds the
    <code>sort_token</code> parameter when it sorts by just the <code>date_added</code> field or just
    the <code>date_modified</code> field.
    <p /><b>Note:</b> This endpoint returns data with an average latency of about 30 minutes.

    Args:
        constituent_code (list[str] | Unset):
        constituent_id (list[str] | Unset):
        custom_field_category (list[str] | Unset):
        fields (list[str] | Unset):
        fundraiser_status (list[str] | Unset):
        include_deceased (bool | Unset):
        include_inactive (bool | Unset):
        list_id (str | Unset):
        postal_code (list[str] | Unset):
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        sort_token (str | Unset):
        sort (list[str] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOfConstituentListItem]
    """

    kwargs = _get_kwargs(
        constituent_code=constituent_code,
        constituent_id=constituent_id,
        custom_field_category=custom_field_category,
        fields=fields,
        fundraiser_status=fundraiser_status,
        include_deceased=include_deceased,
        include_inactive=include_inactive,
        list_id=list_id,
        postal_code=postal_code,
        date_added=date_added,
        last_modified=last_modified,
        sort_token=sort_token,
        sort=sort,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    constituent_code: list[str] | Unset = UNSET,
    constituent_id: list[str] | Unset = UNSET,
    custom_field_category: list[str] | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    fundraiser_status: list[str] | Unset = UNSET,
    include_deceased: bool | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    list_id: str | Unset = UNSET,
    postal_code: list[str] | Unset = UNSET,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | ApiCollectionOfConstituentListItem | None:
    """Constituent list

     Returns a paginated list of constituents.
    <p />
    The default sorting behavior is to list constituents in ascending alphabetical order based on the
    full name of organizations and the last name of individuals. However, some parameters override the
    default sorting behavior. The <code>sort</code> parameter sorts based on the fields that it
    specifies, and the <code>sort_token</code> parameter sorts based on the next stable-sorted list of
    results. (These parameters cannot be provided together.) If the <code>sort</code> and
    <code>sort_token</code> parameters are not provided, then the <code>last_modified</code> parameter
    sorts constituents in ascending order based on when they were last modified and the
    <code>date_added</code> parameter sorts constituents in ascending order based on when they were
    created. (If the <code>last_modified</code> and <code>date_added</code> parameters are both
    specified, sorting is based on the last-modified date.)
    <p />
    Some parameters also add the <code>sort_token</code> parameter to the <code>next_link</code> URL to
    ensure that constituents are stably sorted and that the order persists even if changes occur while
    working through a paginated list. The <code>last_modified</code>, <code>date_added</code>, and
    <code>sort</code> parameters all add the <code>sort_token</code> parameter to the
    <code>next_link</code> URL, although the <code>sort</code> parameter only adds the
    <code>sort_token</code> parameter when it sorts by just the <code>date_added</code> field or just
    the <code>date_modified</code> field.
    <p /><b>Note:</b> This endpoint returns data with an average latency of about 30 minutes.

    Args:
        constituent_code (list[str] | Unset):
        constituent_id (list[str] | Unset):
        custom_field_category (list[str] | Unset):
        fields (list[str] | Unset):
        fundraiser_status (list[str] | Unset):
        include_deceased (bool | Unset):
        include_inactive (bool | Unset):
        list_id (str | Unset):
        postal_code (list[str] | Unset):
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        sort_token (str | Unset):
        sort (list[str] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOfConstituentListItem
    """

    return (
        await asyncio_detailed(
            client=client,
            constituent_code=constituent_code,
            constituent_id=constituent_id,
            custom_field_category=custom_field_category,
            fields=fields,
            fundraiser_status=fundraiser_status,
            include_deceased=include_deceased,
            include_inactive=include_inactive,
            list_id=list_id,
            postal_code=postal_code,
            date_added=date_added,
            last_modified=last_modified,
            sort_token=sort_token,
            sort=sort,
            limit=limit,
            offset=offset,
        )
    ).parsed
