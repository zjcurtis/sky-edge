from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.sort_order import SortOrder

T = TypeVar("T", bound="SortFieldWrite")


@_attrs_define
class SortFieldWrite:
    """A query field used for sorting the results (ORDER BY clause)

    Attributes:
        query_field_id (int | Unset): ID of the query field
        unique_id (None | str | Unset): The attribute type ID, or the specific type ID
        sort_order (SortOrder | Unset): Whether to sort ascending or descending<p>Members:</p><ul><li><i>Ascending</i> -
            Sort ascending</li><li><i>Descending</i> - Sort descending</li></ul>
        summary_instance (int | None | Unset): For sort fields referencing summary fields, the summary_instance of the
            summary field.
    """

    query_field_id: int | Unset = UNSET
    unique_id: None | str | Unset = UNSET
    sort_order: SortOrder | Unset = UNSET
    summary_instance: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        query_field_id = self.query_field_id

        unique_id: None | str | Unset
        if isinstance(self.unique_id, Unset):
            unique_id = UNSET
        else:
            unique_id = self.unique_id

        sort_order: str | Unset = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.value

        summary_instance: int | None | Unset
        if isinstance(self.summary_instance, Unset):
            summary_instance = UNSET
        else:
            summary_instance = self.summary_instance

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if query_field_id is not UNSET:
            field_dict["query_field_id"] = query_field_id
        if unique_id is not UNSET:
            field_dict["unique_id"] = unique_id
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order
        if summary_instance is not UNSET:
            field_dict["summary_instance"] = summary_instance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query_field_id = d.pop("query_field_id", UNSET)

        def _parse_unique_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unique_id = _parse_unique_id(d.pop("unique_id", UNSET))

        _sort_order = d.pop("sort_order", UNSET)
        sort_order: SortOrder | Unset
        if isinstance(_sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = SortOrder(_sort_order)

        def _parse_summary_instance(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        summary_instance = _parse_summary_instance(d.pop("summary_instance", UNSET))

        sort_field_write = cls(
            query_field_id=query_field_id,
            unique_id=unique_id,
            sort_order=sort_order,
            summary_instance=summary_instance,
        )

        return sort_field_write
