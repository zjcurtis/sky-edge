from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.bad_request_400_response_types import BadRequest400ResponseTypes
from ...models.get_linked_gifts_by_member_junction_id_async_linked_gift_sort_fields import (
    GetLinkedGiftsByMemberJunctionIdAsyncLinkedGiftSortFields,
)
from ...models.get_linked_gifts_by_member_junction_id_async_sort_direction import (
    GetLinkedGiftsByMemberJunctionIdAsyncSortDirection,
)
from ...models.linked_gifts_collection import LinkedGiftsCollection
from ...models.problem_details import ProblemDetails


def _get_kwargs(
    member_junction_id: str,
    *,
    sort_by: GetLinkedGiftsByMemberJunctionIdAsyncLinkedGiftSortFields
    | Unset = GetLinkedGiftsByMemberJunctionIdAsyncLinkedGiftSortFields.GIFTDATE,
    sort_direction: GetLinkedGiftsByMemberJunctionIdAsyncSortDirection
    | Unset = GetLinkedGiftsByMemberJunctionIdAsyncSortDirection.ASCENDING,
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
        "url": "/v1/memberships/{member_junction_id}/linkedgifts".format(
            member_junction_id=quote(str(member_junction_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BadRequest400ResponseTypes | LinkedGiftsCollection | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = LinkedGiftsCollection.from_dict(response.json())

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
) -> Response[
    Any | BadRequest400ResponseTypes | LinkedGiftsCollection | ProblemDetails
]:
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
    sort_by: GetLinkedGiftsByMemberJunctionIdAsyncLinkedGiftSortFields
    | Unset = GetLinkedGiftsByMemberJunctionIdAsyncLinkedGiftSortFields.GIFTDATE,
    sort_direction: GetLinkedGiftsByMemberJunctionIdAsyncSortDirection
    | Unset = GetLinkedGiftsByMemberJunctionIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Response[
    Any | BadRequest400ResponseTypes | LinkedGiftsCollection | ProblemDetails
]:
    """Get linked gifts for membership

     Returned linked gifts by joint membership ID

    Args:
        member_junction_id (str):
        sort_by (GetLinkedGiftsByMemberJunctionIdAsyncLinkedGiftSortFields | Unset):  Default:
            GetLinkedGiftsByMemberJunctionIdAsyncLinkedGiftSortFields.GIFTDATE.
        sort_direction (GetLinkedGiftsByMemberJunctionIdAsyncSortDirection | Unset):  Default:
            GetLinkedGiftsByMemberJunctionIdAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadRequest400ResponseTypes | LinkedGiftsCollection | ProblemDetails]
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
    sort_by: GetLinkedGiftsByMemberJunctionIdAsyncLinkedGiftSortFields
    | Unset = GetLinkedGiftsByMemberJunctionIdAsyncLinkedGiftSortFields.GIFTDATE,
    sort_direction: GetLinkedGiftsByMemberJunctionIdAsyncSortDirection
    | Unset = GetLinkedGiftsByMemberJunctionIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Any | BadRequest400ResponseTypes | LinkedGiftsCollection | ProblemDetails | None:
    """Get linked gifts for membership

     Returned linked gifts by joint membership ID

    Args:
        member_junction_id (str):
        sort_by (GetLinkedGiftsByMemberJunctionIdAsyncLinkedGiftSortFields | Unset):  Default:
            GetLinkedGiftsByMemberJunctionIdAsyncLinkedGiftSortFields.GIFTDATE.
        sort_direction (GetLinkedGiftsByMemberJunctionIdAsyncSortDirection | Unset):  Default:
            GetLinkedGiftsByMemberJunctionIdAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadRequest400ResponseTypes | LinkedGiftsCollection | ProblemDetails
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
    sort_by: GetLinkedGiftsByMemberJunctionIdAsyncLinkedGiftSortFields
    | Unset = GetLinkedGiftsByMemberJunctionIdAsyncLinkedGiftSortFields.GIFTDATE,
    sort_direction: GetLinkedGiftsByMemberJunctionIdAsyncSortDirection
    | Unset = GetLinkedGiftsByMemberJunctionIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Response[
    Any | BadRequest400ResponseTypes | LinkedGiftsCollection | ProblemDetails
]:
    """Get linked gifts for membership

     Returned linked gifts by joint membership ID

    Args:
        member_junction_id (str):
        sort_by (GetLinkedGiftsByMemberJunctionIdAsyncLinkedGiftSortFields | Unset):  Default:
            GetLinkedGiftsByMemberJunctionIdAsyncLinkedGiftSortFields.GIFTDATE.
        sort_direction (GetLinkedGiftsByMemberJunctionIdAsyncSortDirection | Unset):  Default:
            GetLinkedGiftsByMemberJunctionIdAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadRequest400ResponseTypes | LinkedGiftsCollection | ProblemDetails]
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
    sort_by: GetLinkedGiftsByMemberJunctionIdAsyncLinkedGiftSortFields
    | Unset = GetLinkedGiftsByMemberJunctionIdAsyncLinkedGiftSortFields.GIFTDATE,
    sort_direction: GetLinkedGiftsByMemberJunctionIdAsyncSortDirection
    | Unset = GetLinkedGiftsByMemberJunctionIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Any | BadRequest400ResponseTypes | LinkedGiftsCollection | ProblemDetails | None:
    """Get linked gifts for membership

     Returned linked gifts by joint membership ID

    Args:
        member_junction_id (str):
        sort_by (GetLinkedGiftsByMemberJunctionIdAsyncLinkedGiftSortFields | Unset):  Default:
            GetLinkedGiftsByMemberJunctionIdAsyncLinkedGiftSortFields.GIFTDATE.
        sort_direction (GetLinkedGiftsByMemberJunctionIdAsyncSortDirection | Unset):  Default:
            GetLinkedGiftsByMemberJunctionIdAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadRequest400ResponseTypes | LinkedGiftsCollection | ProblemDetails
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
