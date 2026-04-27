from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="SelectFieldWrite")


@_attrs_define
class SelectFieldWrite:
    """A query field returned as part of the results (SELECT clause)

    Attributes:
        query_field_id (int | Unset): ID of the query field
        unique_id (None | str | Unset): The attribute type ID, or the specific type ID
        user_alias (None | str | Unset): User's name overriding the standard field name in the output
        summary_instance (int | None | Unset): For select fields referencing summary fields, the summary_instance of the
            summary field.
    """

    query_field_id: int | Unset = UNSET
    unique_id: None | str | Unset = UNSET
    user_alias: None | str | Unset = UNSET
    summary_instance: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        query_field_id = self.query_field_id

        unique_id: None | str | Unset
        if isinstance(self.unique_id, Unset):
            unique_id = UNSET
        else:
            unique_id = self.unique_id

        user_alias: None | str | Unset
        if isinstance(self.user_alias, Unset):
            user_alias = UNSET
        else:
            user_alias = self.user_alias

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
        if user_alias is not UNSET:
            field_dict["user_alias"] = user_alias
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

        def _parse_user_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_alias = _parse_user_alias(d.pop("user_alias", UNSET))

        def _parse_summary_instance(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        summary_instance = _parse_summary_instance(d.pop("summary_instance", UNSET))

        select_field_write = cls(
            query_field_id=query_field_id,
            unique_id=unique_id,
            user_alias=user_alias,
            summary_instance=summary_instance,
        )

        return select_field_write
