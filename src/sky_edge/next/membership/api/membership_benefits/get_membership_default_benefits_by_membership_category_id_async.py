from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.bad_request_400_response_types import BadRequest400ResponseTypes
from ...models.get_membership_default_benefits_by_membership_category_id_async_membership_default_benefits_sort_fields import (
    GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncMembershipDefaultBenefitsSortFields,
)
from ...models.get_membership_default_benefits_by_membership_category_id_async_sort_direction import (
    GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncSortDirection,
)
from ...models.membership_benefit_collection import MembershipBenefitCollection
from ...models.problem_details import ProblemDetails


def _get_kwargs(
    membership_category_id: str,
    *,
    sort_by: GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncMembershipDefaultBenefitsSortFields
    | Unset = GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncMembershipDefaultBenefitsSortFields.SEQUENCE,
    sort_direction: GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncSortDirection
    | Unset = GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncSortDirection.ASCENDING,
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
        "url": "/v1/memberships/categories/{membership_category_id}/benefits".format(
            membership_category_id=quote(str(membership_category_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | BadRequest400ResponseTypes
    | MembershipBenefitCollection
    | ProblemDetails
    | None
):
    if response.status_code == 200:
        response_200 = MembershipBenefitCollection.from_dict(response.json())

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
    Any | BadRequest400ResponseTypes | MembershipBenefitCollection | ProblemDetails
]:
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
    sort_by: GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncMembershipDefaultBenefitsSortFields
    | Unset = GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncMembershipDefaultBenefitsSortFields.SEQUENCE,
    sort_direction: GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncSortDirection
    | Unset = GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Response[
    Any | BadRequest400ResponseTypes | MembershipBenefitCollection | ProblemDetails
]:
    """Get membership default benefits list (PREVIEW)

     Returns the membership default benefits list.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        membership_category_id (str):
        sort_by (GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncMembershipDefaultBenefitsS
            ortFields | Unset):  Default: GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncMembe
            rshipDefaultBenefitsSortFields.SEQUENCE.
        sort_direction (GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncSortDirection |
            Unset):  Default:
            GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadRequest400ResponseTypes | MembershipBenefitCollection | ProblemDetails]
    """

    kwargs = _get_kwargs(
        membership_category_id=membership_category_id,
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
    membership_category_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort_by: GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncMembershipDefaultBenefitsSortFields
    | Unset = GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncMembershipDefaultBenefitsSortFields.SEQUENCE,
    sort_direction: GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncSortDirection
    | Unset = GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> (
    Any
    | BadRequest400ResponseTypes
    | MembershipBenefitCollection
    | ProblemDetails
    | None
):
    """Get membership default benefits list (PREVIEW)

     Returns the membership default benefits list.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        membership_category_id (str):
        sort_by (GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncMembershipDefaultBenefitsS
            ortFields | Unset):  Default: GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncMembe
            rshipDefaultBenefitsSortFields.SEQUENCE.
        sort_direction (GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncSortDirection |
            Unset):  Default:
            GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadRequest400ResponseTypes | MembershipBenefitCollection | ProblemDetails
    """

    return sync_detailed(
        membership_category_id=membership_category_id,
        client=client,
        sort_by=sort_by,
        sort_direction=sort_direction,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    membership_category_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort_by: GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncMembershipDefaultBenefitsSortFields
    | Unset = GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncMembershipDefaultBenefitsSortFields.SEQUENCE,
    sort_direction: GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncSortDirection
    | Unset = GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Response[
    Any | BadRequest400ResponseTypes | MembershipBenefitCollection | ProblemDetails
]:
    """Get membership default benefits list (PREVIEW)

     Returns the membership default benefits list.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        membership_category_id (str):
        sort_by (GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncMembershipDefaultBenefitsS
            ortFields | Unset):  Default: GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncMembe
            rshipDefaultBenefitsSortFields.SEQUENCE.
        sort_direction (GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncSortDirection |
            Unset):  Default:
            GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadRequest400ResponseTypes | MembershipBenefitCollection | ProblemDetails]
    """

    kwargs = _get_kwargs(
        membership_category_id=membership_category_id,
        sort_by=sort_by,
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
    sort_by: GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncMembershipDefaultBenefitsSortFields
    | Unset = GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncMembershipDefaultBenefitsSortFields.SEQUENCE,
    sort_direction: GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncSortDirection
    | Unset = GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncSortDirection.ASCENDING,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> (
    Any
    | BadRequest400ResponseTypes
    | MembershipBenefitCollection
    | ProblemDetails
    | None
):
    """Get membership default benefits list (PREVIEW)

     Returns the membership default benefits list.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        membership_category_id (str):
        sort_by (GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncMembershipDefaultBenefitsS
            ortFields | Unset):  Default: GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncMembe
            rshipDefaultBenefitsSortFields.SEQUENCE.
        sort_direction (GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncSortDirection |
            Unset):  Default:
            GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncSortDirection.ASCENDING.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadRequest400ResponseTypes | MembershipBenefitCollection | ProblemDetails
    """

    return (
        await asyncio_detailed(
            membership_category_id=membership_category_id,
            client=client,
            sort_by=sort_by,
            sort_direction=sort_direction,
            limit=limit,
            offset=offset,
        )
    ).parsed
