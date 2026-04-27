from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodeTable")


@_attrs_define
class CodeTable:
    """A Code Table record from the dbo.CodeTables table in Raiser's Edge.

    Attributes:
        code_tables_id (int | Unset): The unique identifier for the code table.
        name (None | str | Unset): The name of the code table.
        user_defined (bool | Unset): Indicates whether the code table is user defined.
        has_short_description (bool | Unset): The value indicating whether the code table has a short description.
        short_description_length (int | Unset): The length of the short description.
        hidden_system_table (bool | Unset): The value indicating whether the code table is a hidden system table.
    """

    code_tables_id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    user_defined: bool | Unset = UNSET
    has_short_description: bool | Unset = UNSET
    short_description_length: int | Unset = UNSET
    hidden_system_table: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code_tables_id = self.code_tables_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        user_defined = self.user_defined

        has_short_description = self.has_short_description

        short_description_length = self.short_description_length

        hidden_system_table = self.hidden_system_table

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if code_tables_id is not UNSET:
            field_dict["code_tables_id"] = code_tables_id
        if name is not UNSET:
            field_dict["name"] = name
        if user_defined is not UNSET:
            field_dict["user_defined"] = user_defined
        if has_short_description is not UNSET:
            field_dict["has_short_description"] = has_short_description
        if short_description_length is not UNSET:
            field_dict["short_description_length"] = short_description_length
        if hidden_system_table is not UNSET:
            field_dict["hidden_system_table"] = hidden_system_table

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code_tables_id = d.pop("code_tables_id", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        user_defined = d.pop("user_defined", UNSET)

        has_short_description = d.pop("has_short_description", UNSET)

        short_description_length = d.pop("short_description_length", UNSET)

        hidden_system_table = d.pop("hidden_system_table", UNSET)

        code_table = cls(
            code_tables_id=code_tables_id,
            name=name,
            user_defined=user_defined,
            has_short_description=has_short_description,
            short_description_length=short_description_length,
            hidden_system_table=hidden_system_table,
        )

        return code_table
