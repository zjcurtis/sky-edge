from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.available_fields_search_result_type import AvailableFieldsSearchResultType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AvailableFieldsSearchResult")


@_attrs_define
class AvailableFieldsSearchResult:
    """A matching result from the available fields search.

    Attributes:
        result_type (AvailableFieldsSearchResultType | Unset): Whether the AvailableFieldsSearchResult is a node or a
            field in the available fields tree.<p>Members:</p><ul><li><i>Node</i> - The search result is a
            node.</li><li><i>Field</i> - The search result is a field.</li></ul>
        id_sequence (list[int] | None | Unset): The sequence of node and field IDs from the root node to the matching
            node or field.
        result_path (list[str] | None | Unset): The path of nodes leading to and including the matched node or field.
        rating_unique_id (None | str | Unset): The unique ID of a rating field, null when it is not a rating field
    """

    result_type: AvailableFieldsSearchResultType | Unset = UNSET
    id_sequence: list[int] | None | Unset = UNSET
    result_path: list[str] | None | Unset = UNSET
    rating_unique_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        result_type: str | Unset = UNSET
        if not isinstance(self.result_type, Unset):
            result_type = self.result_type.value

        id_sequence: list[int] | None | Unset
        if isinstance(self.id_sequence, Unset):
            id_sequence = UNSET
        elif isinstance(self.id_sequence, list):
            id_sequence = self.id_sequence

        else:
            id_sequence = self.id_sequence

        result_path: list[str] | None | Unset
        if isinstance(self.result_path, Unset):
            result_path = UNSET
        elif isinstance(self.result_path, list):
            result_path = self.result_path

        else:
            result_path = self.result_path

        rating_unique_id: None | str | Unset
        if isinstance(self.rating_unique_id, Unset):
            rating_unique_id = UNSET
        else:
            rating_unique_id = self.rating_unique_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if result_type is not UNSET:
            field_dict["result_type"] = result_type
        if id_sequence is not UNSET:
            field_dict["id_sequence"] = id_sequence
        if result_path is not UNSET:
            field_dict["result_path"] = result_path
        if rating_unique_id is not UNSET:
            field_dict["rating_unique_id"] = rating_unique_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _result_type = d.pop("result_type", UNSET)
        result_type: AvailableFieldsSearchResultType | Unset
        if isinstance(_result_type, Unset):
            result_type = UNSET
        else:
            result_type = AvailableFieldsSearchResultType(_result_type)

        def _parse_id_sequence(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                id_sequence_type_0 = cast(list[int], data)

                return id_sequence_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        id_sequence = _parse_id_sequence(d.pop("id_sequence", UNSET))

        def _parse_result_path(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                result_path_type_0 = cast(list[str], data)

                return result_path_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        result_path = _parse_result_path(d.pop("result_path", UNSET))

        def _parse_rating_unique_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rating_unique_id = _parse_rating_unique_id(d.pop("rating_unique_id", UNSET))

        available_fields_search_result = cls(
            result_type=result_type,
            id_sequence=id_sequence,
            result_path=result_path,
            rating_unique_id=rating_unique_id,
        )

        return available_fields_search_result
