from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="NameFormatConfigurationFieldEdit")


@_attrs_define
class NameFormatConfigurationFieldEdit:
    """A name format configuration represents the layout to display a constituent's name.

    Attributes:
        field_name (str): The field name.
    """

    field_name: str

    def to_dict(self) -> dict[str, Any]:
        field_name = self.field_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "field_name": field_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_name = d.pop("field_name")

        name_format_configuration_field_edit = cls(
            field_name=field_name,
        )

        return name_format_configuration_field_edit
