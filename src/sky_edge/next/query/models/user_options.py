from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="UserOptions")


@_attrs_define
class UserOptions:
    """A set of user options for a given environment + user + product

    Attributes:
        display_code_table_long_description (bool | Unset): Display code table entries by long description (instead of
            short description).
    """

    display_code_table_long_description: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        display_code_table_long_description = self.display_code_table_long_description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if display_code_table_long_description is not UNSET:
            field_dict["display_code_table_long_description"] = (
                display_code_table_long_description
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_code_table_long_description = d.pop(
            "display_code_table_long_description", UNSET
        )

        user_options = cls(
            display_code_table_long_description=display_code_table_long_description,
        )

        return user_options
