from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.phone_format import PhoneFormat
from ..models.phone_number_type import PhoneNumberType
from ..models.ratings_data_type import RatingsDataType

T = TypeVar("T", bound="TableEntry")


@_attrs_define
class TableEntry:
    """A Table entry record.

    Attributes:
        table_entries_id (None | str | Unset): The ID of the table entry.
        is_active (bool | Unset): The active status of the entry.
        long_description (None | str | Unset): The long description of the entry.
        short_description (None | str | Unset): The short description of the entry. Only supported by entries of certain
            tables, such as constituent codes.
        numeric_value (float | None | Unset): The numeric value of the entry. Also known as minimum amount for
            Gift/Donor table entries.
        sequence (int | None | Unset): The sequence of the table entry.
        is_system_entry (bool | Unset): The value indicating whether the entry is a system entry.
        code_tables_id (None | str | Unset): The ID associated with the record's code table.
        date_added (datetime.datetime | None | Unset): The date on which the record was added.
        date_changed (datetime.datetime | None | Unset): The date on which the record was last changed.
        added_by_id (None | str | Unset): The ID of the user who added the record.
        last_changed_by_id (None | str | Unset): The ID of the user who last changed the record.
        code_tables_name (None | str | Unset): The name of the code table the table entry belongs to.
        phone_format (PhoneFormat | Unset): <p>Members:</p><ul><li><i>None</i></li><li><i>Mask1</i></li><li><i>Mask2</i>
            </li><li><i>Mask3</i></li><li><i>Mask4</i></li><li><i>Mask5</i></li><li><i>Mask6</i></li><li><i>Mask7</i></li><l
            i><i>Mask8</i></li><li><i>Mask9</i></li><li><i>Mask10</i></li><li><i>Mask11</i></li></ul>
        phone_type (PhoneNumberType | Unset): <p>Members:</p><ul><li><i>TelephoneNumber</i></li><li><i>FaxNumber</i></li
            ><li><i>EmailAddress</i></li><li><i>WebAddressUrl</i></li><li><i>Other</i></li></ul>
        ratings_data_type (RatingsDataType | Unset): <p>Members:</p><ul><li><i>Text</i></li><li><i>Number</i></li><li><i
            >Date</i></li><li><i>Currency</i></li><li><i>Boolean</i></li><li><i>Table</i></li></ul>
        table_number (None | str | Unset): For ratings type table entries that are of table data type, the table used as
            the possible rating values.
    """

    table_entries_id: None | str | Unset = UNSET
    is_active: bool | Unset = UNSET
    long_description: None | str | Unset = UNSET
    short_description: None | str | Unset = UNSET
    numeric_value: float | None | Unset = UNSET
    sequence: int | None | Unset = UNSET
    is_system_entry: bool | Unset = UNSET
    code_tables_id: None | str | Unset = UNSET
    date_added: datetime.datetime | None | Unset = UNSET
    date_changed: datetime.datetime | None | Unset = UNSET
    added_by_id: None | str | Unset = UNSET
    last_changed_by_id: None | str | Unset = UNSET
    code_tables_name: None | str | Unset = UNSET
    phone_format: PhoneFormat | Unset = UNSET
    phone_type: PhoneNumberType | Unset = UNSET
    ratings_data_type: RatingsDataType | Unset = UNSET
    table_number: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        table_entries_id: None | str | Unset
        if isinstance(self.table_entries_id, Unset):
            table_entries_id = UNSET
        else:
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

        code_tables_id: None | str | Unset
        if isinstance(self.code_tables_id, Unset):
            code_tables_id = UNSET
        else:
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

        added_by_id: None | str | Unset
        if isinstance(self.added_by_id, Unset):
            added_by_id = UNSET
        else:
            added_by_id = self.added_by_id

        last_changed_by_id: None | str | Unset
        if isinstance(self.last_changed_by_id, Unset):
            last_changed_by_id = UNSET
        else:
            last_changed_by_id = self.last_changed_by_id

        code_tables_name: None | str | Unset
        if isinstance(self.code_tables_name, Unset):
            code_tables_name = UNSET
        else:
            code_tables_name = self.code_tables_name

        phone_format: str | Unset = UNSET
        if not isinstance(self.phone_format, Unset):
            phone_format = self.phone_format.value

        phone_type: str | Unset = UNSET
        if not isinstance(self.phone_type, Unset):
            phone_type = self.phone_type.value

        ratings_data_type: str | Unset = UNSET
        if not isinstance(self.ratings_data_type, Unset):
            ratings_data_type = self.ratings_data_type.value

        table_number: None | str | Unset
        if isinstance(self.table_number, Unset):
            table_number = UNSET
        else:
            table_number = self.table_number

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
        if phone_format is not UNSET:
            field_dict["phone_format"] = phone_format
        if phone_type is not UNSET:
            field_dict["phone_type"] = phone_type
        if ratings_data_type is not UNSET:
            field_dict["ratings_data_type"] = ratings_data_type
        if table_number is not UNSET:
            field_dict["table_number"] = table_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_table_entries_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        table_entries_id = _parse_table_entries_id(d.pop("table_entries_id", UNSET))

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

        def _parse_code_tables_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code_tables_id = _parse_code_tables_id(d.pop("code_tables_id", UNSET))

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

        def _parse_added_by_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        added_by_id = _parse_added_by_id(d.pop("added_by_id", UNSET))

        def _parse_last_changed_by_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

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

        _phone_format = d.pop("phone_format", UNSET)
        phone_format: PhoneFormat | Unset
        if isinstance(_phone_format, Unset):
            phone_format = UNSET
        else:
            phone_format = PhoneFormat(_phone_format)

        _phone_type = d.pop("phone_type", UNSET)
        phone_type: PhoneNumberType | Unset
        if isinstance(_phone_type, Unset):
            phone_type = UNSET
        else:
            phone_type = PhoneNumberType(_phone_type)

        _ratings_data_type = d.pop("ratings_data_type", UNSET)
        ratings_data_type: RatingsDataType | Unset
        if isinstance(_ratings_data_type, Unset):
            ratings_data_type = UNSET
        else:
            ratings_data_type = RatingsDataType(_ratings_data_type)

        def _parse_table_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        table_number = _parse_table_number(d.pop("table_number", UNSET))

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
            phone_format=phone_format,
            phone_type=phone_type,
            ratings_data_type=ratings_data_type,
            table_number=table_number,
        )

        return table_entry
