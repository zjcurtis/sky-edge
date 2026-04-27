from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_field_write import FilterFieldWrite


T = TypeVar("T", bound="SummaryFieldWrite")


@_attrs_define
class SummaryFieldWrite:
    """Definition of a summary field.  Select, output, and sort fields reference these by query_field_id and
    summary_instance.

        Attributes:
            query_field_id (int): The query field ID of the summary field
            summary_instance (int): An additional identifier to differentiate multiple instances of the same summary field
                (query_field_id) used on a query.
                The combinations of query_field_id and summary_instance must be unique in the collection of summary_fields on a
                query.
                This value becomes part of the field name in the query UI (again, to differentiate multiple instances of the
                same summary field on the query),
                so it is recommended to start your sequence at 1 for each query_field_id and proceed sequentially for any
                additional instances of the same query_field_id.
            filter_fields (list[FilterFieldWrite] | None | Unset): The filters on this summary field
    """

    query_field_id: int
    summary_instance: int
    filter_fields: list[FilterFieldWrite] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        query_field_id = self.query_field_id

        summary_instance = self.summary_instance

        filter_fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.filter_fields, Unset):
            filter_fields = UNSET
        elif isinstance(self.filter_fields, list):
            filter_fields = []
            for filter_fields_type_0_item_data in self.filter_fields:
                filter_fields_type_0_item = filter_fields_type_0_item_data.to_dict()
                filter_fields.append(filter_fields_type_0_item)

        else:
            filter_fields = self.filter_fields

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "query_field_id": query_field_id,
                "summary_instance": summary_instance,
            }
        )
        if filter_fields is not UNSET:
            field_dict["filter_fields"] = filter_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_field_write import FilterFieldWrite

        d = dict(src_dict)
        query_field_id = d.pop("query_field_id")

        summary_instance = d.pop("summary_instance")

        def _parse_filter_fields(data: object) -> list[FilterFieldWrite] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filter_fields_type_0 = []
                _filter_fields_type_0 = data
                for filter_fields_type_0_item_data in _filter_fields_type_0:
                    filter_fields_type_0_item = FilterFieldWrite.from_dict(
                        filter_fields_type_0_item_data
                    )

                    filter_fields_type_0.append(filter_fields_type_0_item)

                return filter_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FilterFieldWrite] | None | Unset, data)

        filter_fields = _parse_filter_fields(d.pop("filter_fields", UNSET))

        summary_field_write = cls(
            query_field_id=query_field_id,
            summary_instance=summary_instance,
            filter_fields=filter_fields,
        )

        return summary_field_write
