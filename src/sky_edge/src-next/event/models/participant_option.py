from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ParticipantOption")


@_attrs_define
class ParticipantOption:
    """The participant option associated with a given participant

    Attributes:
        id (None | str | Unset): The ID of the participant option.
        participant_id (None | str | Unset): The ID of the participant.
        event_id (None | str | Unset): The ID of the event.
        event_participant_option_id (None | str | Unset): The ID of the event participant option.
        option_value (None | str | Unset): The participant's response to the option.
        added_by_user (None | str | Unset): The ID of the user that added the participant option.
        updated_by_user (None | str | Unset): The ID of the user who updated the participant option.
        added_by_service (None | str | Unset): The name of the service that added this participant option.
        updated_by_service (None | str | Unset): The name of the service that updated this participant option.
        date_added (datetime.datetime | Unset): The date the participant option was added. Includes an offset from UTC
            in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format</a>: <i>1969-11-21T10:29:43-04:00</i>.
        date_updated (datetime.datetime | Unset): The date the participant option was updated. Includes an offset from
            UTC in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format</a>: <i>1969-11-21T10:29:43-04:00</i>.
    """

    id: None | str | Unset = UNSET
    participant_id: None | str | Unset = UNSET
    event_id: None | str | Unset = UNSET
    event_participant_option_id: None | str | Unset = UNSET
    option_value: None | str | Unset = UNSET
    added_by_user: None | str | Unset = UNSET
    updated_by_user: None | str | Unset = UNSET
    added_by_service: None | str | Unset = UNSET
    updated_by_service: None | str | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    date_updated: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        participant_id: None | str | Unset
        if isinstance(self.participant_id, Unset):
            participant_id = UNSET
        else:
            participant_id = self.participant_id

        event_id: None | str | Unset
        if isinstance(self.event_id, Unset):
            event_id = UNSET
        else:
            event_id = self.event_id

        event_participant_option_id: None | str | Unset
        if isinstance(self.event_participant_option_id, Unset):
            event_participant_option_id = UNSET
        else:
            event_participant_option_id = self.event_participant_option_id

        option_value: None | str | Unset
        if isinstance(self.option_value, Unset):
            option_value = UNSET
        else:
            option_value = self.option_value

        added_by_user: None | str | Unset
        if isinstance(self.added_by_user, Unset):
            added_by_user = UNSET
        else:
            added_by_user = self.added_by_user

        updated_by_user: None | str | Unset
        if isinstance(self.updated_by_user, Unset):
            updated_by_user = UNSET
        else:
            updated_by_user = self.updated_by_user

        added_by_service: None | str | Unset
        if isinstance(self.added_by_service, Unset):
            added_by_service = UNSET
        else:
            added_by_service = self.added_by_service

        updated_by_service: None | str | Unset
        if isinstance(self.updated_by_service, Unset):
            updated_by_service = UNSET
        else:
            updated_by_service = self.updated_by_service

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        date_updated: str | Unset = UNSET
        if not isinstance(self.date_updated, Unset):
            date_updated = self.date_updated.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if participant_id is not UNSET:
            field_dict["participant_id"] = participant_id
        if event_id is not UNSET:
            field_dict["event_id"] = event_id
        if event_participant_option_id is not UNSET:
            field_dict["event_participant_option_id"] = event_participant_option_id
        if option_value is not UNSET:
            field_dict["option_value"] = option_value
        if added_by_user is not UNSET:
            field_dict["added_by_user"] = added_by_user
        if updated_by_user is not UNSET:
            field_dict["updated_by_user"] = updated_by_user
        if added_by_service is not UNSET:
            field_dict["added_by_service"] = added_by_service
        if updated_by_service is not UNSET:
            field_dict["updated_by_service"] = updated_by_service
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_updated is not UNSET:
            field_dict["date_updated"] = date_updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_participant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        participant_id = _parse_participant_id(d.pop("participant_id", UNSET))

        def _parse_event_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_id = _parse_event_id(d.pop("event_id", UNSET))

        def _parse_event_participant_option_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_participant_option_id = _parse_event_participant_option_id(d.pop("event_participant_option_id", UNSET))

        def _parse_option_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        option_value = _parse_option_value(d.pop("option_value", UNSET))

        def _parse_added_by_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        added_by_user = _parse_added_by_user(d.pop("added_by_user", UNSET))

        def _parse_updated_by_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_by_user = _parse_updated_by_user(d.pop("updated_by_user", UNSET))

        def _parse_added_by_service(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        added_by_service = _parse_added_by_service(d.pop("added_by_service", UNSET))

        def _parse_updated_by_service(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_by_service = _parse_updated_by_service(d.pop("updated_by_service", UNSET))

        _date_added = d.pop("date_added", UNSET)
        date_added: datetime.datetime | Unset
        if isinstance(_date_added, Unset):
            date_added = UNSET
        else:
            date_added = isoparse(_date_added)

        _date_updated = d.pop("date_updated", UNSET)
        date_updated: datetime.datetime | Unset
        if isinstance(_date_updated, Unset):
            date_updated = UNSET
        else:
            date_updated = isoparse(_date_updated)

        participant_option = cls(
            id=id,
            participant_id=participant_id,
            event_id=event_id,
            event_participant_option_id=event_participant_option_id,
            option_value=option_value,
            added_by_user=added_by_user,
            updated_by_user=updated_by_user,
            added_by_service=added_by_service,
            updated_by_service=updated_by_service,
            date_added=date_added,
            date_updated=date_updated,
        )

        return participant_option
