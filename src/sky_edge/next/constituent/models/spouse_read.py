from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="SpouseRead")


@_attrs_define
class SpouseRead:
    """The spouse entity describes spouses for individual constituents.

    Attributes:
        id (str | Unset): The immutable system record ID of the spouse.
        first (str | Unset): The spouse's first name.
        last (str | Unset): The spouse's last name.
        is_head_of_household (bool | Unset): Indicates whether the spouse is the head household. Only applies to
            constituent spouses.
    """

    id: str | Unset = UNSET
    first: str | Unset = UNSET
    last: str | Unset = UNSET
    is_head_of_household: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        first = self.first

        last = self.last

        is_head_of_household = self.is_head_of_household

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if first is not UNSET:
            field_dict["first"] = first
        if last is not UNSET:
            field_dict["last"] = last
        if is_head_of_household is not UNSET:
            field_dict["is_head_of_household"] = is_head_of_household

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        first = d.pop("first", UNSET)

        last = d.pop("last", UNSET)

        is_head_of_household = d.pop("is_head_of_household", UNSET)

        spouse_read = cls(
            id=id,
            first=first,
            last=last,
            is_head_of_household=is_head_of_household,
        )

        spouse_read.additional_properties = d
        return spouse_read

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
