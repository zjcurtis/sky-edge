from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="MembershipMemberRead")


@_attrs_define
class MembershipMemberRead:
    """Members are constituents who join your organization through memberships that encourage more active involvement.
    Members are usually more involved with your organization than other donors, even if their only contribution is
    routine giving.

        Attributes:
            id (str | Unset): The immutable system record ID of the member.
            constituent_id (str | Unset): The immutable system record ID of the constituent associated with the member.
            primary (bool | Unset): Indicates whether this is the primary member on the membership.
    """

    id: str | Unset = UNSET
    constituent_id: str | Unset = UNSET
    primary: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        constituent_id = self.constituent_id

        primary = self.primary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        constituent_id = d.pop("constituent_id", UNSET)

        primary = d.pop("primary", UNSET)

        membership_member_read = cls(
            id=id,
            constituent_id=constituent_id,
            primary=primary,
        )

        membership_member_read.additional_properties = d
        return membership_member_read

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
