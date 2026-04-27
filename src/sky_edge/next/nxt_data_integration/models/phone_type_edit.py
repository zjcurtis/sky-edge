from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.phone_type_edit_phone_format import PhoneTypeEditPhoneFormat
from ..models.phone_type_edit_phone_number_type import PhoneTypeEditPhoneNumberType

T = TypeVar("T", bound="PhoneTypeEdit")


@_attrs_define
class PhoneTypeEdit:
    """RE7 Phone type record base class from the dbo.TableEntries table in Raiser's Edge.

    Attributes:
        description (str): The phone type description.
        type_ (PhoneTypeEditPhoneNumberType): The phone number type.
        format_ (PhoneTypeEditPhoneFormat): The phone number format.
        is_active (bool | Unset): The active status of the phone type.
    """

    description: str
    type_: PhoneTypeEditPhoneNumberType
    format_: PhoneTypeEditPhoneFormat
    is_active: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        type_ = self.type_.value

        format_ = self.format_.value

        is_active = self.is_active

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "description": description,
                "type": type_,
                "format": format_,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        type_ = PhoneTypeEditPhoneNumberType(d.pop("type"))

        format_ = PhoneTypeEditPhoneFormat(d.pop("format"))

        is_active = d.pop("is_active", UNSET)

        phone_type_edit = cls(
            description=description,
            type_=type_,
            format_=format_,
            is_active=is_active,
        )

        return phone_type_edit
