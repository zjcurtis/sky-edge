from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.phone_type_phone_format import PhoneTypePhoneFormat
from ..models.phone_type_phone_number_type import PhoneTypePhoneNumberType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PhoneType")


@_attrs_define
class PhoneType:
    """A record from the dbo.TableEntries table in Raiser's Edge for a Phone Type.

    Attributes:
        description (str): The phone type description.
        type_ (PhoneTypePhoneNumberType): The phone number type.
        format_ (PhoneTypePhoneFormat): The phone number format.
        sequence (int | None | Unset): The sequence associated with the phone type.
        is_system_entry (bool | Unset): The value indicating whether the phone type is a system entry.
        date_added (datetime.datetime | None | Unset): The date that the phone type was added.
        date_changed (datetime.datetime | None | Unset): The date that the phone type was changed.
        added_by_id (int | None | Unset): The ID of the user who added the phone type.
        last_changed_by_id (int | None | Unset): The ID of the user who last changed the phone type.
        format_mask (None | str | Unset): The phone format.
        table_entries_id (int | Unset): The ID for the phone type in the dbo.TableEntries table.
        is_active (bool | Unset): The active status of the phone type.
    """

    description: str
    type_: PhoneTypePhoneNumberType
    format_: PhoneTypePhoneFormat
    sequence: int | None | Unset = UNSET
    is_system_entry: bool | Unset = UNSET
    date_added: datetime.datetime | None | Unset = UNSET
    date_changed: datetime.datetime | None | Unset = UNSET
    added_by_id: int | None | Unset = UNSET
    last_changed_by_id: int | None | Unset = UNSET
    format_mask: None | str | Unset = UNSET
    table_entries_id: int | Unset = UNSET
    is_active: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        type_ = self.type_.value

        format_ = self.format_.value

        sequence: int | None | Unset
        if isinstance(self.sequence, Unset):
            sequence = UNSET
        else:
            sequence = self.sequence

        is_system_entry = self.is_system_entry

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

        format_mask: None | str | Unset
        if isinstance(self.format_mask, Unset):
            format_mask = UNSET
        else:
            format_mask = self.format_mask

        table_entries_id = self.table_entries_id

        is_active = self.is_active

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "description": description,
                "type": type_,
                "format": format_,
            }
        )
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if is_system_entry is not UNSET:
            field_dict["is_system_entry"] = is_system_entry
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_changed is not UNSET:
            field_dict["date_changed"] = date_changed
        if added_by_id is not UNSET:
            field_dict["added_by_id"] = added_by_id
        if last_changed_by_id is not UNSET:
            field_dict["last_changed_by_id"] = last_changed_by_id
        if format_mask is not UNSET:
            field_dict["format_mask"] = format_mask
        if table_entries_id is not UNSET:
            field_dict["table_entries_id"] = table_entries_id
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        type_ = PhoneTypePhoneNumberType(d.pop("type"))

        format_ = PhoneTypePhoneFormat(d.pop("format"))

        def _parse_sequence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequence = _parse_sequence(d.pop("sequence", UNSET))

        is_system_entry = d.pop("is_system_entry", UNSET)

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

        last_changed_by_id = _parse_last_changed_by_id(d.pop("last_changed_by_id", UNSET))

        def _parse_format_mask(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_mask = _parse_format_mask(d.pop("format_mask", UNSET))

        table_entries_id = d.pop("table_entries_id", UNSET)

        is_active = d.pop("is_active", UNSET)

        phone_type = cls(
            description=description,
            type_=type_,
            format_=format_,
            sequence=sequence,
            is_system_entry=is_system_entry,
            date_added=date_added,
            date_changed=date_changed,
            added_by_id=added_by_id,
            last_changed_by_id=last_changed_by_id,
            format_mask=format_mask,
            table_entries_id=table_entries_id,
            is_active=is_active,
        )

        return phone_type
