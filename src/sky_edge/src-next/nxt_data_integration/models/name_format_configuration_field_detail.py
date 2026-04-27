from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NameFormatConfigurationFieldDetail")


@_attrs_define
class NameFormatConfigurationFieldDetail:
    """Contains the fields needed to configure a field in a constituent name format.

    Attributes:
        field_id (int): The unique identifier for the field.
        sequence (int): The numeric sequence associated with the field.
        initial (bool | Unset): The value used to indicate whether the field is the initial field in a name format.
        comma (bool | Unset): The value used to indicate whether a comma is included in the field.
        conditional_break (bool | Unset): The value used to indicate whether a conditional break is included in the
            field.
        hard_break (bool | Unset): The value used to indicate whether a hard break is included in the field.
        concatenate (bool | Unset): The value used to indicate whether the field can be concatenated.
        smart (bool | Unset): The value used to indicate whether the field is a smart concatenate field; it can be true
            only when preceded by a user-defined field.
    """

    field_id: int
    sequence: int
    initial: bool | Unset = UNSET
    comma: bool | Unset = UNSET
    conditional_break: bool | Unset = UNSET
    hard_break: bool | Unset = UNSET
    concatenate: bool | Unset = UNSET
    smart: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        sequence = self.sequence

        initial = self.initial

        comma = self.comma

        conditional_break = self.conditional_break

        hard_break = self.hard_break

        concatenate = self.concatenate

        smart = self.smart

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "field_id": field_id,
                "sequence": sequence,
            }
        )
        if initial is not UNSET:
            field_dict["initial"] = initial
        if comma is not UNSET:
            field_dict["comma"] = comma
        if conditional_break is not UNSET:
            field_dict["conditional_break"] = conditional_break
        if hard_break is not UNSET:
            field_dict["hard_break"] = hard_break
        if concatenate is not UNSET:
            field_dict["concatenate"] = concatenate
        if smart is not UNSET:
            field_dict["smart"] = smart

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_id = d.pop("field_id")

        sequence = d.pop("sequence")

        initial = d.pop("initial", UNSET)

        comma = d.pop("comma", UNSET)

        conditional_break = d.pop("conditional_break", UNSET)

        hard_break = d.pop("hard_break", UNSET)

        concatenate = d.pop("concatenate", UNSET)

        smart = d.pop("smart", UNSET)

        name_format_configuration_field_detail = cls(
            field_id=field_id,
            sequence=sequence,
            initial=initial,
            comma=comma,
            conditional_break=conditional_break,
            hard_break=hard_break,
            concatenate=concatenate,
            smart=smart,
        )

        return name_format_configuration_field_detail
