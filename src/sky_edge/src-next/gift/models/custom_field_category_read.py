from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_field_category_read_type import CustomFieldCategoryReadType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldCategoryRead")


@_attrs_define
class CustomFieldCategoryRead:
    """The system includes many different types of custom fields. Custom field categories store the metadata to
    appropriately match how you use a given custom field with an available type.

        Attributes:
            name (str | Unset): The name of the custom field category.
            type_ (CustomFieldCategoryReadType | Unset): The type of data that custom fields with this category represent.
                Available values are listed below.
            code_table_id (str | Unset): The code table identifier when the custom field category DataType is
                CodeTableEntry.
            one_per_record (bool | Unset): Flag indicating that only one value for the custom field category is allowed per
                record.
    """

    name: str | Unset = UNSET
    type_: CustomFieldCategoryReadType | Unset = UNSET
    code_table_id: str | Unset = UNSET
    one_per_record: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        code_table_id = self.code_table_id

        one_per_record = self.one_per_record

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if code_table_id is not UNSET:
            field_dict["code_table_id"] = code_table_id
        if one_per_record is not UNSET:
            field_dict["one_per_record"] = one_per_record

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: CustomFieldCategoryReadType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CustomFieldCategoryReadType(_type_)

        code_table_id = d.pop("code_table_id", UNSET)

        one_per_record = d.pop("one_per_record", UNSET)

        custom_field_category_read = cls(
            name=name,
            type_=type_,
            code_table_id=code_table_id,
            one_per_record=one_per_record,
        )

        custom_field_category_read.additional_properties = d
        return custom_field_category_read

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
