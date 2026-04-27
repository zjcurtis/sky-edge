from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.name_format_configuration_field_detail import NameFormatConfigurationFieldDetail


T = TypeVar("T", bound="NameFormatConfiguration")


@_attrs_define
class NameFormatConfiguration:
    """A record from the dbo.SALUTATIONS table in Raiser's Edge.

    Attributes:
        fields (list[NameFormatConfigurationFieldDetail]): The collection of configurations for name format fields.
        id (int | Unset): The unique identifier for the name format configuration.
    """

    fields: list[NameFormatConfigurationFieldDetail]
    id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "fields": fields,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.name_format_configuration_field_detail import NameFormatConfigurationFieldDetail

        d = dict(src_dict)
        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = NameFormatConfigurationFieldDetail.from_dict(fields_item_data)

            fields.append(fields_item)

        id = d.pop("id", UNSET)

        name_format_configuration = cls(
            fields=fields,
            id=id,
        )

        return name_format_configuration
