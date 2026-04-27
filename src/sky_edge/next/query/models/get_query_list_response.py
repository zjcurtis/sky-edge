from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_summary import QuerySummary


T = TypeVar("T", bound="GetQueryListResponse")


@_attrs_define
class GetQueryListResponse:
    """Response model for GET /queries

    Attributes:
        limit (int): The limit on the list request.
        offset (int): The offset on the list request.
        queries (list[QuerySummary] | None | Unset): The requested set of queries.
        any_query_types (bool | Unset): Does the user have access to any query types?
        count (int | Unset): The total number of items in the collection before limit/offset.
    """

    limit: int
    offset: int
    queries: list[QuerySummary] | None | Unset = UNSET
    any_query_types: bool | Unset = UNSET
    count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        offset = self.offset

        queries: list[dict[str, Any]] | None | Unset
        if isinstance(self.queries, Unset):
            queries = UNSET
        elif isinstance(self.queries, list):
            queries = []
            for queries_type_0_item_data in self.queries:
                queries_type_0_item = queries_type_0_item_data.to_dict()
                queries.append(queries_type_0_item)

        else:
            queries = self.queries

        any_query_types = self.any_query_types

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "limit": limit,
                "offset": offset,
            }
        )
        if queries is not UNSET:
            field_dict["queries"] = queries
        if any_query_types is not UNSET:
            field_dict["any_query_types"] = any_query_types
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_summary import QuerySummary

        d = dict(src_dict)
        limit = d.pop("limit")

        offset = d.pop("offset")

        def _parse_queries(data: object) -> list[QuerySummary] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                queries_type_0 = []
                _queries_type_0 = data
                for queries_type_0_item_data in _queries_type_0:
                    queries_type_0_item = QuerySummary.from_dict(
                        queries_type_0_item_data
                    )

                    queries_type_0.append(queries_type_0_item)

                return queries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[QuerySummary] | None | Unset, data)

        queries = _parse_queries(d.pop("queries", UNSET))

        any_query_types = d.pop("any_query_types", UNSET)

        count = d.pop("count", UNSET)

        get_query_list_response = cls(
            limit=limit,
            offset=offset,
            queries=queries,
            any_query_types=any_query_types,
            count=count,
        )

        return get_query_list_response
