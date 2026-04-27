from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.custom_field_category_create_custom_field_category_data_type import (
    CustomFieldCategoryCreateCustomFieldCategoryDataType,
)
from ..models.custom_field_category_create_custom_field_category_record_type import (
    CustomFieldCategoryCreateCustomFieldCategoryRecordType,
)

T = TypeVar("T", bound="CustomFieldCategoryCreate")


@_attrs_define
class CustomFieldCategoryCreate:
    """
    Attributes:
        record_type (CustomFieldCategoryCreateCustomFieldCategoryRecordType): The type of record (e.g., constituent,
            gift or action) to which the custom field category applies.
        description (str): The custom field category description.
        data_type (CustomFieldCategoryCreateCustomFieldCategoryDataType): The data type for the custom field category.
        id (int | Unset): The unique identifier for the custom field category.
        code_table_id (int | None | Unset): The code table ID for the custom field category.
        is_required (bool | Unset): Value to indicate whether the custom field category is required.
        is_unique (bool | Unset): Value to indicate whether the custom field category is unique.
        is_active (bool | Unset): Value to indicate whether the custom field category is active. Default: True.
        sequence (int | None | Unset): The numeric sequence associated with the custom field category.
    """

    record_type: CustomFieldCategoryCreateCustomFieldCategoryRecordType
    description: str
    data_type: CustomFieldCategoryCreateCustomFieldCategoryDataType
    id: int | Unset = UNSET
    code_table_id: int | None | Unset = UNSET
    is_required: bool | Unset = UNSET
    is_unique: bool | Unset = UNSET
    is_active: bool | Unset = True
    sequence: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        record_type = self.record_type.value

        description = self.description

        data_type = self.data_type.value

        id = self.id

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
                "record_type": record_type,
                "description": description,
                "data_type": data_type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
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
        record_type = CustomFieldCategoryCreateCustomFieldCategoryRecordType(
            d.pop("record_type")
        )

        description = d.pop("description")

        data_type = CustomFieldCategoryCreateCustomFieldCategoryDataType(
            d.pop("data_type")
        )

        id = d.pop("id", UNSET)

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

        custom_field_category_create = cls(
            record_type=record_type,
            description=description,
            data_type=data_type,
            id=id,
            code_table_id=code_table_id,
            is_required=is_required,
            is_unique=is_unique,
            is_active=is_active,
            sequence=sequence,
        )

        return custom_field_category_create
