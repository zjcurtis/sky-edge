from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.phone_format import PhoneFormat
from ..models.phone_number_type import PhoneNumberType
from ..models.ratings_data_type import RatingsDataType

T = TypeVar("T", bound="TableEntryEdit")


@_attrs_define
class TableEntryEdit:
    """Table entry to update

    Attributes:
        long_description (str): The long description of the entry.
        is_active (bool | Unset): The active status of the entry.
        short_description (None | str | Unset): The short description of the entry. Only supported by entries of certain
            tables, such as constituent codes.
        numeric_value (float | None | Unset): The numeric value of the entry. Also known as minimum amount for
            Gift/Donor table entries.
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

    long_description: str
    is_active: bool | Unset = UNSET
    short_description: None | str | Unset = UNSET
    numeric_value: float | None | Unset = UNSET
    phone_format: PhoneFormat | Unset = UNSET
    phone_type: PhoneNumberType | Unset = UNSET
    ratings_data_type: RatingsDataType | Unset = UNSET
    table_number: None | str | Unset = UNSET

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

        table_entry_edit = cls(
            long_description=long_description,
            is_active=is_active,
            short_description=short_description,
            numeric_value=numeric_value,
            phone_format=phone_format,
            phone_type=phone_type,
            ratings_data_type=ratings_data_type,
            table_number=table_number,
        )

        return table_entry_edit
