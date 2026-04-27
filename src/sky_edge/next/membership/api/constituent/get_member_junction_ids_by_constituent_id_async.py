from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.get_member_junction_ids_by_constituent_id_async_sort_direction import (
    GetMemberJunctionIdsByConstituentIdAsyncSortDirection,
)
from ...models.membership_junction_ids_collection import MembershipJunctionIdsCollection
from ...models.problem_details import ProblemDetails


def _get_kwargs(
    constituent_id: str,
    *,
    sort_direction: GetMemberJunctionIdsByConstituentIdAsyncSortDirection
    | Unset = GetMemberJunctionIdsByConstituentIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_sort_direction: str | Unset = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sort_direction"] = json_sort_direction

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/constituents/{constituent_id}/membershipjunctionids".format(
            constituent_id=quote(str(constituent_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MembershipJunctionIdsCollection | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = MembershipJunctionIdsCollection.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ProblemDetails.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MembershipJunctionIdsCollection | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort_direction: GetMemberJunctionIdsByConstituentIdAsyncSortDirection
    | Unset = GetMemberJunctionIdsByConstituentIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Response[MembershipJunctionIdsCollection | ProblemDetails]:
    """Get membership junction IDs for a constituent. (PREVIEW)

     Return membership junction IDs by constituent ID

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        constituent_id (str):
        sort_direction (GetMemberJunctionIdsByConstituentIdAsyncSortDirection | Unset):  Default:
            GetMemberJunctionIdsByConstituentIdAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MembershipJunctionIdsCollection | ProblemDetails]
    """

    kwargs = _get_kwargs(
        constituent_id=constituent_id,
        sort_direction=sort_direction,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort_direction: GetMemberJunctionIdsByConstituentIdAsyncSortDirection
    | Unset = GetMemberJunctionIdsByConstituentIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> MembershipJunctionIdsCollection | ProblemDetails | None:
    """Get membership junction IDs for a constituent. (PREVIEW)

     Return membership junction IDs by constituent ID

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        constituent_id (str):
        sort_direction (GetMemberJunctionIdsByConstituentIdAsyncSortDirection | Unset):  Default:
            GetMemberJunctionIdsByConstituentIdAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MembershipJunctionIdsCollection | ProblemDetails
    """

    return sync_detailed(
        constituent_id=constituent_id,
        client=client,
        sort_direction=sort_direction,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort_direction: GetMemberJunctionIdsByConstituentIdAsyncSortDirection
    | Unset = GetMemberJunctionIdsByConstituentIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Response[MembershipJunctionIdsCollection | ProblemDetails]:
    """Get membership junction IDs for a constituent. (PREVIEW)

     Return membership junction IDs by constituent ID

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        constituent_id (str):
        sort_direction (GetMemberJunctionIdsByConstituentIdAsyncSortDirection | Unset):  Default:
            GetMemberJunctionIdsByConstituentIdAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MembershipJunctionIdsCollection | ProblemDetails]
    """

    kwargs = _get_kwargs(
        constituent_id=constituent_id,
        sort_direction=sort_direction,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort_direction: GetMemberJunctionIdsByConstituentIdAsyncSortDirection
    | Unset = GetMemberJunctionIdsByConstituentIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> MembershipJunctionIdsCollection | ProblemDetails | None:
    """Get membership junction IDs for a constituent. (PREVIEW)

     Return membership junction IDs by constituent ID

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        constituent_id (str):
        sort_direction (GetMemberJunctionIdsByConstituentIdAsyncSortDirection | Unset):  Default:
            GetMemberJunctionIdsByConstituentIdAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MembershipJunctionIdsCollection | ProblemDetails
    """

    return (
        await asyncio_detailed(
            constituent_id=constituent_id,
            client=client,
            sort_direction=sort_direction,
            limit=limit,
            offset=offset,
        )
    ).parsed
