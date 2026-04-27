import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.constituent_event_participation_collection import ConstituentEventParticipationCollection
from ...models.get_constituent_event_participation_invitation_status_item import (
    GetConstituentEventParticipationInvitationStatusItem,
)
from ...models.get_constituent_event_participation_rsvp_status_item import (
    GetConstituentEventParticipationRsvpStatusItem,
)
from ...models.service_error import ServiceError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    constituent_id: str,
    *,
    search_text: str | Unset = UNSET,
    start_date_from: datetime.date | Unset = UNSET,
    start_date_to: datetime.date | Unset = UNSET,
    invitation_status: list[GetConstituentEventParticipationInvitationStatusItem] | Unset = UNSET,
    rsvp_status: list[GetConstituentEventParticipationRsvpStatusItem] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["search_text"] = search_text

    json_start_date_from: str | Unset = UNSET
    if not isinstance(start_date_from, Unset):
        json_start_date_from = start_date_from.isoformat()
    params["start_date_from"] = json_start_date_from

    json_start_date_to: str | Unset = UNSET
    if not isinstance(start_date_to, Unset):
        json_start_date_to = start_date_to.isoformat()
    params["start_date_to"] = json_start_date_to

    json_invitation_status: list[str] | Unset = UNSET
    if not isinstance(invitation_status, Unset):
        json_invitation_status = []
        for invitation_status_item_data in invitation_status:
            invitation_status_item = invitation_status_item_data.value
            json_invitation_status.append(invitation_status_item)

    params["invitation_status"] = json_invitation_status

    json_rsvp_status: list[str] | Unset = UNSET
    if not isinstance(rsvp_status, Unset):
        json_rsvp_status = []
        for rsvp_status_item_data in rsvp_status:
            rsvp_status_item = rsvp_status_item_data.value
            json_rsvp_status.append(rsvp_status_item)

    params["rsvp_status"] = json_rsvp_status

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/constituents/{constituent_id}/eventparticipation".format(
            constituent_id=quote(str(constituent_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConstituentEventParticipationCollection | list[ServiceError] | None:
    if response.status_code == 200:
        response_200 = ConstituentEventParticipationCollection.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ServiceError.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400

    if response.status_code == 403:
        response_403 = []
        _response_403 = response.json()
        for response_403_item_data in _response_403:
            response_403_item = ServiceError.from_dict(response_403_item_data)

            response_403.append(response_403_item)

        return response_403

    if response.status_code == 404:
        response_404 = []
        _response_404 = response.json()
        for response_404_item_data in _response_404:
            response_404_item = ServiceError.from_dict(response_404_item_data)

            response_404.append(response_404_item)

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ConstituentEventParticipationCollection | list[ServiceError]]:
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
    search_text: str | Unset = UNSET,
    start_date_from: datetime.date | Unset = UNSET,
    start_date_to: datetime.date | Unset = UNSET,
    invitation_status: list[GetConstituentEventParticipationInvitationStatusItem] | Unset = UNSET,
    rsvp_status: list[GetConstituentEventParticipationRsvpStatusItem] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[ConstituentEventParticipationCollection | list[ServiceError]]:
    """Get a constituent's event participation (PREVIEW)

     Returns a constituent's event participation.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        constituent_id (str):
        search_text (str | Unset):
        start_date_from (datetime.date | Unset):
        start_date_to (datetime.date | Unset):
        invitation_status (list[GetConstituentEventParticipationInvitationStatusItem] | Unset):
        rsvp_status (list[GetConstituentEventParticipationRsvpStatusItem] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConstituentEventParticipationCollection | list[ServiceError]]
    """

    kwargs = _get_kwargs(
        constituent_id=constituent_id,
        search_text=search_text,
        start_date_from=start_date_from,
        start_date_to=start_date_to,
        invitation_status=invitation_status,
        rsvp_status=rsvp_status,
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
    search_text: str | Unset = UNSET,
    start_date_from: datetime.date | Unset = UNSET,
    start_date_to: datetime.date | Unset = UNSET,
    invitation_status: list[GetConstituentEventParticipationInvitationStatusItem] | Unset = UNSET,
    rsvp_status: list[GetConstituentEventParticipationRsvpStatusItem] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> ConstituentEventParticipationCollection | list[ServiceError] | None:
    """Get a constituent's event participation (PREVIEW)

     Returns a constituent's event participation.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        constituent_id (str):
        search_text (str | Unset):
        start_date_from (datetime.date | Unset):
        start_date_to (datetime.date | Unset):
        invitation_status (list[GetConstituentEventParticipationInvitationStatusItem] | Unset):
        rsvp_status (list[GetConstituentEventParticipationRsvpStatusItem] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConstituentEventParticipationCollection | list[ServiceError]
    """

    return sync_detailed(
        constituent_id=constituent_id,
        client=client,
        search_text=search_text,
        start_date_from=start_date_from,
        start_date_to=start_date_to,
        invitation_status=invitation_status,
        rsvp_status=rsvp_status,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    search_text: str | Unset = UNSET,
    start_date_from: datetime.date | Unset = UNSET,
    start_date_to: datetime.date | Unset = UNSET,
    invitation_status: list[GetConstituentEventParticipationInvitationStatusItem] | Unset = UNSET,
    rsvp_status: list[GetConstituentEventParticipationRsvpStatusItem] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[ConstituentEventParticipationCollection | list[ServiceError]]:
    """Get a constituent's event participation (PREVIEW)

     Returns a constituent's event participation.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        constituent_id (str):
        search_text (str | Unset):
        start_date_from (datetime.date | Unset):
        start_date_to (datetime.date | Unset):
        invitation_status (list[GetConstituentEventParticipationInvitationStatusItem] | Unset):
        rsvp_status (list[GetConstituentEventParticipationRsvpStatusItem] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConstituentEventParticipationCollection | list[ServiceError]]
    """

    kwargs = _get_kwargs(
        constituent_id=constituent_id,
        search_text=search_text,
        start_date_from=start_date_from,
        start_date_to=start_date_to,
        invitation_status=invitation_status,
        rsvp_status=rsvp_status,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    search_text: str | Unset = UNSET,
    start_date_from: datetime.date | Unset = UNSET,
    start_date_to: datetime.date | Unset = UNSET,
    invitation_status: list[GetConstituentEventParticipationInvitationStatusItem] | Unset = UNSET,
    rsvp_status: list[GetConstituentEventParticipationRsvpStatusItem] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> ConstituentEventParticipationCollection | list[ServiceError] | None:
    """Get a constituent's event participation (PREVIEW)

     Returns a constituent's event participation.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        constituent_id (str):
        search_text (str | Unset):
        start_date_from (datetime.date | Unset):
        start_date_to (datetime.date | Unset):
        invitation_status (list[GetConstituentEventParticipationInvitationStatusItem] | Unset):
        rsvp_status (list[GetConstituentEventParticipationRsvpStatusItem] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConstituentEventParticipationCollection | list[ServiceError]
    """

    return (
        await asyncio_detailed(
            constituent_id=constituent_id,
            client=client,
            search_text=search_text,
            start_date_from=start_date_from,
            start_date_to=start_date_to,
            invitation_status=invitation_status,
            rsvp_status=rsvp_status,
            limit=limit,
            offset=offset,
        )
    ).parsed
