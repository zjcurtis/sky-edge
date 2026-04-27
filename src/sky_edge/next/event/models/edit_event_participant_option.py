from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_participant_option_list_option import (
        EventParticipantOptionListOption,
    )


T = TypeVar("T", bound="EditEventParticipantOption")


@_attrs_define
class EditEventParticipantOption:
    """Event participant options are fields that collects details about participants, such as t-shirt sizes, meal
    preferences, or seating requests.
    Set options and their values for an event and then add responses for each participant.

        Attributes:
            name (None | str | Unset): The name of the event participant option.
            list_options (list[EventParticipantOptionListOption] | None | Unset): The available options for the List input
                type.
    """

    name: None | str | Unset = UNSET
    list_options: list[EventParticipantOptionListOption] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if list_options is not UNSET:
            field_dict["list_options"] = list_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_participant_option_list_option import (
            EventParticipantOptionListOption,
        )

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

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

        edit_event_participant_option = cls(
            name=name,
            list_options=list_options,
        )

        return edit_event_participant_option
