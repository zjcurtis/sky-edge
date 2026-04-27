import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_collection_appeal_read import ApiCollectionAppealRead
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    appeal_id: list[str] | Unset = UNSET,
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

    params["sort_token"] = sort_token

    params["include_inactive"] = include_inactive

    json_appeal_id: list[str] | Unset = UNSET
    if not isinstance(appeal_id, Unset):
        json_appeal_id = appeal_id

    params["appeal_id"] = json_appeal_id

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/appeals",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiCollectionAppealRead | None:
    if response.status_code == 200:
        response_200 = ApiCollectionAppealRead.from_dict(response.json())

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
) -> Response[Any | ApiCollectionAppealRead]:
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
    sort_token: str | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    appeal_id: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | ApiCollectionAppealRead]:
    """Appeal list

     Returns a paginated list of appeals.
    <p />
    The default sorting behavior is to list appeals in ascending order based on when they were created.
    <p />
    However, the <code>last_modified</code> parameter overrides the default sorting behavior to list
    appeals in ascending order based on when they were last modified. The <code>last_modified</code>
    parameter also adds the <code>sort_token</code> parameter to the <code>next_link</code> URL to
    ensure that appeals are stably sorted and that order persists when changes occur while working
    through a paginated list.
    <p />
    If the <code>last_modified</code> and <code>date_added</code> parameters are both specified, the
    sorting behavior is to list appeals based on when they were last modified.
    <p />

    Args:
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        sort_token (str | Unset):
        include_inactive (bool | Unset):
        appeal_id (list[str] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionAppealRead]
    """

    kwargs = _get_kwargs(
        date_added=date_added,
        last_modified=last_modified,
        sort_token=sort_token,
        include_inactive=include_inactive,
        appeal_id=appeal_id,
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
    sort_token: str | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    appeal_id: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | ApiCollectionAppealRead | None:
    """Appeal list

     Returns a paginated list of appeals.
    <p />
    The default sorting behavior is to list appeals in ascending order based on when they were created.
    <p />
    However, the <code>last_modified</code> parameter overrides the default sorting behavior to list
    appeals in ascending order based on when they were last modified. The <code>last_modified</code>
    parameter also adds the <code>sort_token</code> parameter to the <code>next_link</code> URL to
    ensure that appeals are stably sorted and that order persists when changes occur while working
    through a paginated list.
    <p />
    If the <code>last_modified</code> and <code>date_added</code> parameters are both specified, the
    sorting behavior is to list appeals based on when they were last modified.
    <p />

    Args:
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        sort_token (str | Unset):
        include_inactive (bool | Unset):
        appeal_id (list[str] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionAppealRead
    """

    return sync_detailed(
        client=client,
        date_added=date_added,
        last_modified=last_modified,
        sort_token=sort_token,
        include_inactive=include_inactive,
        appeal_id=appeal_id,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    appeal_id: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | ApiCollectionAppealRead]:
    """Appeal list

     Returns a paginated list of appeals.
    <p />
    The default sorting behavior is to list appeals in ascending order based on when they were created.
    <p />
    However, the <code>last_modified</code> parameter overrides the default sorting behavior to list
    appeals in ascending order based on when they were last modified. The <code>last_modified</code>
    parameter also adds the <code>sort_token</code> parameter to the <code>next_link</code> URL to
    ensure that appeals are stably sorted and that order persists when changes occur while working
    through a paginated list.
    <p />
    If the <code>last_modified</code> and <code>date_added</code> parameters are both specified, the
    sorting behavior is to list appeals based on when they were last modified.
    <p />

    Args:
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        sort_token (str | Unset):
        include_inactive (bool | Unset):
        appeal_id (list[str] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionAppealRead]
    """

    kwargs = _get_kwargs(
        date_added=date_added,
        last_modified=last_modified,
        sort_token=sort_token,
        include_inactive=include_inactive,
        appeal_id=appeal_id,
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
    sort_token: str | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    appeal_id: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | ApiCollectionAppealRead | None:
    """Appeal list

     Returns a paginated list of appeals.
    <p />
    The default sorting behavior is to list appeals in ascending order based on when they were created.
    <p />
    However, the <code>last_modified</code> parameter overrides the default sorting behavior to list
    appeals in ascending order based on when they were last modified. The <code>last_modified</code>
    parameter also adds the <code>sort_token</code> parameter to the <code>next_link</code> URL to
    ensure that appeals are stably sorted and that order persists when changes occur while working
    through a paginated list.
    <p />
    If the <code>last_modified</code> and <code>date_added</code> parameters are both specified, the
    sorting behavior is to list appeals based on when they were last modified.
    <p />

    Args:
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        sort_token (str | Unset):
        include_inactive (bool | Unset):
        appeal_id (list[str] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionAppealRead
    """

    return (
        await asyncio_detailed(
            client=client,
            date_added=date_added,
            last_modified=last_modified,
            sort_token=sort_token,
            include_inactive=include_inactive,
            appeal_id=appeal_id,
            limit=limit,
            offset=offset,
        )
    ).parsed
