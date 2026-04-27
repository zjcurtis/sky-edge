from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

from ..models.primary_name_format_read_primary_type import (
    PrimaryNameFormatReadPrimaryType,
)

T = TypeVar("T", bound="PrimaryNameFormatRead")


@_attrs_define
class PrimaryNameFormatRead:
    """Primary name formats are elevated name formats used for the constituent's most commonly used addressee and
    salutation name formats.

        Attributes:
            id (str | Unset): The immutable system record ID of the primary name format.
            configuration_id (str | Unset): The primary name format configuration identifier.
            constituent_id (str | Unset): The immutable system record ID of the constituent associated with the primary name
                format.
            custom_format (bool | Unset): Whether the primary name format uses a custom format.
            formatted_name (str | Unset): The primary name format formatted name.
            primary_type (PrimaryNameFormatReadPrimaryType | Unset): The primary name format primary type.
    """

    id: str | Unset = UNSET
    configuration_id: str | Unset = UNSET
    constituent_id: str | Unset = UNSET
    custom_format: bool | Unset = UNSET
    formatted_name: str | Unset = UNSET
    primary_type: PrimaryNameFormatReadPrimaryType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        configuration_id = self.configuration_id

        constituent_id = self.constituent_id

        custom_format = self.custom_format

        formatted_name = self.formatted_name

        primary_type: str | Unset = UNSET
        if not isinstance(self.primary_type, Unset):
            primary_type = self.primary_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if configuration_id is not UNSET:
            field_dict["configuration_id"] = configuration_id
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if custom_format is not UNSET:
            field_dict["custom_format"] = custom_format
        if formatted_name is not UNSET:
            field_dict["formatted_name"] = formatted_name
        if primary_type is not UNSET:
            field_dict["primary_type"] = primary_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        configuration_id = d.pop("configuration_id", UNSET)

        constituent_id = d.pop("constituent_id", UNSET)

        custom_format = d.pop("custom_format", UNSET)

        formatted_name = d.pop("formatted_name", UNSET)

        _primary_type = d.pop("primary_type", UNSET)
        primary_type: PrimaryNameFormatReadPrimaryType | Unset
        if isinstance(_primary_type, Unset):
            primary_type = UNSET
        else:
            primary_type = PrimaryNameFormatReadPrimaryType(_primary_type)

        primary_name_format_read = cls(
            id=id,
            configuration_id=configuration_id,
            constituent_id=constituent_id,
            custom_format=custom_format,
            formatted_name=formatted_name,
            primary_type=primary_type,
        )

        primary_name_format_read.additional_properties = d
        return primary_name_format_read

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
