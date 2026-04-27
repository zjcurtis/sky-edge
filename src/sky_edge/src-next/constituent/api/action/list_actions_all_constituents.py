import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_collection_of_action_read import ApiCollectionOfActionRead
from ...models.list_actions_all_constituents_computed_status_item import ListActionsAllConstituentsComputedStatusItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    computed_status: list[ListActionsAllConstituentsComputedStatusItem] | Unset = UNSET,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    status_code: list[str] | Unset = UNSET,
    list_id: str | Unset = UNSET,
    continuation_token: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_computed_status: list[str] | Unset = UNSET
    if not isinstance(computed_status, Unset):
        json_computed_status = []
        for computed_status_item_data in computed_status:
            computed_status_item = computed_status_item_data.value
            json_computed_status.append(computed_status_item)

    params["computed_status"] = json_computed_status

    json_date_added: str | Unset = UNSET
    if not isinstance(date_added, Unset):
        json_date_added = date_added.isoformat()
    params["date_added"] = json_date_added

    json_last_modified: str | Unset = UNSET
    if not isinstance(last_modified, Unset):
        json_last_modified = last_modified.isoformat()
    params["last_modified"] = json_last_modified

    params["sort_token"] = sort_token

    json_status_code: list[str] | Unset = UNSET
    if not isinstance(status_code, Unset):
        json_status_code = status_code

    params["status_code"] = json_status_code

    params["list_id"] = list_id

    params["continuation_token"] = continuation_token

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/actions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiCollectionOfActionRead | None:
    if response.status_code == 200:
        response_200 = ApiCollectionOfActionRead.from_dict(response.json())

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
) -> Response[Any | ApiCollectionOfActionRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    computed_status: list[ListActionsAllConstituentsComputedStatusItem] | Unset = UNSET,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    status_code: list[str] | Unset = UNSET,
    list_id: str | Unset = UNSET,
    continuation_token: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[Any | ApiCollectionOfActionRead]:
    """Action list (All constituents)

     Returns a paginated list of actions.
    <p />
    The default sorting behavior is to list actions in ascending order based on when they were created.
    <p />
    However, the <code>last_modified</code> parameter overrides the default sorting behavior to list
    actions in ascending order based on when they were last modified. The <code>last_modified</code>
    parameter also adds the <code>sort_token</code> parameter to the <code>next_link</code> URL to
    ensure that actions are stably sorted and that order persists when changes occur while working
    through a paginated list.
    <p />
    If the <code>last_modified</code> and <code>date_added</code> parameters are both specified, the
    sorting behavior is to list actions based on when they were last modified.
    <p />

    Args:
        computed_status (list[ListActionsAllConstituentsComputedStatusItem] | Unset):
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        sort_token (str | Unset):
        status_code (list[str] | Unset):
        list_id (str | Unset):
        continuation_token (str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOfActionRead]
    """

    kwargs = _get_kwargs(
        computed_status=computed_status,
        date_added=date_added,
        last_modified=last_modified,
        sort_token=sort_token,
        status_code=status_code,
        list_id=list_id,
        continuation_token=continuation_token,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    computed_status: list[ListActionsAllConstituentsComputedStatusItem] | Unset = UNSET,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    status_code: list[str] | Unset = UNSET,
    list_id: str | Unset = UNSET,
    continuation_token: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Any | ApiCollectionOfActionRead | None:
    """Action list (All constituents)

     Returns a paginated list of actions.
    <p />
    The default sorting behavior is to list actions in ascending order based on when they were created.
    <p />
    However, the <code>last_modified</code> parameter overrides the default sorting behavior to list
    actions in ascending order based on when they were last modified. The <code>last_modified</code>
    parameter also adds the <code>sort_token</code> parameter to the <code>next_link</code> URL to
    ensure that actions are stably sorted and that order persists when changes occur while working
    through a paginated list.
    <p />
    If the <code>last_modified</code> and <code>date_added</code> parameters are both specified, the
    sorting behavior is to list actions based on when they were last modified.
    <p />

    Args:
        computed_status (list[ListActionsAllConstituentsComputedStatusItem] | Unset):
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        sort_token (str | Unset):
        status_code (list[str] | Unset):
        list_id (str | Unset):
        continuation_token (str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOfActionRead
    """

    return sync_detailed(
        client=client,
        computed_status=computed_status,
        date_added=date_added,
        last_modified=last_modified,
        sort_token=sort_token,
        status_code=status_code,
        list_id=list_id,
        continuation_token=continuation_token,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    computed_status: list[ListActionsAllConstituentsComputedStatusItem] | Unset = UNSET,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    status_code: list[str] | Unset = UNSET,
    list_id: str | Unset = UNSET,
    continuation_token: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[Any | ApiCollectionOfActionRead]:
    """Action list (All constituents)

     Returns a paginated list of actions.
    <p />
    The default sorting behavior is to list actions in ascending order based on when they were created.
    <p />
    However, the <code>last_modified</code> parameter overrides the default sorting behavior to list
    actions in ascending order based on when they were last modified. The <code>last_modified</code>
    parameter also adds the <code>sort_token</code> parameter to the <code>next_link</code> URL to
    ensure that actions are stably sorted and that order persists when changes occur while working
    through a paginated list.
    <p />
    If the <code>last_modified</code> and <code>date_added</code> parameters are both specified, the
    sorting behavior is to list actions based on when they were last modified.
    <p />

    Args:
        computed_status (list[ListActionsAllConstituentsComputedStatusItem] | Unset):
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        sort_token (str | Unset):
        status_code (list[str] | Unset):
        list_id (str | Unset):
        continuation_token (str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOfActionRead]
    """

    kwargs = _get_kwargs(
        computed_status=computed_status,
        date_added=date_added,
        last_modified=last_modified,
        sort_token=sort_token,
        status_code=status_code,
        list_id=list_id,
        continuation_token=continuation_token,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    computed_status: list[ListActionsAllConstituentsComputedStatusItem] | Unset = UNSET,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    status_code: list[str] | Unset = UNSET,
    list_id: str | Unset = UNSET,
    continuation_token: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Any | ApiCollectionOfActionRead | None:
    """Action list (All constituents)

     Returns a paginated list of actions.
    <p />
    The default sorting behavior is to list actions in ascending order based on when they were created.
    <p />
    However, the <code>last_modified</code> parameter overrides the default sorting behavior to list
    actions in ascending order based on when they were last modified. The <code>last_modified</code>
    parameter also adds the <code>sort_token</code> parameter to the <code>next_link</code> URL to
    ensure that actions are stably sorted and that order persists when changes occur while working
    through a paginated list.
    <p />
    If the <code>last_modified</code> and <code>date_added</code> parameters are both specified, the
    sorting behavior is to list actions based on when they were last modified.
    <p />

    Args:
        computed_status (list[ListActionsAllConstituentsComputedStatusItem] | Unset):
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        sort_token (str | Unset):
        status_code (list[str] | Unset):
        list_id (str | Unset):
        continuation_token (str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOfActionRead
    """

    return (
        await asyncio_detailed(
            client=client,
            computed_status=computed_status,
            date_added=date_added,
            last_modified=last_modified,
            sort_token=sort_token,
            status_code=status_code,
            list_id=list_id,
            continuation_token=continuation_token,
            offset=offset,
            limit=limit,
        )
    ).parsed
