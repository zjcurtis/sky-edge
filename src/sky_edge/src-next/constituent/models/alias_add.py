from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AliasAdd")


@_attrs_define
class AliasAdd:
    """Aliases provide secondary identification for individuals or organizations. For example, aliases can be stage names
    or acronyms.

        Attributes:
            constituent_id (str): The immutable system record ID of the constituent associated with the alias.
            name (str): The name to use as the constituent's alias. Character limit: 100.
            type_ (str | Unset): The alias type. Available values are the active entries in the <a href="https://developer.s
                ky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListAliasTypes"><b>Alias Types</b></a> table.
    """

    constituent_id: str
    name: str
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        constituent_id = self.constituent_id

        name = self.name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "constituent_id": constituent_id,
                "name": name,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        constituent_id = d.pop("constituent_id")

        name = d.pop("name")

        type_ = d.pop("type", UNSET)

        alias_add = cls(
            constituent_id=constituent_id,
            name=name,
            type_=type_,
        )

        alias_add.additional_properties = d
        return alias_add

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
