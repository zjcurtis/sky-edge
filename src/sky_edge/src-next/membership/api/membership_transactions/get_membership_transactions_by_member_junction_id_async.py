from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request_400_response_types import BadRequest400ResponseTypes
from ...models.get_membership_transactions_by_member_junction_id_async_membership_history_sort_fields import (
    GetMembershipTransactionsByMemberJunctionIdAsyncMembershipHistorySortFields,
)
from ...models.get_membership_transactions_by_member_junction_id_async_sort_direction import (
    GetMembershipTransactionsByMemberJunctionIdAsyncSortDirection,
)
from ...models.membership_history_collection import MembershipHistoryCollection
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    member_junction_id: str,
    *,
    sort_by: GetMembershipTransactionsByMemberJunctionIdAsyncMembershipHistorySortFields
    | Unset = GetMembershipTransactionsByMemberJunctionIdAsyncMembershipHistorySortFields.ACTIVITYDATE,
    sort_direction: GetMembershipTransactionsByMemberJunctionIdAsyncSortDirection
    | Unset = GetMembershipTransactionsByMemberJunctionIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

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
        "url": "/v1/memberships/{member_junction_id}/transactions".format(
            member_junction_id=quote(str(member_junction_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BadRequest400ResponseTypes | MembershipHistoryCollection | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = MembershipHistoryCollection.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = BadRequest400ResponseTypes.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | BadRequest400ResponseTypes | MembershipHistoryCollection | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    member_junction_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort_by: GetMembershipTransactionsByMemberJunctionIdAsyncMembershipHistorySortFields
    | Unset = GetMembershipTransactionsByMemberJunctionIdAsyncMembershipHistorySortFields.ACTIVITYDATE,
    sort_direction: GetMembershipTransactionsByMemberJunctionIdAsyncSortDirection
    | Unset = GetMembershipTransactionsByMemberJunctionIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Response[Any | BadRequest400ResponseTypes | MembershipHistoryCollection | ProblemDetails]:
    """Get membership history list

     Returns the membership history list by member junction ID.

    Args:
        member_junction_id (str):
        sort_by (GetMembershipTransactionsByMemberJunctionIdAsyncMembershipHistorySortFields |
            Unset):  Default:
            GetMembershipTransactionsByMemberJunctionIdAsyncMembershipHistorySortFields.ACTIVITYDATE.
        sort_direction (GetMembershipTransactionsByMemberJunctionIdAsyncSortDirection | Unset):
            Default: GetMembershipTransactionsByMemberJunctionIdAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadRequest400ResponseTypes | MembershipHistoryCollection | ProblemDetails]
    """

    kwargs = _get_kwargs(
        member_junction_id=member_junction_id,
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
    member_junction_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort_by: GetMembershipTransactionsByMemberJunctionIdAsyncMembershipHistorySortFields
    | Unset = GetMembershipTransactionsByMemberJunctionIdAsyncMembershipHistorySortFields.ACTIVITYDATE,
    sort_direction: GetMembershipTransactionsByMemberJunctionIdAsyncSortDirection
    | Unset = GetMembershipTransactionsByMemberJunctionIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Any | BadRequest400ResponseTypes | MembershipHistoryCollection | ProblemDetails | None:
    """Get membership history list

     Returns the membership history list by member junction ID.

    Args:
        member_junction_id (str):
        sort_by (GetMembershipTransactionsByMemberJunctionIdAsyncMembershipHistorySortFields |
            Unset):  Default:
            GetMembershipTransactionsByMemberJunctionIdAsyncMembershipHistorySortFields.ACTIVITYDATE.
        sort_direction (GetMembershipTransactionsByMemberJunctionIdAsyncSortDirection | Unset):
            Default: GetMembershipTransactionsByMemberJunctionIdAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadRequest400ResponseTypes | MembershipHistoryCollection | ProblemDetails
    """

    return sync_detailed(
        member_junction_id=member_junction_id,
        client=client,
        sort_by=sort_by,
        sort_direction=sort_direction,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    member_junction_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort_by: GetMembershipTransactionsByMemberJunctionIdAsyncMembershipHistorySortFields
    | Unset = GetMembershipTransactionsByMemberJunctionIdAsyncMembershipHistorySortFields.ACTIVITYDATE,
    sort_direction: GetMembershipTransactionsByMemberJunctionIdAsyncSortDirection
    | Unset = GetMembershipTransactionsByMemberJunctionIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Response[Any | BadRequest400ResponseTypes | MembershipHistoryCollection | ProblemDetails]:
    """Get membership history list

     Returns the membership history list by member junction ID.

    Args:
        member_junction_id (str):
        sort_by (GetMembershipTransactionsByMemberJunctionIdAsyncMembershipHistorySortFields |
            Unset):  Default:
            GetMembershipTransactionsByMemberJunctionIdAsyncMembershipHistorySortFields.ACTIVITYDATE.
        sort_direction (GetMembershipTransactionsByMemberJunctionIdAsyncSortDirection | Unset):
            Default: GetMembershipTransactionsByMemberJunctionIdAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadRequest400ResponseTypes | MembershipHistoryCollection | ProblemDetails]
    """

    kwargs = _get_kwargs(
        member_junction_id=member_junction_id,
        sort_by=sort_by,
        sort_direction=sort_direction,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    member_junction_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort_by: GetMembershipTransactionsByMemberJunctionIdAsyncMembershipHistorySortFields
    | Unset = GetMembershipTransactionsByMemberJunctionIdAsyncMembershipHistorySortFields.ACTIVITYDATE,
    sort_direction: GetMembershipTransactionsByMemberJunctionIdAsyncSortDirection
    | Unset = GetMembershipTransactionsByMemberJunctionIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Any | BadRequest400ResponseTypes | MembershipHistoryCollection | ProblemDetails | None:
    """Get membership history list

     Returns the membership history list by member junction ID.

    Args:
        member_junction_id (str):
        sort_by (GetMembershipTransactionsByMemberJunctionIdAsyncMembershipHistorySortFields |
            Unset):  Default:
            GetMembershipTransactionsByMemberJunctionIdAsyncMembershipHistorySortFields.ACTIVITYDATE.
        sort_direction (GetMembershipTransactionsByMemberJunctionIdAsyncSortDirection | Unset):
            Default: GetMembershipTransactionsByMemberJunctionIdAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadRequest400ResponseTypes | MembershipHistoryCollection | ProblemDetails
    """

    return (
        await asyncio_detailed(
            member_junction_id=member_junction_id,
            client=client,
            sort_by=sort_by,
            sort_direction=sort_direction,
            limit=limit,
            offset=offset,
        )
    ).parsed
