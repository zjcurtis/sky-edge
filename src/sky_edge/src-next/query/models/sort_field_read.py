from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.sort_order import SortOrder
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_field import QueryField


T = TypeVar("T", bound="SortFieldRead")


@_attrs_define
class SortFieldRead:
    """A query field used for sorting the results (ORDER BY clause)

    Attributes:
        query_field (QueryField | Unset): A field available for use in a query
        sort_order (SortOrder | Unset): Whether to sort ascending or descending<p>Members:</p><ul><li><i>Ascending</i> -
            Sort ascending</li><li><i>Descending</i> - Sort descending</li></ul>
        summary_instance (int | None | Unset): For sort fields referencing summary fields, the summary_instance of the
            summary field.
    """

    query_field: QueryField | Unset = UNSET
    sort_order: SortOrder | Unset = UNSET
    summary_instance: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        query_field: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query_field, Unset):
            query_field = self.query_field.to_dict()

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
        if query_field is not UNSET:
            field_dict["query_field"] = query_field
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order
        if summary_instance is not UNSET:
            field_dict["summary_instance"] = summary_instance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_field import QueryField

        d = dict(src_dict)
        _query_field = d.pop("query_field", UNSET)
        query_field: QueryField | Unset
        if isinstance(_query_field, Unset):
            query_field = UNSET
        else:
            query_field = QueryField.from_dict(_query_field)

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

        sort_field_read = cls(
            query_field=query_field,
            sort_order=sort_order,
            summary_instance=summary_instance,
        )

        return sort_field_read
