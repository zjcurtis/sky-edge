from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="TableEntryEdit")


@_attrs_define
class TableEntryEdit:
    """RE7 Table entry record edit class from the dbo.TableEntries table in Raiser's Edge.

    Attributes:
        long_description (str): The long description of the entry.
        is_active (bool | Unset): The active status of the entry.
        short_description (None | str | Unset): The short description of the entry.
        numeric_value (float | None | Unset): The numeric value of the entry.
    """

    long_description: str
    is_active: bool | Unset = UNSET
    short_description: None | str | Unset = UNSET
    numeric_value: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        long_description = self.long_description

        is_active = self.is_active

        short_description: None | str | Unset
        if isinstance(self.short_description, Unset):
            short_description = UNSET
        else:
            short_description = self.short_description

        numeric_value: float | None | Unset
        if isinstance(self.numeric_value, Unset):
            numeric_value = UNSET
        else:
            numeric_value = self.numeric_value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "long_description": long_description,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if short_description is not UNSET:
            field_dict["short_description"] = short_description
        if numeric_value is not UNSET:
            field_dict["numeric_value"] = numeric_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        long_description = d.pop("long_description")

        is_active = d.pop("is_active", UNSET)

        def _parse_short_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        short_description = _parse_short_description(d.pop("short_description", UNSET))

        def _parse_numeric_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        numeric_value = _parse_numeric_value(d.pop("numeric_value", UNSET))

        table_entry_edit = cls(
            long_description=long_description,
            is_active=is_active,
            short_description=short_description,
            numeric_value=numeric_value,
        )

        return table_entry_edit
