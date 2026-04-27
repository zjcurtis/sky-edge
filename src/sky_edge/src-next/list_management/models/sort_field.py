from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.sort_field_sort_order import SortFieldSortOrder
from ..types import UNSET, Unset

T = TypeVar("T", bound="SortField")


@_attrs_define
class SortField:
    """Defines a sort field

    Attributes:
        field_id (None | str | Unset): The field ID to be sorted on
        sort_order (SortFieldSortOrder | Unset): The sort order
    """

    field_id: None | str | Unset = UNSET
    sort_order: SortFieldSortOrder | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        field_id: None | str | Unset
        if isinstance(self.field_id, Unset):
            field_id = UNSET
        else:
            field_id = self.field_id

        sort_order: str | Unset = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if field_id is not UNSET:
            field_dict["field_id"] = field_id
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_field_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_id = _parse_field_id(d.pop("field_id", UNSET))

        _sort_order = d.pop("sort_order", UNSET)
        sort_order: SortFieldSortOrder | Unset
        if isinstance(_sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = SortFieldSortOrder(_sort_order)

        sort_field = cls(
            field_id=field_id,
            sort_order=sort_order,
        )

        return sort_field
