from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.participant_entry_participant_option_input_type import (
    ParticipantEntryParticipantOptionInputType,
)

if TYPE_CHECKING:
    from ..models.participant_option_value import ParticipantOptionValue


T = TypeVar("T", bound="ParticipantEntryParticipantOption")


@_attrs_define
class ParticipantEntryParticipantOption:
    """An event participant option for a participant entry

    Attributes:
        id (None | str | Unset): The event participant option ID
        name (None | str | Unset): The event participant option name
        input_type (ParticipantEntryParticipantOptionInputType | Unset): The event participant option type<p>Available
            values:</p><ul><li><i>Boolean</i> - Represents a true/false option.</li><li><i>String</i> - Represents a free-
            form text option.</li><li><i>List</i> - Represents an option with a list of possible values.</li></ul>
        values (list[ParticipantOptionValue] | None | Unset): The participant option value(s)
    """

    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    input_type: ParticipantEntryParticipantOptionInputType | Unset = UNSET
    values: list[ParticipantOptionValue] | None | Unset = UNSET

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

        values: list[dict[str, Any]] | None | Unset
        if isinstance(self.values, Unset):
            values = UNSET
        elif isinstance(self.values, list):
            values = []
            for values_type_0_item_data in self.values:
                values_type_0_item = values_type_0_item_data.to_dict()
                values.append(values_type_0_item)

        else:
            values = self.values

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if input_type is not UNSET:
            field_dict["input_type"] = input_type
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.participant_option_value import ParticipantOptionValue

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
        input_type: ParticipantEntryParticipantOptionInputType | Unset
        if isinstance(_input_type, Unset):
            input_type = UNSET
        else:
            input_type = ParticipantEntryParticipantOptionInputType(_input_type)

        def _parse_values(data: object) -> list[ParticipantOptionValue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                values_type_0 = []
                _values_type_0 = data
                for values_type_0_item_data in _values_type_0:
                    values_type_0_item = ParticipantOptionValue.from_dict(
                        values_type_0_item_data
                    )

                    values_type_0.append(values_type_0_item)

                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ParticipantOptionValue] | None | Unset, data)

        values = _parse_values(d.pop("values", UNSET))

        participant_entry_participant_option = cls(
            id=id,
            name=name,
            input_type=input_type,
            values=values,
        )

        return participant_entry_participant_option
