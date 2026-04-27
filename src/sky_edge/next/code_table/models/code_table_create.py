from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.code_table_category import CodeTableCategory

T = TypeVar("T", bound="CodeTableCreate")


@_attrs_define
class CodeTableCreate:
    """New code table to be added

    Attributes:
        name (str): The name of the code table.
        category (CodeTableCategory | Unset): The code table categories available. Certain categories are product module
            dependent.
    """

    name: str
    category: CodeTableCategory | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _category = d.pop("category", UNSET)
        category: CodeTableCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = CodeTableCategory(_category)

        code_table_create = cls(
            name=name,
            category=category,
        )

        return code_table_create
