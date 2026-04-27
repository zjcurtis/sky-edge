from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_type import QueryType


T = TypeVar("T", bound="GetQueryTypesResponse")


@_attrs_define
class GetQueryTypesResponse:
    """Response model for GET /querytypes

    Attributes:
        query_types (list[QueryType] | None | Unset): The requested set of query types.
        default_query_type_id (int | None | Unset): The ID of the query type to select as the default.
    """

    query_types: list[QueryType] | None | Unset = UNSET
    default_query_type_id: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        query_types: list[dict[str, Any]] | None | Unset
        if isinstance(self.query_types, Unset):
            query_types = UNSET
        elif isinstance(self.query_types, list):
            query_types = []
            for query_types_type_0_item_data in self.query_types:
                query_types_type_0_item = query_types_type_0_item_data.to_dict()
                query_types.append(query_types_type_0_item)

        else:
            query_types = self.query_types

        default_query_type_id: int | None | Unset
        if isinstance(self.default_query_type_id, Unset):
            default_query_type_id = UNSET
        else:
            default_query_type_id = self.default_query_type_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if query_types is not UNSET:
            field_dict["query_types"] = query_types
        if default_query_type_id is not UNSET:
            field_dict["default_query_type_id"] = default_query_type_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_type import QueryType

        d = dict(src_dict)

        def _parse_query_types(data: object) -> list[QueryType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                query_types_type_0 = []
                _query_types_type_0 = data
                for query_types_type_0_item_data in _query_types_type_0:
                    query_types_type_0_item = QueryType.from_dict(
                        query_types_type_0_item_data
                    )

                    query_types_type_0.append(query_types_type_0_item)

                return query_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[QueryType] | None | Unset, data)

        query_types = _parse_query_types(d.pop("query_types", UNSET))

        def _parse_default_query_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        default_query_type_id = _parse_default_query_type_id(
            d.pop("default_query_type_id", UNSET)
        )

        get_query_types_response = cls(
            query_types=query_types,
            default_query_type_id=default_query_type_id,
        )

        return get_query_types_response
