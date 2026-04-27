from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="Vendor")


@_attrs_define
class Vendor:
    """Vendor details of event expense.

    Attributes:
        participant_id (None | str | Unset): The ID of a vendor participant of an event expense.
        display_name (None | str | Unset): The display name of a vendor participant of an event expense.
    """

    participant_id: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        participant_id: None | str | Unset
        if isinstance(self.participant_id, Unset):
            participant_id = UNSET
        else:
            participant_id = self.participant_id

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if participant_id is not UNSET:
            field_dict["participant_id"] = participant_id
        if display_name is not UNSET:
            field_dict["display_name"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_participant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        participant_id = _parse_participant_id(d.pop("participant_id", UNSET))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        vendor = cls(
            participant_id=participant_id,
            display_name=display_name,
        )

        return vendor
