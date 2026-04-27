from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OnlinePresenceEdit")


@_attrs_define
class OnlinePresenceEdit:
    """Online presence entities store a constituent’s social media accounts, websites, and other means of reaching out or
    gaining more information about the constituent.

        Attributes:
            address (str | Unset): The web address for the online presence. This property cannot be set to null.
            inactive (bool | Unset): Indicates whether the online presence is inactive.
            primary (bool | Unset): Indicates whether this is the constituent's primary online presence.
            type_ (str | Unset): The online presence type. Available values are the entries in the <a href="https://develope
                r.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListOnlinePresenceTypes"><b>Phone
                Types</b></a> table. This property cannot be set to null.
    """

    address: str | Unset = UNSET
    inactive: bool | Unset = UNSET
    primary: bool | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        inactive = self.inactive

        primary = self.primary

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if primary is not UNSET:
            field_dict["primary"] = primary
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address", UNSET)

        inactive = d.pop("inactive", UNSET)

        primary = d.pop("primary", UNSET)

        type_ = d.pop("type", UNSET)

        online_presence_edit = cls(
            address=address,
            inactive=inactive,
            primary=primary,
            type_=type_,
        )

        online_presence_edit.additional_properties = d
        return online_presence_edit

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
