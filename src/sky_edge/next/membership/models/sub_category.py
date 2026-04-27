from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="SubCategory")


@_attrs_define
class SubCategory:
    """SubCategory drop down data

    Attributes:
        legacy_id (int | None | Unset): The system genrated ID.
        value (None | str | Unset): The value of the code table entry.
    """

    legacy_id: int | None | Unset = UNSET
    value: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        legacy_id: int | None | Unset
        if isinstance(self.legacy_id, Unset):
            legacy_id = UNSET
        else:
            legacy_id = self.legacy_id

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if legacy_id is not UNSET:
            field_dict["legacy_id"] = legacy_id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_legacy_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        legacy_id = _parse_legacy_id(d.pop("legacy_id", UNSET))

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        sub_category = cls(
            legacy_id=legacy_id,
            value=value,
        )

        return sub_category
