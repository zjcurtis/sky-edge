from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="PhoneEdit")


@_attrs_define
class PhoneEdit:
    """Phones store information about constituent phone numbers and where to call individuals and organizations.

    Attributes:
        do_not_call (bool | Unset): Indicates whether the constituent requests not to be contacted at this number.
        inactive (bool | Unset): Indicates whether the phone is inactive.
        number (str | Unset): The phone number. This property cannot be set to null.
        primary (bool | Unset): Indicates whether this is the constituent's primary phone.
        type_ (str | Unset): The phone type. Available values are the entries in the <a href="https://developer.sky.blac
            kbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListPhoneTypes"><b>Phone Types</b></a> table. This
            property cannot be set to null.
    """

    do_not_call: bool | Unset = UNSET
    inactive: bool | Unset = UNSET
    number: str | Unset = UNSET
    primary: bool | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        do_not_call = self.do_not_call

        inactive = self.inactive

        number = self.number

        primary = self.primary

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if do_not_call is not UNSET:
            field_dict["do_not_call"] = do_not_call
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if number is not UNSET:
            field_dict["number"] = number
        if primary is not UNSET:
            field_dict["primary"] = primary
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        do_not_call = d.pop("do_not_call", UNSET)

        inactive = d.pop("inactive", UNSET)

        number = d.pop("number", UNSET)

        primary = d.pop("primary", UNSET)

        type_ = d.pop("type", UNSET)

        phone_edit = cls(
            do_not_call=do_not_call,
            inactive=inactive,
            number=number,
            primary=primary,
            type_=type_,
        )

        phone_edit.additional_properties = d
        return phone_edit

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
