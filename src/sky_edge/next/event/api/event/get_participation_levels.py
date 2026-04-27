from http import HTTPStatus
from typing import Any

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.participation_level_collection import ParticipationLevelCollection
from ...models.service_error import ServiceError


def _get_kwargs(
    *,
    include_inactive: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include_inactive"] = include_inactive

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/participationlevels",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ParticipationLevelCollection | list[ServiceError] | None:
    if response.status_code == 200:
        response_200 = ParticipationLevelCollection.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = []
        _response_403 = response.json()
        for response_403_item_data in _response_403:
            response_403_item = ServiceError.from_dict(response_403_item_data)

            response_403.append(response_403_item)

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ParticipationLevelCollection | list[ServiceError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_inactive: bool | Unset = UNSET,
) -> Response[ParticipationLevelCollection | list[ServiceError]]:
    """Get participation levels

     Returns a list of participation levels for all events. Participation levels describe a participant's
    involvement in an event, such as child participant or local business supporter.

    Args:
        include_inactive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ParticipationLevelCollection | list[ServiceError]]
    """

    kwargs = _get_kwargs(
        include_inactive=include_inactive,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    include_inactive: bool | Unset = UNSET,
) -> ParticipationLevelCollection | list[ServiceError] | None:
    """Get participation levels

     Returns a list of participation levels for all events. Participation levels describe a participant's
    involvement in an event, such as child participant or local business supporter.

    Args:
        include_inactive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ParticipationLevelCollection | list[ServiceError]
    """

    return sync_detailed(
        client=client,
        include_inactive=include_inactive,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_inactive: bool | Unset = UNSET,
) -> Response[ParticipationLevelCollection | list[ServiceError]]:
    """Get participation levels

     Returns a list of participation levels for all events. Participation levels describe a participant's
    involvement in an event, such as child participant or local business supporter.

    Args:
        include_inactive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ParticipationLevelCollection | list[ServiceError]]
    """

    kwargs = _get_kwargs(
        include_inactive=include_inactive,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    include_inactive: bool | Unset = UNSET,
) -> ParticipationLevelCollection | list[ServiceError] | None:
    """Get participation levels

     Returns a list of participation levels for all events. Participation levels describe a participant's
    involvement in an event, such as child participant or local business supporter.

    Args:
        include_inactive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ParticipationLevelCollection | list[ServiceError]
    """

    return (
        await asyncio_detailed(
            client=client,
            include_inactive=include_inactive,
        )
    ).parsed
