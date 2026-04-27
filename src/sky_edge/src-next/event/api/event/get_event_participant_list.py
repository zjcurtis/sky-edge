import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_event_participant_list_event_fee_include_type import GetEventParticipantListEventFeeIncludeType
from ...models.get_event_participant_list_invitation_status_item import GetEventParticipantListInvitationStatusItem
from ...models.get_event_participant_list_online_data_health_item import GetEventParticipantListOnlineDataHealthItem
from ...models.get_event_participant_list_registration_form_include_type import (
    GetEventParticipantListRegistrationFormIncludeType,
)
from ...models.get_event_participant_list_rsvp_status_item import GetEventParticipantListRsvpStatusItem
from ...models.participant_list_entry_collection import ParticipantListEntryCollection
from ...models.service_error import ServiceError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    event_id: str,
    *,
    name: str | Unset = UNSET,
    participation_level: list[str] | Unset = UNSET,
    attended_filter: bool | Unset = UNSET,
    is_constituent_filter: bool | Unset = UNSET,
    email_eligible_filter: bool | Unset = UNSET,
    phone_call_eligible_filter: bool | Unset = UNSET,
    invitation_status: list[GetEventParticipantListInvitationStatusItem] | Unset = UNSET,
    rsvp_status: list[GetEventParticipantListRsvpStatusItem] | Unset = UNSET,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    fees_paid_filter: bool | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    participant_option_id: str | Unset = UNSET,
    participant_option_values: list[str] | Unset = UNSET,
    registration_form_include_type: GetEventParticipantListRegistrationFormIncludeType | Unset = UNSET,
    registration_form_ids: list[str] | Unset = UNSET,
    online_data_health: list[GetEventParticipantListOnlineDataHealthItem] | Unset = UNSET,
    event_fee_include_type: GetEventParticipantListEventFeeIncludeType | Unset = UNSET,
    event_fee_ids: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["name"] = name

    json_participation_level: list[str] | Unset = UNSET
    if not isinstance(participation_level, Unset):
        json_participation_level = participation_level

    params["participation_level"] = json_participation_level

    params["attended_filter"] = attended_filter

    params["is_constituent_filter"] = is_constituent_filter

    params["email_eligible_filter"] = email_eligible_filter

    params["phone_call_eligible_filter"] = phone_call_eligible_filter

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

    json_date_added: str | Unset = UNSET
    if not isinstance(date_added, Unset):
        json_date_added = date_added.isoformat()
    params["date_added"] = json_date_added

    json_last_modified: str | Unset = UNSET
    if not isinstance(last_modified, Unset):
        json_last_modified = last_modified.isoformat()
    params["last_modified"] = json_last_modified

    params["fees_paid_filter"] = fees_paid_filter

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    json_sort: list[str] | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["participant_option_id"] = participant_option_id

    json_participant_option_values: list[str] | Unset = UNSET
    if not isinstance(participant_option_values, Unset):
        json_participant_option_values = participant_option_values

    params["participant_option_values"] = json_participant_option_values

    json_registration_form_include_type: str | Unset = UNSET
    if not isinstance(registration_form_include_type, Unset):
        json_registration_form_include_type = registration_form_include_type.value

    params["registration_form_include_type"] = json_registration_form_include_type

    json_registration_form_ids: list[str] | Unset = UNSET
    if not isinstance(registration_form_ids, Unset):
        json_registration_form_ids = registration_form_ids

    params["registration_form_ids"] = json_registration_form_ids

    json_online_data_health: list[str] | Unset = UNSET
    if not isinstance(online_data_health, Unset):
        json_online_data_health = []
        for online_data_health_item_data in online_data_health:
            online_data_health_item = online_data_health_item_data.value
            json_online_data_health.append(online_data_health_item)

    params["online_data_health"] = json_online_data_health

    json_event_fee_include_type: str | Unset = UNSET
    if not isinstance(event_fee_include_type, Unset):
        json_event_fee_include_type = event_fee_include_type.value

    params["event_fee_include_type"] = json_event_fee_include_type

    json_event_fee_ids: list[str] | Unset = UNSET
    if not isinstance(event_fee_ids, Unset):
        json_event_fee_ids = event_fee_ids

    params["event_fee_ids"] = json_event_fee_ids

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/events/{event_id}/participants".format(
            event_id=quote(str(event_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ParticipantListEntryCollection | list[ServiceError] | None:
    if response.status_code == 200:
        response_200 = ParticipantListEntryCollection.from_dict(response.json())

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
) -> Response[ParticipantListEntryCollection | list[ServiceError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    participation_level: list[str] | Unset = UNSET,
    attended_filter: bool | Unset = UNSET,
    is_constituent_filter: bool | Unset = UNSET,
    email_eligible_filter: bool | Unset = UNSET,
    phone_call_eligible_filter: bool | Unset = UNSET,
    invitation_status: list[GetEventParticipantListInvitationStatusItem] | Unset = UNSET,
    rsvp_status: list[GetEventParticipantListRsvpStatusItem] | Unset = UNSET,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    fees_paid_filter: bool | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    participant_option_id: str | Unset = UNSET,
    participant_option_values: list[str] | Unset = UNSET,
    registration_form_include_type: GetEventParticipantListRegistrationFormIncludeType | Unset = UNSET,
    registration_form_ids: list[str] | Unset = UNSET,
    online_data_health: list[GetEventParticipantListOnlineDataHealthItem] | Unset = UNSET,
    event_fee_include_type: GetEventParticipantListEventFeeIncludeType | Unset = UNSET,
    event_fee_ids: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[ParticipantListEntryCollection | list[ServiceError]]:
    """Get event participant list

     Returns a list of participants for an event.

    Args:
        event_id (str):
        name (str | Unset):
        participation_level (list[str] | Unset):
        attended_filter (bool | Unset):
        is_constituent_filter (bool | Unset):
        email_eligible_filter (bool | Unset):
        phone_call_eligible_filter (bool | Unset):
        invitation_status (list[GetEventParticipantListInvitationStatusItem] | Unset):
        rsvp_status (list[GetEventParticipantListRsvpStatusItem] | Unset):
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        fees_paid_filter (bool | Unset):
        fields (list[str] | Unset):
        sort (list[str] | Unset):
        participant_option_id (str | Unset):
        participant_option_values (list[str] | Unset):
        registration_form_include_type (GetEventParticipantListRegistrationFormIncludeType |
            Unset):
        registration_form_ids (list[str] | Unset):
        online_data_health (list[GetEventParticipantListOnlineDataHealthItem] | Unset):
        event_fee_include_type (GetEventParticipantListEventFeeIncludeType | Unset):
        event_fee_ids (list[str] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ParticipantListEntryCollection | list[ServiceError]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        name=name,
        participation_level=participation_level,
        attended_filter=attended_filter,
        is_constituent_filter=is_constituent_filter,
        email_eligible_filter=email_eligible_filter,
        phone_call_eligible_filter=phone_call_eligible_filter,
        invitation_status=invitation_status,
        rsvp_status=rsvp_status,
        date_added=date_added,
        last_modified=last_modified,
        fees_paid_filter=fees_paid_filter,
        fields=fields,
        sort=sort,
        participant_option_id=participant_option_id,
        participant_option_values=participant_option_values,
        registration_form_include_type=registration_form_include_type,
        registration_form_ids=registration_form_ids,
        online_data_health=online_data_health,
        event_fee_include_type=event_fee_include_type,
        event_fee_ids=event_fee_ids,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    participation_level: list[str] | Unset = UNSET,
    attended_filter: bool | Unset = UNSET,
    is_constituent_filter: bool | Unset = UNSET,
    email_eligible_filter: bool | Unset = UNSET,
    phone_call_eligible_filter: bool | Unset = UNSET,
    invitation_status: list[GetEventParticipantListInvitationStatusItem] | Unset = UNSET,
    rsvp_status: list[GetEventParticipantListRsvpStatusItem] | Unset = UNSET,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    fees_paid_filter: bool | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    participant_option_id: str | Unset = UNSET,
    participant_option_values: list[str] | Unset = UNSET,
    registration_form_include_type: GetEventParticipantListRegistrationFormIncludeType | Unset = UNSET,
    registration_form_ids: list[str] | Unset = UNSET,
    online_data_health: list[GetEventParticipantListOnlineDataHealthItem] | Unset = UNSET,
    event_fee_include_type: GetEventParticipantListEventFeeIncludeType | Unset = UNSET,
    event_fee_ids: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> ParticipantListEntryCollection | list[ServiceError] | None:
    """Get event participant list

     Returns a list of participants for an event.

    Args:
        event_id (str):
        name (str | Unset):
        participation_level (list[str] | Unset):
        attended_filter (bool | Unset):
        is_constituent_filter (bool | Unset):
        email_eligible_filter (bool | Unset):
        phone_call_eligible_filter (bool | Unset):
        invitation_status (list[GetEventParticipantListInvitationStatusItem] | Unset):
        rsvp_status (list[GetEventParticipantListRsvpStatusItem] | Unset):
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        fees_paid_filter (bool | Unset):
        fields (list[str] | Unset):
        sort (list[str] | Unset):
        participant_option_id (str | Unset):
        participant_option_values (list[str] | Unset):
        registration_form_include_type (GetEventParticipantListRegistrationFormIncludeType |
            Unset):
        registration_form_ids (list[str] | Unset):
        online_data_health (list[GetEventParticipantListOnlineDataHealthItem] | Unset):
        event_fee_include_type (GetEventParticipantListEventFeeIncludeType | Unset):
        event_fee_ids (list[str] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ParticipantListEntryCollection | list[ServiceError]
    """

    return sync_detailed(
        event_id=event_id,
        client=client,
        name=name,
        participation_level=participation_level,
        attended_filter=attended_filter,
        is_constituent_filter=is_constituent_filter,
        email_eligible_filter=email_eligible_filter,
        phone_call_eligible_filter=phone_call_eligible_filter,
        invitation_status=invitation_status,
        rsvp_status=rsvp_status,
        date_added=date_added,
        last_modified=last_modified,
        fees_paid_filter=fees_paid_filter,
        fields=fields,
        sort=sort,
        participant_option_id=participant_option_id,
        participant_option_values=participant_option_values,
        registration_form_include_type=registration_form_include_type,
        registration_form_ids=registration_form_ids,
        online_data_health=online_data_health,
        event_fee_include_type=event_fee_include_type,
        event_fee_ids=event_fee_ids,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    participation_level: list[str] | Unset = UNSET,
    attended_filter: bool | Unset = UNSET,
    is_constituent_filter: bool | Unset = UNSET,
    email_eligible_filter: bool | Unset = UNSET,
    phone_call_eligible_filter: bool | Unset = UNSET,
    invitation_status: list[GetEventParticipantListInvitationStatusItem] | Unset = UNSET,
    rsvp_status: list[GetEventParticipantListRsvpStatusItem] | Unset = UNSET,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    fees_paid_filter: bool | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    participant_option_id: str | Unset = UNSET,
    participant_option_values: list[str] | Unset = UNSET,
    registration_form_include_type: GetEventParticipantListRegistrationFormIncludeType | Unset = UNSET,
    registration_form_ids: list[str] | Unset = UNSET,
    online_data_health: list[GetEventParticipantListOnlineDataHealthItem] | Unset = UNSET,
    event_fee_include_type: GetEventParticipantListEventFeeIncludeType | Unset = UNSET,
    event_fee_ids: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[ParticipantListEntryCollection | list[ServiceError]]:
    """Get event participant list

     Returns a list of participants for an event.

    Args:
        event_id (str):
        name (str | Unset):
        participation_level (list[str] | Unset):
        attended_filter (bool | Unset):
        is_constituent_filter (bool | Unset):
        email_eligible_filter (bool | Unset):
        phone_call_eligible_filter (bool | Unset):
        invitation_status (list[GetEventParticipantListInvitationStatusItem] | Unset):
        rsvp_status (list[GetEventParticipantListRsvpStatusItem] | Unset):
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        fees_paid_filter (bool | Unset):
        fields (list[str] | Unset):
        sort (list[str] | Unset):
        participant_option_id (str | Unset):
        participant_option_values (list[str] | Unset):
        registration_form_include_type (GetEventParticipantListRegistrationFormIncludeType |
            Unset):
        registration_form_ids (list[str] | Unset):
        online_data_health (list[GetEventParticipantListOnlineDataHealthItem] | Unset):
        event_fee_include_type (GetEventParticipantListEventFeeIncludeType | Unset):
        event_fee_ids (list[str] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ParticipantListEntryCollection | list[ServiceError]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        name=name,
        participation_level=participation_level,
        attended_filter=attended_filter,
        is_constituent_filter=is_constituent_filter,
        email_eligible_filter=email_eligible_filter,
        phone_call_eligible_filter=phone_call_eligible_filter,
        invitation_status=invitation_status,
        rsvp_status=rsvp_status,
        date_added=date_added,
        last_modified=last_modified,
        fees_paid_filter=fees_paid_filter,
        fields=fields,
        sort=sort,
        participant_option_id=participant_option_id,
        participant_option_values=participant_option_values,
        registration_form_include_type=registration_form_include_type,
        registration_form_ids=registration_form_ids,
        online_data_health=online_data_health,
        event_fee_include_type=event_fee_include_type,
        event_fee_ids=event_fee_ids,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    participation_level: list[str] | Unset = UNSET,
    attended_filter: bool | Unset = UNSET,
    is_constituent_filter: bool | Unset = UNSET,
    email_eligible_filter: bool | Unset = UNSET,
    phone_call_eligible_filter: bool | Unset = UNSET,
    invitation_status: list[GetEventParticipantListInvitationStatusItem] | Unset = UNSET,
    rsvp_status: list[GetEventParticipantListRsvpStatusItem] | Unset = UNSET,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    fees_paid_filter: bool | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    participant_option_id: str | Unset = UNSET,
    participant_option_values: list[str] | Unset = UNSET,
    registration_form_include_type: GetEventParticipantListRegistrationFormIncludeType | Unset = UNSET,
    registration_form_ids: list[str] | Unset = UNSET,
    online_data_health: list[GetEventParticipantListOnlineDataHealthItem] | Unset = UNSET,
    event_fee_include_type: GetEventParticipantListEventFeeIncludeType | Unset = UNSET,
    event_fee_ids: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> ParticipantListEntryCollection | list[ServiceError] | None:
    """Get event participant list

     Returns a list of participants for an event.

    Args:
        event_id (str):
        name (str | Unset):
        participation_level (list[str] | Unset):
        attended_filter (bool | Unset):
        is_constituent_filter (bool | Unset):
        email_eligible_filter (bool | Unset):
        phone_call_eligible_filter (bool | Unset):
        invitation_status (list[GetEventParticipantListInvitationStatusItem] | Unset):
        rsvp_status (list[GetEventParticipantListRsvpStatusItem] | Unset):
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        fees_paid_filter (bool | Unset):
        fields (list[str] | Unset):
        sort (list[str] | Unset):
        participant_option_id (str | Unset):
        participant_option_values (list[str] | Unset):
        registration_form_include_type (GetEventParticipantListRegistrationFormIncludeType |
            Unset):
        registration_form_ids (list[str] | Unset):
        online_data_health (list[GetEventParticipantListOnlineDataHealthItem] | Unset):
        event_fee_include_type (GetEventParticipantListEventFeeIncludeType | Unset):
        event_fee_ids (list[str] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ParticipantListEntryCollection | list[ServiceError]
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            client=client,
            name=name,
            participation_level=participation_level,
            attended_filter=attended_filter,
            is_constituent_filter=is_constituent_filter,
            email_eligible_filter=email_eligible_filter,
            phone_call_eligible_filter=phone_call_eligible_filter,
            invitation_status=invitation_status,
            rsvp_status=rsvp_status,
            date_added=date_added,
            last_modified=last_modified,
            fees_paid_filter=fees_paid_filter,
            fields=fields,
            sort=sort,
            participant_option_id=participant_option_id,
            participant_option_values=participant_option_values,
            registration_form_include_type=registration_form_include_type,
            registration_form_ids=registration_form_ids,
            online_data_health=online_data_health,
            event_fee_include_type=event_fee_include_type,
            event_fee_ids=event_fee_ids,
            limit=limit,
            offset=offset,
        )
    ).parsed
