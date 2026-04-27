from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PhoneAddCollectionPhone")


@_attrs_define
class PhoneAddCollectionPhone:
    """Phones store information about constituent phone numbers and where to call individuals and organizations.

    Attributes:
        number (str): The phone number.
        type_ (str): The phone type. Available values are the entries in the <a href="https://developer.sky.blackbaud.co
            m/docs/services/56b76470069a0509c8f1c5b3/operations/ListPhoneTypes"><b>Phone Types</b></a> table.
        do_not_call (bool | Unset): Indicates whether the constituent requests not to be contacted at this number.
        inactive (bool | Unset): Indicates whether the phone is inactive.
        primary (bool | Unset): Indicates whether this is the constituent's primary phone.
    """

    number: str
    type_: str
    do_not_call: bool | Unset = UNSET
    inactive: bool | Unset = UNSET
    primary: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        type_ = self.type_

        do_not_call = self.do_not_call

        inactive = self.inactive

        primary = self.primary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "number": number,
                "type": type_,
            }
        )
        if do_not_call is not UNSET:
            field_dict["do_not_call"] = do_not_call
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number = d.pop("number")

        type_ = d.pop("type")

        do_not_call = d.pop("do_not_call", UNSET)

        inactive = d.pop("inactive", UNSET)

        primary = d.pop("primary", UNSET)

        phone_add_collection_phone = cls(
            number=number,
            type_=type_,
            do_not_call=do_not_call,
            inactive=inactive,
            primary=primary,
        )

        phone_add_collection_phone.additional_properties = d
        return phone_add_collection_phone

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
