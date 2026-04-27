from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.custom_field_category_custom_field_category_data_type import (
    CustomFieldCategoryCustomFieldCategoryDataType,
)
from ..models.custom_field_category_custom_field_category_record_type import (
    CustomFieldCategoryCustomFieldCategoryRecordType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldCategory")


@_attrs_define
class CustomFieldCategory:
    """
    Attributes:
        id (int | Unset): The unique identifier for the custom field category.
        record_type (CustomFieldCategoryCustomFieldCategoryRecordType | Unset): The type of record (e.g., constituent,
            gift or action) to which the custom field category applies.
        description (None | str | Unset): The custom field category description.
        data_type (CustomFieldCategoryCustomFieldCategoryDataType | Unset): The data type for the custom field category.
        code_table_id (int | None | Unset): The code table ID for the custom field category.
        is_required (bool | Unset): Value to indicate whether the custom field category is required.
        is_unique (bool | Unset): Value to indicate whether the custom field category is unique.
        is_active (bool | Unset): Value to indicate whether the custom field category is active.
        sequence (int | None | Unset): The numeric sequence associated with the custom field category.
        code_table (None | str | Unset): The code table associated with the custom field category.
    """

    id: int | Unset = UNSET
    record_type: CustomFieldCategoryCustomFieldCategoryRecordType | Unset = UNSET
    description: None | str | Unset = UNSET
    data_type: CustomFieldCategoryCustomFieldCategoryDataType | Unset = UNSET
    code_table_id: int | None | Unset = UNSET
    is_required: bool | Unset = UNSET
    is_unique: bool | Unset = UNSET
    is_active: bool | Unset = UNSET
    sequence: int | None | Unset = UNSET
    code_table: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        record_type: str | Unset = UNSET
        if not isinstance(self.record_type, Unset):
            record_type = self.record_type.value

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        data_type: str | Unset = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        code_table_id: int | None | Unset
        if isinstance(self.code_table_id, Unset):
            code_table_id = UNSET
        else:
            code_table_id = self.code_table_id

        is_required = self.is_required

        is_unique = self.is_unique

        is_active = self.is_active

        sequence: int | None | Unset
        if isinstance(self.sequence, Unset):
            sequence = UNSET
        else:
            sequence = self.sequence

        code_table: None | str | Unset
        if isinstance(self.code_table, Unset):
            code_table = UNSET
        else:
            code_table = self.code_table

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if record_type is not UNSET:
            field_dict["record_type"] = record_type
        if description is not UNSET:
            field_dict["description"] = description
        if data_type is not UNSET:
            field_dict["data_type"] = data_type
        if code_table_id is not UNSET:
            field_dict["code_table_id"] = code_table_id
        if is_required is not UNSET:
            field_dict["is_required"] = is_required
        if is_unique is not UNSET:
            field_dict["is_unique"] = is_unique
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if code_table is not UNSET:
            field_dict["code_table"] = code_table

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _record_type = d.pop("record_type", UNSET)
        record_type: CustomFieldCategoryCustomFieldCategoryRecordType | Unset
        if isinstance(_record_type, Unset):
            record_type = UNSET
        else:
            record_type = CustomFieldCategoryCustomFieldCategoryRecordType(_record_type)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _data_type = d.pop("data_type", UNSET)
        data_type: CustomFieldCategoryCustomFieldCategoryDataType | Unset
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = CustomFieldCategoryCustomFieldCategoryDataType(_data_type)

        def _parse_code_table_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        code_table_id = _parse_code_table_id(d.pop("code_table_id", UNSET))

        is_required = d.pop("is_required", UNSET)

        is_unique = d.pop("is_unique", UNSET)

        is_active = d.pop("is_active", UNSET)

        def _parse_sequence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequence = _parse_sequence(d.pop("sequence", UNSET))

        def _parse_code_table(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code_table = _parse_code_table(d.pop("code_table", UNSET))

        custom_field_category = cls(
            id=id,
            record_type=record_type,
            description=description,
            data_type=data_type,
            code_table_id=code_table_id,
            is_required=is_required,
            is_unique=is_unique,
            is_active=is_active,
            sequence=sequence,
            code_table=code_table,
        )

        return custom_field_category
