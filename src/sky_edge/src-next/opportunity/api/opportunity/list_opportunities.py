import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_collection_opportunity_read import ApiCollectionOpportunityRead
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    search_text: str | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    constituent_id: list[str] | Unset = UNSET,
    list_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_date_added: str | Unset = UNSET
    if not isinstance(date_added, Unset):
        json_date_added = date_added.isoformat()
    params["date_added"] = json_date_added

    json_last_modified: str | Unset = UNSET
    if not isinstance(last_modified, Unset):
        json_last_modified = last_modified.isoformat()
    params["last_modified"] = json_last_modified

    params["include_inactive"] = include_inactive

    params["search_text"] = search_text

    params["sort_token"] = sort_token

    json_constituent_id: list[str] | Unset = UNSET
    if not isinstance(constituent_id, Unset):
        json_constituent_id = constituent_id

    params["constituent_id"] = json_constituent_id

    params["list_id"] = list_id

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/opportunities",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiCollectionOpportunityRead | None:
    if response.status_code == 200:
        response_200 = ApiCollectionOpportunityRead.from_dict(response.json())

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
) -> Response[Any | ApiCollectionOpportunityRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    search_text: str | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    constituent_id: list[str] | Unset = UNSET,
    list_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | ApiCollectionOpportunityRead]:
    """Opportunity list

     Returns a paginated list of opportunities.
    <p />
    The default sorting behavior is to list opportunities in ascending order based on the
    <code>id</code>.
    <p />
    However, the <code>last_modified</code> parameter overrides the default sorting behavior to list
    opportunities in ascending order based on when they were last modified, and the
    <code>date_added</code> parameter overrides the default sorting behavior to list opportunities in
    ascending order based on when they were created. The <code>last_modified</code> parameter also adds
    the <code>sort_token</code> parameter to the <code>next_link</code> URL to ensure that opportunities
    are stably sorted and that order persists when changes occur while working through a paginated list.
    <p />
    If the <code>last_modified</code> and <code>date_added</code> parameters are both specified, the
    sorting behavior is to list opportunities based on when they were last modified.
    <p />

    Args:
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        include_inactive (bool | Unset):
        search_text (str | Unset):
        sort_token (str | Unset):
        constituent_id (list[str] | Unset):
        list_id (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOpportunityRead]
    """

    kwargs = _get_kwargs(
        date_added=date_added,
        last_modified=last_modified,
        include_inactive=include_inactive,
        search_text=search_text,
        sort_token=sort_token,
        constituent_id=constituent_id,
        list_id=list_id,
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
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    search_text: str | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    constituent_id: list[str] | Unset = UNSET,
    list_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | ApiCollectionOpportunityRead | None:
    """Opportunity list

     Returns a paginated list of opportunities.
    <p />
    The default sorting behavior is to list opportunities in ascending order based on the
    <code>id</code>.
    <p />
    However, the <code>last_modified</code> parameter overrides the default sorting behavior to list
    opportunities in ascending order based on when they were last modified, and the
    <code>date_added</code> parameter overrides the default sorting behavior to list opportunities in
    ascending order based on when they were created. The <code>last_modified</code> parameter also adds
    the <code>sort_token</code> parameter to the <code>next_link</code> URL to ensure that opportunities
    are stably sorted and that order persists when changes occur while working through a paginated list.
    <p />
    If the <code>last_modified</code> and <code>date_added</code> parameters are both specified, the
    sorting behavior is to list opportunities based on when they were last modified.
    <p />

    Args:
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        include_inactive (bool | Unset):
        search_text (str | Unset):
        sort_token (str | Unset):
        constituent_id (list[str] | Unset):
        list_id (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOpportunityRead
    """

    return sync_detailed(
        client=client,
        date_added=date_added,
        last_modified=last_modified,
        include_inactive=include_inactive,
        search_text=search_text,
        sort_token=sort_token,
        constituent_id=constituent_id,
        list_id=list_id,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    search_text: str | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    constituent_id: list[str] | Unset = UNSET,
    list_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | ApiCollectionOpportunityRead]:
    """Opportunity list

     Returns a paginated list of opportunities.
    <p />
    The default sorting behavior is to list opportunities in ascending order based on the
    <code>id</code>.
    <p />
    However, the <code>last_modified</code> parameter overrides the default sorting behavior to list
    opportunities in ascending order based on when they were last modified, and the
    <code>date_added</code> parameter overrides the default sorting behavior to list opportunities in
    ascending order based on when they were created. The <code>last_modified</code> parameter also adds
    the <code>sort_token</code> parameter to the <code>next_link</code> URL to ensure that opportunities
    are stably sorted and that order persists when changes occur while working through a paginated list.
    <p />
    If the <code>last_modified</code> and <code>date_added</code> parameters are both specified, the
    sorting behavior is to list opportunities based on when they were last modified.
    <p />

    Args:
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        include_inactive (bool | Unset):
        search_text (str | Unset):
        sort_token (str | Unset):
        constituent_id (list[str] | Unset):
        list_id (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOpportunityRead]
    """

    kwargs = _get_kwargs(
        date_added=date_added,
        last_modified=last_modified,
        include_inactive=include_inactive,
        search_text=search_text,
        sort_token=sort_token,
        constituent_id=constituent_id,
        list_id=list_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    search_text: str | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    constituent_id: list[str] | Unset = UNSET,
    list_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | ApiCollectionOpportunityRead | None:
    """Opportunity list

     Returns a paginated list of opportunities.
    <p />
    The default sorting behavior is to list opportunities in ascending order based on the
    <code>id</code>.
    <p />
    However, the <code>last_modified</code> parameter overrides the default sorting behavior to list
    opportunities in ascending order based on when they were last modified, and the
    <code>date_added</code> parameter overrides the default sorting behavior to list opportunities in
    ascending order based on when they were created. The <code>last_modified</code> parameter also adds
    the <code>sort_token</code> parameter to the <code>next_link</code> URL to ensure that opportunities
    are stably sorted and that order persists when changes occur while working through a paginated list.
    <p />
    If the <code>last_modified</code> and <code>date_added</code> parameters are both specified, the
    sorting behavior is to list opportunities based on when they were last modified.
    <p />

    Args:
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        include_inactive (bool | Unset):
        search_text (str | Unset):
        sort_token (str | Unset):
        constituent_id (list[str] | Unset):
        list_id (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOpportunityRead
    """

    return (
        await asyncio_detailed(
            client=client,
            date_added=date_added,
            last_modified=last_modified,
            include_inactive=include_inactive,
            search_text=search_text,
            sort_token=sort_token,
            constituent_id=constituent_id,
            list_id=list_id,
            limit=limit,
            offset=offset,
        )
    ).parsed
