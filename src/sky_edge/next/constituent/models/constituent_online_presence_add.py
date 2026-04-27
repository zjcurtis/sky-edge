from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="ConstituentOnlinePresenceAdd")


@_attrs_define
class ConstituentOnlinePresenceAdd:
    """Defines the shape of an online presence for adding with a constituent.

    Attributes:
        address (str): The web address for the online presence.
        type_ (str): The online presence type. Available values are the entries in the <a href="https://developer.sky.bl
            ackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListOnlinePresenceTypes"><b>Phone Types</b></a>
            table.
        inactive (bool | Unset): Indicates whether the online presence is inactive.
        primary (bool | Unset): Indicates whether this is the constituent's primary online presence.
    """

    address: str
    type_: str
    inactive: bool | Unset = UNSET
    primary: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        type_ = self.type_

        inactive = self.inactive

        primary = self.primary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "type": type_,
            }
        )
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address")

        type_ = d.pop("type")

        inactive = d.pop("inactive", UNSET)

        primary = d.pop("primary", UNSET)

        constituent_online_presence_add = cls(
            address=address,
            type_=type_,
            inactive=inactive,
            primary=primary,
        )

        constituent_online_presence_add.additional_properties = d
        return constituent_online_presence_add

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
