from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.available_fields_search_result import AvailableFieldsSearchResult


T = TypeVar("T", bound="AvailableFieldsSearchResponse")


@_attrs_define
class AvailableFieldsSearchResponse:
    """Results of an available field search

    Attributes:
        limit (int): The limit on the search request.
        available_fields (list[AvailableFieldsSearchResult] | None | Unset): Available nodes/fields that match the
            search criteria.
        continuation_token (None | str | Unset): A value will be returned here if not all possible results have been
            returned.
            To get the next page of results, make another request with this token and the same search criteria.
    """

    limit: int
    available_fields: list[AvailableFieldsSearchResult] | None | Unset = UNSET
    continuation_token: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        available_fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.available_fields, Unset):
            available_fields = UNSET
        elif isinstance(self.available_fields, list):
            available_fields = []
            for available_fields_type_0_item_data in self.available_fields:
                available_fields_type_0_item = (
                    available_fields_type_0_item_data.to_dict()
                )
                available_fields.append(available_fields_type_0_item)

        else:
            available_fields = self.available_fields

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
        if available_fields is not UNSET:
            field_dict["available_fields"] = available_fields
        if continuation_token is not UNSET:
            field_dict["continuation_token"] = continuation_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.available_fields_search_result import AvailableFieldsSearchResult

        d = dict(src_dict)
        limit = d.pop("limit")

        def _parse_available_fields(
            data: object,
        ) -> list[AvailableFieldsSearchResult] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                available_fields_type_0 = []
                _available_fields_type_0 = data
                for available_fields_type_0_item_data in _available_fields_type_0:
                    available_fields_type_0_item = (
                        AvailableFieldsSearchResult.from_dict(
                            available_fields_type_0_item_data
                        )
                    )

                    available_fields_type_0.append(available_fields_type_0_item)

                return available_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AvailableFieldsSearchResult] | None | Unset, data)

        available_fields = _parse_available_fields(d.pop("available_fields", UNSET))

        def _parse_continuation_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        continuation_token = _parse_continuation_token(
            d.pop("continuation_token", UNSET)
        )

        available_fields_search_response = cls(
            limit=limit,
            available_fields=available_fields,
            continuation_token=continuation_token,
        )

        return available_fields_search_response
