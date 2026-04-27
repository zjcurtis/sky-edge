from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldCategoryRead")


@_attrs_define
class CustomFieldCategoryRead:
    """Represents a custom field category

    Attributes:
        name (None | str | Unset): The name/description of the custom field category.
        type_ (None | str | Unset): The type of data that custom fields with this category represent (as string).
        code_table_id (None | str | Unset): The code table identifier when the custom field category DataType is
            CodeTableEntry.
        one_per_record (bool | None | Unset): Flag indicating that only one value for the custom field category is
            allowed per record.
    """

    name: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    code_table_id: None | str | Unset = UNSET
    one_per_record: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        code_table_id: None | str | Unset
        if isinstance(self.code_table_id, Unset):
            code_table_id = UNSET
        else:
            code_table_id = self.code_table_id

        one_per_record: bool | None | Unset
        if isinstance(self.one_per_record, Unset):
            one_per_record = UNSET
        else:
            one_per_record = self.one_per_record

        field_dict: dict[str, Any] = {}

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_code_table_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code_table_id = _parse_code_table_id(d.pop("code_table_id", UNSET))

        def _parse_one_per_record(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        one_per_record = _parse_one_per_record(d.pop("one_per_record", UNSET))

        custom_field_category_read = cls(
            name=name,
            type_=type_,
            code_table_id=code_table_id,
            one_per_record=one_per_record,
        )

        return custom_field_category_read
