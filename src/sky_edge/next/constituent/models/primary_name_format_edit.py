from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="PrimaryNameFormatEdit")


@_attrs_define
class PrimaryNameFormatEdit:
    """Primary name formats are elevated name formats used for the constituent's most commonly used addressee and
    salutation name formats.

        Attributes:
            configuration_id (str | Unset): The name format configuration identifier. Required when custom_format is false.
            custom_format (bool | Unset): Whether the name format uses a custom format.
            formatted_name (str | Unset): The name format formatted name. Required when custom_format is true. Character
                limit: 255.
    """

    configuration_id: str | Unset = UNSET
    custom_format: bool | Unset = UNSET
    formatted_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration_id = self.configuration_id

        custom_format = self.custom_format

        formatted_name = self.formatted_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configuration_id is not UNSET:
            field_dict["configuration_id"] = configuration_id
        if custom_format is not UNSET:
            field_dict["custom_format"] = custom_format
        if formatted_name is not UNSET:
            field_dict["formatted_name"] = formatted_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        configuration_id = d.pop("configuration_id", UNSET)

        custom_format = d.pop("custom_format", UNSET)

        formatted_name = d.pop("formatted_name", UNSET)

        primary_name_format_edit = cls(
            configuration_id=configuration_id,
            custom_format=custom_format,
            formatted_name=formatted_name,
        )

        primary_name_format_edit.additional_properties = d
        return primary_name_format_edit

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
