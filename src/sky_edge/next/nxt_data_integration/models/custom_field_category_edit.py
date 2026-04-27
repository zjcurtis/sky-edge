from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.custom_field_category_edit_custom_field_category_data_type import (
    CustomFieldCategoryEditCustomFieldCategoryDataType,
)
from ..models.custom_field_category_edit_custom_field_category_record_type import (
    CustomFieldCategoryEditCustomFieldCategoryRecordType,
)

T = TypeVar("T", bound="CustomFieldCategoryEdit")


@_attrs_define
class CustomFieldCategoryEdit:
    """
    Attributes:
        description (str): The custom field category description.
        id (int | Unset):
        record_type (CustomFieldCategoryEditCustomFieldCategoryRecordType | Unset):
        data_type (CustomFieldCategoryEditCustomFieldCategoryDataType | Unset):
        code_table_id (int | None | Unset):
        is_required (bool | Unset): Value to indicate whether the custom field category is required.
        is_unique (bool | Unset): Value to indicate whether the custom field category is unique.
        is_active (bool | Unset): Value to indicate whether the custom field category is active.
        sequence (int | None | Unset): The numeric sequence associated with the custom field category.
    """

    description: str
    id: int | Unset = UNSET
    record_type: CustomFieldCategoryEditCustomFieldCategoryRecordType | Unset = UNSET
    data_type: CustomFieldCategoryEditCustomFieldCategoryDataType | Unset = UNSET
    code_table_id: int | None | Unset = UNSET
    is_required: bool | Unset = UNSET
    is_unique: bool | Unset = UNSET
    is_active: bool | Unset = UNSET
    sequence: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        id = self.id

        record_type: str | Unset = UNSET
        if not isinstance(self.record_type, Unset):
            record_type = self.record_type.value

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "description": description,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if record_type is not UNSET:
            field_dict["record_type"] = record_type
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        id = d.pop("id", UNSET)

        _record_type = d.pop("record_type", UNSET)
        record_type: CustomFieldCategoryEditCustomFieldCategoryRecordType | Unset
        if isinstance(_record_type, Unset):
            record_type = UNSET
        else:
            record_type = CustomFieldCategoryEditCustomFieldCategoryRecordType(
                _record_type
            )

        _data_type = d.pop("data_type", UNSET)
        data_type: CustomFieldCategoryEditCustomFieldCategoryDataType | Unset
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = CustomFieldCategoryEditCustomFieldCategoryDataType(_data_type)

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

        custom_field_category_edit = cls(
            description=description,
            id=id,
            record_type=record_type,
            data_type=data_type,
            code_table_id=code_table_id,
            is_required=is_required,
            is_unique=is_unique,
            is_active=is_active,
            sequence=sequence,
        )

        return custom_field_category_edit
