from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AliasRead")


@_attrs_define
class AliasRead:
    """Aliases provide secondary identification for individuals or organizations. For example, aliases can be stage names
    or acronyms.

        Attributes:
            id (str | Unset): The immutable system record ID of the alias.
            constituent_id (str | Unset): The immutable system record ID of the constituent associated with the alias.
            name (str | Unset): The name to use as the constituent's alias.
            type_ (str | Unset): The alias type. Available values are the active entries in the <a href="https://developer.s
                ky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListAliasTypes"><b>Alias Types</b></a> table.
    """

    id: str | Unset = UNSET
    constituent_id: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        constituent_id = self.constituent_id

        name = self.name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        constituent_id = d.pop("constituent_id", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        alias_read = cls(
            id=id,
            constituent_id=constituent_id,
            name=name,
            type_=type_,
        )

        alias_read.additional_properties = d
        return alias_read

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
