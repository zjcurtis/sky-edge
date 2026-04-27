from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_field_category_add_type import CustomFieldCategoryAddType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldCategoryAdd")


@_attrs_define
class CustomFieldCategoryAdd:
    """Add a new custom field category.

    Attributes:
        name (str): The custom field category name.
        type_ (CustomFieldCategoryAddType): The type of data for the custom field category.
        must_be_unique (bool | Unset): Indicates whether the values on this custom field category are meant to be
            unique. Defaults to false.
    """

    name: str
    type_: CustomFieldCategoryAddType
    must_be_unique: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        must_be_unique = self.must_be_unique

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if must_be_unique is not UNSET:
            field_dict["must_be_unique"] = must_be_unique

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = CustomFieldCategoryAddType(d.pop("type"))

        must_be_unique = d.pop("must_be_unique", UNSET)

        custom_field_category_add = cls(
            name=name,
            type_=type_,
            must_be_unique=must_be_unique,
        )

        custom_field_category_add.additional_properties = d
        return custom_field_category_add

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
