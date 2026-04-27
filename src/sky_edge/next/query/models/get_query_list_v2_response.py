from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_summary import QuerySummary


T = TypeVar("T", bound="GetQueryListV2Response")


@_attrs_define
class GetQueryListV2Response:
    """Response model for GET /v2/queries

    Attributes:
        limit (int): The limit on the list request.
        queries (list[QuerySummary] | None | Unset): The requested set of queries.
        any_query_types (bool | Unset): Does the user have access to any query types?
        continuation_token (None | str | Unset): The continuation token when additional pages exist.
    """

    limit: int
    queries: list[QuerySummary] | None | Unset = UNSET
    any_query_types: bool | Unset = UNSET
    continuation_token: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

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

        continuation_token: None | str | Unset
        if isinstance(self.continuation_token, Unset):
            continuation_token = UNSET
        else:
            continuation_token = self.continuation_token

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "limit": limit,
            }
        )
        if queries is not UNSET:
            field_dict["queries"] = queries
        if any_query_types is not UNSET:
            field_dict["any_query_types"] = any_query_types
        if continuation_token is not UNSET:
            field_dict["continuation_token"] = continuation_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_summary import QuerySummary

        d = dict(src_dict)
        limit = d.pop("limit")

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

        def _parse_continuation_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        continuation_token = _parse_continuation_token(
            d.pop("continuation_token", UNSET)
        )

        get_query_list_v2_response = cls(
            limit=limit,
            queries=queries,
            any_query_types=any_query_types,
            continuation_token=continuation_token,
        )

        return get_query_list_v2_response
