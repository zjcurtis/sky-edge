import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.api_collection_of_membership_read import ApiCollectionOfMembershipRead


def _get_kwargs(
    *,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    sort_token: str | Unset = UNSET,
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

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/memberships",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiCollectionOfMembershipRead | None:
    if response.status_code == 200:
        response_200 = ApiCollectionOfMembershipRead.from_dict(response.json())

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
) -> Response[Any | ApiCollectionOfMembershipRead]:
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | ApiCollectionOfMembershipRead]:
    """Membership list (All constituents)

     Returns a paginated list of memberships.
    <p />
    The default sorting behavior is to list memberships in ascending order based on when they were
    created.
    <p />
    However, the <code>last_modified</code> parameter overrides the default sorting behavior to list
    memberships in ascending order based on when they were last modified. The <code>last_modified</code>
    parameter also adds the <code>sort_token</code> parameter to the <code>next_link</code> URL to
    ensure that memberships are stably sorted and that order persists when changes occur while working
    through a paginated list.
    <p />
    If the <code>last_modified</code> and <code>date_added</code> parameters are both specified, the
    sorting behavior is to list memberships based on when they were last modified.
    <p />

    Args:
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        sort_token (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOfMembershipRead]
    """

    kwargs = _get_kwargs(
        date_added=date_added,
        last_modified=last_modified,
        sort_token=sort_token,
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | ApiCollectionOfMembershipRead | None:
    """Membership list (All constituents)

     Returns a paginated list of memberships.
    <p />
    The default sorting behavior is to list memberships in ascending order based on when they were
    created.
    <p />
    However, the <code>last_modified</code> parameter overrides the default sorting behavior to list
    memberships in ascending order based on when they were last modified. The <code>last_modified</code>
    parameter also adds the <code>sort_token</code> parameter to the <code>next_link</code> URL to
    ensure that memberships are stably sorted and that order persists when changes occur while working
    through a paginated list.
    <p />
    If the <code>last_modified</code> and <code>date_added</code> parameters are both specified, the
    sorting behavior is to list memberships based on when they were last modified.
    <p />

    Args:
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        sort_token (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOfMembershipRead
    """

    return sync_detailed(
        client=client,
        date_added=date_added,
        last_modified=last_modified,
        sort_token=sort_token,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | ApiCollectionOfMembershipRead]:
    """Membership list (All constituents)

     Returns a paginated list of memberships.
    <p />
    The default sorting behavior is to list memberships in ascending order based on when they were
    created.
    <p />
    However, the <code>last_modified</code> parameter overrides the default sorting behavior to list
    memberships in ascending order based on when they were last modified. The <code>last_modified</code>
    parameter also adds the <code>sort_token</code> parameter to the <code>next_link</code> URL to
    ensure that memberships are stably sorted and that order persists when changes occur while working
    through a paginated list.
    <p />
    If the <code>last_modified</code> and <code>date_added</code> parameters are both specified, the
    sorting behavior is to list memberships based on when they were last modified.
    <p />

    Args:
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        sort_token (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOfMembershipRead]
    """

    kwargs = _get_kwargs(
        date_added=date_added,
        last_modified=last_modified,
        sort_token=sort_token,
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | ApiCollectionOfMembershipRead | None:
    """Membership list (All constituents)

     Returns a paginated list of memberships.
    <p />
    The default sorting behavior is to list memberships in ascending order based on when they were
    created.
    <p />
    However, the <code>last_modified</code> parameter overrides the default sorting behavior to list
    memberships in ascending order based on when they were last modified. The <code>last_modified</code>
    parameter also adds the <code>sort_token</code> parameter to the <code>next_link</code> URL to
    ensure that memberships are stably sorted and that order persists when changes occur while working
    through a paginated list.
    <p />
    If the <code>last_modified</code> and <code>date_added</code> parameters are both specified, the
    sorting behavior is to list memberships based on when they were last modified.
    <p />

    Args:
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        sort_token (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOfMembershipRead
    """

    return (
        await asyncio_detailed(
            client=client,
            date_added=date_added,
            last_modified=last_modified,
            sort_token=sort_token,
            limit=limit,
            offset=offset,
        )
    ).parsed
