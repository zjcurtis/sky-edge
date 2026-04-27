from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="ConsentSource")


@_attrs_define
class ConsentSource:
    """Represents the consent source entity.

    Attributes:
        description (None | str | Unset): The name of the consent source.
        inactive (bool | None | Unset): Indicates whether the consent source is inactive.
        sequence (int | None | Unset): The placement of the source in the order of source table values, if defined.
    """

    description: None | str | Unset = UNSET
    inactive: bool | None | Unset = UNSET
    sequence: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        inactive: bool | None | Unset
        if isinstance(self.inactive, Unset):
            inactive = UNSET
        else:
            inactive = self.inactive

        sequence: int | None | Unset
        if isinstance(self.sequence, Unset):
            sequence = UNSET
        else:
            sequence = self.sequence

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if sequence is not UNSET:
            field_dict["sequence"] = sequence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_inactive(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        inactive = _parse_inactive(d.pop("inactive", UNSET))

        def _parse_sequence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequence = _parse_sequence(d.pop("sequence", UNSET))

        consent_source = cls(
            description=description,
            inactive=inactive,
            sequence=sequence,
        )

        return consent_source
