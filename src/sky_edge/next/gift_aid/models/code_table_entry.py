from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="CodeTableEntry")


@_attrs_define
class CodeTableEntry:
    """Code table entry

    Attributes:
        table_entries_id (int | None | Unset): The table entry ID
        long_description (None | str | Unset): The long description.
    """

    table_entries_id: int | None | Unset = UNSET
    long_description: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        table_entries_id: int | None | Unset
        if isinstance(self.table_entries_id, Unset):
            table_entries_id = UNSET
        else:
            table_entries_id = self.table_entries_id

        long_description: None | str | Unset
        if isinstance(self.long_description, Unset):
            long_description = UNSET
        else:
            long_description = self.long_description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if table_entries_id is not UNSET:
            field_dict["table_entries_id"] = table_entries_id
        if long_description is not UNSET:
            field_dict["long_description"] = long_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_table_entries_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        table_entries_id = _parse_table_entries_id(d.pop("table_entries_id", UNSET))

        def _parse_long_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        long_description = _parse_long_description(d.pop("long_description", UNSET))

        code_table_entry = cls(
            table_entries_id=table_entries_id,
            long_description=long_description,
        )

        return code_table_entry
