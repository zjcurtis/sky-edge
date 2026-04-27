from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NameFormatConfigurationField")


@_attrs_define
class NameFormatConfigurationField:
    """A record from the dbo.SALUTATION_FIELDS table in Raiser's Edge.

    Attributes:
        id (int): The immutable system record ID of the name format configuration field.
        field_name (str): The field name.
        is_system (bool | Unset): The value indicating whether the field is a system field.
    """

    id: int
    field_name: str
    is_system: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field_name = self.field_name

        is_system = self.is_system

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "field_name": field_name,
            }
        )
        if is_system is not UNSET:
            field_dict["is_system"] = is_system

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        field_name = d.pop("field_name")

        is_system = d.pop("is_system", UNSET)

        name_format_configuration_field = cls(
            id=id,
            field_name=field_name,
            is_system=is_system,
        )

        return name_format_configuration_field
