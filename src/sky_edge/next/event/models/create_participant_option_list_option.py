from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="CreateParticipantOptionListOption")


@_attrs_define
class CreateParticipantOptionListOption:
    """List options for event participant options are the values participants can select when they provide responses.

    Attributes:
        name (None | str | Unset): The name of the list option.
        sequence (int | Unset): The 0-based sequence used for ordering.
    """

    name: None | str | Unset = UNSET
    sequence: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        sequence = self.sequence

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if sequence is not UNSET:
            field_dict["sequence"] = sequence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        sequence = d.pop("sequence", UNSET)

        create_participant_option_list_option = cls(
            name=name,
            sequence=sequence,
        )

        return create_participant_option_list_option
