from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.custom_field_create import CustomFieldCreate


T = TypeVar("T", bound="CustomFieldsCreate")


@_attrs_define
class CustomFieldsCreate:
    """Represents the custom fields collection data to be added

    Attributes:
        custom_fields (list[CustomFieldCreate]): List of custom fields to be added.
    """

    custom_fields: list[CustomFieldCreate]

    def to_dict(self) -> dict[str, Any]:
        custom_fields = []
        for custom_fields_item_data in self.custom_fields:
            custom_fields_item = custom_fields_item_data.to_dict()
            custom_fields.append(custom_fields_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "custom_fields": custom_fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_field_create import CustomFieldCreate

        d = dict(src_dict)
        custom_fields = []
        _custom_fields = d.pop("custom_fields")
        for custom_fields_item_data in _custom_fields:
            custom_fields_item = CustomFieldCreate.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        custom_fields_create = cls(
            custom_fields=custom_fields,
        )

        return custom_fields_create
