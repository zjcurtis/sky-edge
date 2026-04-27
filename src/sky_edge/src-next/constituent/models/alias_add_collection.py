from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alias_add_collection_alias import AliasAddCollectionAlias


T = TypeVar("T", bound="AliasAddCollection")


@_attrs_define
class AliasAddCollection:
    """Aliases provide secondary identification for individuals or organizations. For example, aliases can be stage names
    or acronyms.

        Attributes:
            aliases (list[AliasAddCollectionAlias]): Collection of aliases to add
    """

    aliases: list[AliasAddCollectionAlias]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aliases = []
        for aliases_item_data in self.aliases:
            aliases_item = aliases_item_data.to_dict()
            aliases.append(aliases_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aliases": aliases,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alias_add_collection_alias import AliasAddCollectionAlias

        d = dict(src_dict)
        aliases = []
        _aliases = d.pop("aliases")
        for aliases_item_data in _aliases:
            aliases_item = AliasAddCollectionAlias.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        alias_add_collection = cls(
            aliases=aliases,
        )

        alias_add_collection.additional_properties = d
        return alias_add_collection

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
