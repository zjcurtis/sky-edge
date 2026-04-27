from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="TableEntry")


@_attrs_define
class TableEntry:
    """A Code Table record from the dbo.CodeTables table in Raiser's Edge.

    Attributes:
        table_entries_id (int | Unset): The ID for the entry in the dbo.TableEntries table.
        is_active (bool | Unset): The active status of the entry.
        long_description (None | str | Unset): The long description of the entry.
        short_description (None | str | Unset): The short description of the entry.
        numeric_value (float | None | Unset): The numeric value of the entry.
        sequence (int | None | Unset): The sequence of the table entry.
        is_system_entry (bool | Unset): The value indicating whether the entry is a system entry.
        code_tables_id (int | Unset): The ID associated with the record's code table.
        date_added (datetime.datetime | None | Unset): The date on which the record was added.
        date_changed (datetime.datetime | None | Unset): The date on which the record was last changed.
        added_by_id (int | None | Unset): The ID of the user who added the record.
        last_changed_by_id (int | None | Unset): The ID of the user who last changed the record.
        code_tables_name (None | str | Unset): The name of the code table.
    """

    table_entries_id: int | Unset = UNSET
    is_active: bool | Unset = UNSET
    long_description: None | str | Unset = UNSET
    short_description: None | str | Unset = UNSET
    numeric_value: float | None | Unset = UNSET
    sequence: int | None | Unset = UNSET
    is_system_entry: bool | Unset = UNSET
    code_tables_id: int | Unset = UNSET
    date_added: datetime.datetime | None | Unset = UNSET
    date_changed: datetime.datetime | None | Unset = UNSET
    added_by_id: int | None | Unset = UNSET
    last_changed_by_id: int | None | Unset = UNSET
    code_tables_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        table_entries_id = self.table_entries_id

        is_active = self.is_active

        long_description: None | str | Unset
        if isinstance(self.long_description, Unset):
            long_description = UNSET
        else:
            long_description = self.long_description

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

        sequence: int | None | Unset
        if isinstance(self.sequence, Unset):
            sequence = UNSET
        else:
            sequence = self.sequence

        is_system_entry = self.is_system_entry

        code_tables_id = self.code_tables_id

        date_added: None | str | Unset
        if isinstance(self.date_added, Unset):
            date_added = UNSET
        elif isinstance(self.date_added, datetime.datetime):
            date_added = self.date_added.isoformat()
        else:
            date_added = self.date_added

        date_changed: None | str | Unset
        if isinstance(self.date_changed, Unset):
            date_changed = UNSET
        elif isinstance(self.date_changed, datetime.datetime):
            date_changed = self.date_changed.isoformat()
        else:
            date_changed = self.date_changed

        added_by_id: int | None | Unset
        if isinstance(self.added_by_id, Unset):
            added_by_id = UNSET
        else:
            added_by_id = self.added_by_id

        last_changed_by_id: int | None | Unset
        if isinstance(self.last_changed_by_id, Unset):
            last_changed_by_id = UNSET
        else:
            last_changed_by_id = self.last_changed_by_id

        code_tables_name: None | str | Unset
        if isinstance(self.code_tables_name, Unset):
            code_tables_name = UNSET
        else:
            code_tables_name = self.code_tables_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if table_entries_id is not UNSET:
            field_dict["table_entries_id"] = table_entries_id
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if long_description is not UNSET:
            field_dict["long_description"] = long_description
        if short_description is not UNSET:
            field_dict["short_description"] = short_description
        if numeric_value is not UNSET:
            field_dict["numeric_value"] = numeric_value
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if is_system_entry is not UNSET:
            field_dict["is_system_entry"] = is_system_entry
        if code_tables_id is not UNSET:
            field_dict["code_tables_id"] = code_tables_id
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_changed is not UNSET:
            field_dict["date_changed"] = date_changed
        if added_by_id is not UNSET:
            field_dict["added_by_id"] = added_by_id
        if last_changed_by_id is not UNSET:
            field_dict["last_changed_by_id"] = last_changed_by_id
        if code_tables_name is not UNSET:
            field_dict["code_tables_name"] = code_tables_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        table_entries_id = d.pop("table_entries_id", UNSET)

        is_active = d.pop("is_active", UNSET)

        def _parse_long_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        long_description = _parse_long_description(d.pop("long_description", UNSET))

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

        def _parse_sequence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequence = _parse_sequence(d.pop("sequence", UNSET))

        is_system_entry = d.pop("is_system_entry", UNSET)

        code_tables_id = d.pop("code_tables_id", UNSET)

        def _parse_date_added(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_added_type_0 = isoparse(data)

                return date_added_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_added = _parse_date_added(d.pop("date_added", UNSET))

        def _parse_date_changed(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_changed_type_0 = isoparse(data)

                return date_changed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_changed = _parse_date_changed(d.pop("date_changed", UNSET))

        def _parse_added_by_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        added_by_id = _parse_added_by_id(d.pop("added_by_id", UNSET))

        def _parse_last_changed_by_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_changed_by_id = _parse_last_changed_by_id(
            d.pop("last_changed_by_id", UNSET)
        )

        def _parse_code_tables_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code_tables_name = _parse_code_tables_name(d.pop("code_tables_name", UNSET))

        table_entry = cls(
            table_entries_id=table_entries_id,
            is_active=is_active,
            long_description=long_description,
            short_description=short_description,
            numeric_value=numeric_value,
            sequence=sequence,
            is_system_entry=is_system_entry,
            code_tables_id=code_tables_id,
            date_added=date_added,
            date_changed=date_changed,
            added_by_id=added_by_id,
            last_changed_by_id=last_changed_by_id,
            code_tables_name=code_tables_name,
        )

        return table_entry
