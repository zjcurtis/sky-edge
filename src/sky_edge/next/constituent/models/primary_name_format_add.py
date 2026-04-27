from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

from ..models.primary_name_format_add_primary_type import (
    PrimaryNameFormatAddPrimaryType,
)

T = TypeVar("T", bound="PrimaryNameFormatAdd")


@_attrs_define
class PrimaryNameFormatAdd:
    """Primary name formats are elevated name formats used for the constituent's most commonly used addressee and
    salutation.

        Attributes:
            constituent_id (str): The immutable system record ID of the constituent associated with the primary name format.
            primary_type (PrimaryNameFormatAddPrimaryType): The primary name format type. Available values are
                <i>Addressee</i> and <i>Salutation</i>.
            configuration_id (str | Unset): The primary name format configuration identifier. Required when custom_format is
                false.
            custom_format (bool | Unset): Whether the primary name format uses a custom format. Defaults to false.
            formatted_name (str | Unset): The primary name format formatted name. Required when custom_format is true.
                Character limit: 255.
    """

    constituent_id: str
    primary_type: PrimaryNameFormatAddPrimaryType
    configuration_id: str | Unset = UNSET
    custom_format: bool | Unset = UNSET
    formatted_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        constituent_id = self.constituent_id

        primary_type = self.primary_type.value

        configuration_id = self.configuration_id

        custom_format = self.custom_format

        formatted_name = self.formatted_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "constituent_id": constituent_id,
                "primary_type": primary_type,
            }
        )
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
        constituent_id = d.pop("constituent_id")

        primary_type = PrimaryNameFormatAddPrimaryType(d.pop("primary_type"))

        configuration_id = d.pop("configuration_id", UNSET)

        custom_format = d.pop("custom_format", UNSET)

        formatted_name = d.pop("formatted_name", UNSET)

        primary_name_format_add = cls(
            constituent_id=constituent_id,
            primary_type=primary_type,
            configuration_id=configuration_id,
            custom_format=custom_format,
            formatted_name=formatted_name,
        )

        primary_name_format_add.additional_properties = d
        return primary_name_format_add

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
