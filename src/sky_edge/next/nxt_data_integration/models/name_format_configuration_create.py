from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.name_format_configuration_field_detail import (
        NameFormatConfigurationFieldDetail,
    )


T = TypeVar("T", bound="NameFormatConfigurationCreate")


@_attrs_define
class NameFormatConfigurationCreate:
    """Name format configurations provide a preset layout to display a constituent's name.

    Attributes:
        fields (list[NameFormatConfigurationFieldDetail]): The collection of configurations for name format fields.
    """

    fields: list[NameFormatConfigurationFieldDetail]

    def to_dict(self) -> dict[str, Any]:
        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "fields": fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.name_format_configuration_field_detail import (
            NameFormatConfigurationFieldDetail,
        )

        d = dict(src_dict)
        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = NameFormatConfigurationFieldDetail.from_dict(fields_item_data)

            fields.append(fields_item)

        name_format_configuration_create = cls(
            fields=fields,
        )

        return name_format_configuration_create
