from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="CountryRead")


@_attrs_define
class CountryRead:
    """The country entity returns information about countries that are available for use in your database.

    Attributes:
        id (str | Unset): The immutable system record ID of the country.
        abbreviation (str | Unset): The user-defined abbreviation for the country.
        name (str | Unset): The country name.
    """

    id: str | Unset = UNSET
    abbreviation: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        abbreviation = self.abbreviation

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        name = d.pop("name", UNSET)

        country_read = cls(
            id=id,
            abbreviation=abbreviation,
            name=name,
        )

        country_read.additional_properties = d
        return country_read

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
