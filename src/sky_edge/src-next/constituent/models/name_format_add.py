from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NameFormatAdd")


@_attrs_define
class NameFormatAdd:
    """Name formats define how to address constituents in communications. How you refer to individuals sets the tone of
    your communications with them and how well they receive your interactions.

        Attributes:
            constituent_id (str): The immutable system record ID of the constituent associated with the name format.
            type_ (str): The name format type. Available values are the entries in the <a href="https://developer.sky.blackb
                aud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListNameFormatTypes"><b>Addr/Sal Types</b></a> table.
            configuration_id (str | Unset): The name format configuration identifier. Required when custom_format is false.
            custom_format (bool | Unset): Whether the name format uses a custom format. Defaults to false.
            formatted_name (str | Unset): The name format formatted name. Required when custom_format is true. Character
                limit: 255.
    """

    constituent_id: str
    type_: str
    configuration_id: str | Unset = UNSET
    custom_format: bool | Unset = UNSET
    formatted_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        constituent_id = self.constituent_id

        type_ = self.type_

        configuration_id = self.configuration_id

        custom_format = self.custom_format

        formatted_name = self.formatted_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "constituent_id": constituent_id,
                "type": type_,
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

        type_ = d.pop("type")

        configuration_id = d.pop("configuration_id", UNSET)

        custom_format = d.pop("custom_format", UNSET)

        formatted_name = d.pop("formatted_name", UNSET)

        name_format_add = cls(
            constituent_id=constituent_id,
            type_=type_,
            configuration_id=configuration_id,
            custom_format=custom_format,
            formatted_name=formatted_name,
        )

        name_format_add.additional_properties = d
        return name_format_add

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
