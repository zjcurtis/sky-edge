from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.event_participant_option_input_type import (
    EventParticipantOptionInputType,
)
from ..models.event_participant_option_list_option import (
    EventParticipantOptionListOption,
)

T = TypeVar("T", bound="EventParticipantOption")


@_attrs_define
class EventParticipantOption:
    """Event participant options are fields that collects details about participants, such as t-shirt sizes, meal
    preferences, or seating requests.
    Set options and their values for an event and then add responses for each participant.

        Attributes:
            id (None | str | Unset): The ID of the event participant option.
            name (None | str | Unset): The name of the event participant option.
            input_type (EventParticipantOptionInputType | Unset): The type of the event participant option.<p>Available
                values:</p><ul><li><i>Boolean</i> - Represents a true/false option.</li><li><i>String</i> - Represents a free-
                form text option.</li><li><i>List</i> - Represents an option with a list of possible values.</li></ul>
            multi_select (bool | Unset): Only valid for List input type, determines if multiple options can be selected.
            list_options (list[EventParticipantOptionListOption] | None | Unset): Only valid for List input type, the
                available options.
            added_by_user (None | str | Unset): The ID of the user that added this option.
            updated_by_user (None | str | Unset): The ID of the user who updated this option.
            added_by_service (None | str | Unset): The name of the service that added this option.
            updated_by_service (None | str | Unset): The name of the service that updated this option.
            date_added (datetime.datetime | Unset): The date this option was added. Includes an offset from UTC in <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format</a>: <i>1969-11-21T10:29:43-04:00</i>.
            date_updated (datetime.datetime | Unset): The date this option was updated. Includes an offset from UTC in <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format</a>: <i>1969-11-21T10:29:43-04:00</i>.
            version (int | Unset): The version number of the option.
    """

    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    input_type: EventParticipantOptionInputType | Unset = UNSET
    multi_select: bool | Unset = UNSET
    list_options: list[EventParticipantOptionListOption] | None | Unset = UNSET
    added_by_user: None | str | Unset = UNSET
    updated_by_user: None | str | Unset = UNSET
    added_by_service: None | str | Unset = UNSET
    updated_by_service: None | str | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    date_updated: datetime.datetime | Unset = UNSET
    version: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        input_type: str | Unset = UNSET
        if not isinstance(self.input_type, Unset):
            input_type = self.input_type.value

        multi_select = self.multi_select

        list_options: list[dict[str, Any]] | None | Unset
        if isinstance(self.list_options, Unset):
            list_options = UNSET
        elif isinstance(self.list_options, list):
            list_options = []
            for list_options_type_0_item_data in self.list_options:
                list_options_type_0_item = list_options_type_0_item_data.to_dict()
                list_options.append(list_options_type_0_item)

        else:
            list_options = self.list_options

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

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if input_type is not UNSET:
            field_dict["input_type"] = input_type
        if multi_select is not UNSET:
            field_dict["multi_select"] = multi_select
        if list_options is not UNSET:
            field_dict["list_options"] = list_options
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
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_participant_option_list_option import (
            EventParticipantOptionListOption,
        )

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _input_type = d.pop("input_type", UNSET)
        input_type: EventParticipantOptionInputType | Unset
        if isinstance(_input_type, Unset):
            input_type = UNSET
        else:
            input_type = EventParticipantOptionInputType(_input_type)

        multi_select = d.pop("multi_select", UNSET)

        def _parse_list_options(
            data: object,
        ) -> list[EventParticipantOptionListOption] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                list_options_type_0 = []
                _list_options_type_0 = data
                for list_options_type_0_item_data in _list_options_type_0:
                    list_options_type_0_item = (
                        EventParticipantOptionListOption.from_dict(
                            list_options_type_0_item_data
                        )
                    )

                    list_options_type_0.append(list_options_type_0_item)

                return list_options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EventParticipantOptionListOption] | None | Unset, data)

        list_options = _parse_list_options(d.pop("list_options", UNSET))

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

        updated_by_service = _parse_updated_by_service(
            d.pop("updated_by_service", UNSET)
        )

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

        version = d.pop("version", UNSET)

        event_participant_option = cls(
            id=id,
            name=name,
            input_type=input_type,
            multi_select=multi_select,
            list_options=list_options,
            added_by_user=added_by_user,
            updated_by_user=updated_by_user,
            added_by_service=added_by_service,
            updated_by_service=updated_by_service,
            date_added=date_added,
            date_updated=date_updated,
            version=version,
        )

        return event_participant_option
