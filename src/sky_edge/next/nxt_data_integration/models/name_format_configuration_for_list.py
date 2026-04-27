from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="NameFormatConfigurationForList")


@_attrs_define
class NameFormatConfigurationForList:
    """A record from the dbo.SALUTATION table in Raiser's Edge.

    Attributes:
        id (int | Unset): The unique identifier for the name format configuration.
        example (None | str | Unset): The text example for the name format configuration field.
    """

    id: int | Unset = UNSET
    example: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        example: None | str | Unset
        if isinstance(self.example, Unset):
            example = UNSET
        else:
            example = self.example

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if example is not UNSET:
            field_dict["example"] = example

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_example(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        example = _parse_example(d.pop("example", UNSET))

        name_format_configuration_for_list = cls(
            id=id,
            example=example,
        )

        return name_format_configuration_for_list
