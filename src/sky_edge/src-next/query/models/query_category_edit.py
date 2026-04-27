from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryCategoryEdit")


@_attrs_define
class QueryCategoryEdit:
    """Model used to edit a query category

    Attributes:
        sequence (int | Unset): Sequence of the category, affecting order in the list
        name (None | str | Unset): Name of the query category
    """

    sequence: int | Unset = UNSET
    name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        sequence = self.sequence

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sequence = d.pop("sequence", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        query_category_edit = cls(
            sequence=sequence,
            name=name,
        )

        return query_category_edit
