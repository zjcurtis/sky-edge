from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.available_relationship_list_response import AvailableRelationshipListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    gift_id: str,
    *,
    offset: int | Unset = 0,
    limit: int | Unset = 500,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/gifts/{gift_id}/plannedgift/relationships/available".format(
            gift_id=quote(str(gift_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AvailableRelationshipListResponse | None:
    if response.status_code == 200:
        response_200 = AvailableRelationshipListResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AvailableRelationshipListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 500,
) -> Response[AvailableRelationshipListResponse]:
    """Get available relationships for a planned gift. (PREVIEW)

     Returns a paginated list of available relationships across all 4 types
    (Individual, Organization, Financial, Education) for the constituent
    associated with the specified planned gift. Each relationship includes
    flags indicating whether it is already added as a gift relationship or beneficiary.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 500.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailableRelationshipListResponse]
    """

    kwargs = _get_kwargs(
        gift_id=gift_id,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 500,
) -> AvailableRelationshipListResponse | None:
    """Get available relationships for a planned gift. (PREVIEW)

     Returns a paginated list of available relationships across all 4 types
    (Individual, Organization, Financial, Education) for the constituent
    associated with the specified planned gift. Each relationship includes
    flags indicating whether it is already added as a gift relationship or beneficiary.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 500.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AvailableRelationshipListResponse
    """

    return sync_detailed(
        gift_id=gift_id,
        client=client,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 500,
) -> Response[AvailableRelationshipListResponse]:
    """Get available relationships for a planned gift. (PREVIEW)

     Returns a paginated list of available relationships across all 4 types
    (Individual, Organization, Financial, Education) for the constituent
    associated with the specified planned gift. Each relationship includes
    flags indicating whether it is already added as a gift relationship or beneficiary.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 500.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailableRelationshipListResponse]
    """

    kwargs = _get_kwargs(
        gift_id=gift_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 500,
) -> AvailableRelationshipListResponse | None:
    """Get available relationships for a planned gift. (PREVIEW)

     Returns a paginated list of available relationships across all 4 types
    (Individual, Organization, Financial, Education) for the constituent
    associated with the specified planned gift. Each relationship includes
    flags indicating whether it is already added as a gift relationship or beneficiary.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 500.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AvailableRelationshipListResponse
    """

    return (
        await asyncio_detailed(
            gift_id=gift_id,
            client=client,
            offset=offset,
            limit=limit,
        )
    ).parsed
