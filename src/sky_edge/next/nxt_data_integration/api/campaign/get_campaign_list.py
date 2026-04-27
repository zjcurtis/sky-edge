from http import HTTPStatus
from typing import Any, cast

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.campaign_collection import CampaignCollection


def _get_kwargs(
    *,
    campaign_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["campaign_id"] = campaign_id

    params["description"] = description

    params["include_inactive"] = include_inactive

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/re/campaigns",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CampaignCollection | None:
    if response.status_code == 200:
        response_200 = CampaignCollection.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CampaignCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    campaign_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | CampaignCollection]:
    """Get campaign list

     Returns a list of campaigns.

    Args:
        campaign_id (str | Unset):
        description (str | Unset):
        include_inactive (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CampaignCollection]
    """

    kwargs = _get_kwargs(
        campaign_id=campaign_id,
        description=description,
        include_inactive=include_inactive,
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
    campaign_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | CampaignCollection | None:
    """Get campaign list

     Returns a list of campaigns.

    Args:
        campaign_id (str | Unset):
        description (str | Unset):
        include_inactive (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CampaignCollection
    """

    return sync_detailed(
        client=client,
        campaign_id=campaign_id,
        description=description,
        include_inactive=include_inactive,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    campaign_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | CampaignCollection]:
    """Get campaign list

     Returns a list of campaigns.

    Args:
        campaign_id (str | Unset):
        description (str | Unset):
        include_inactive (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CampaignCollection]
    """

    kwargs = _get_kwargs(
        campaign_id=campaign_id,
        description=description,
        include_inactive=include_inactive,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    campaign_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | CampaignCollection | None:
    """Get campaign list

     Returns a list of campaigns.

    Args:
        campaign_id (str | Unset):
        description (str | Unset):
        include_inactive (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CampaignCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            campaign_id=campaign_id,
            description=description,
            include_inactive=include_inactive,
            limit=limit,
            offset=offset,
        )
    ).parsed
