from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_field import QueryField


T = TypeVar("T", bound="SelectFieldRead")


@_attrs_define
class SelectFieldRead:
    """A query field returned as part of the results (SELECT clause)

    Attributes:
        query_field (QueryField | Unset): A field available for use in a query
        user_alias (None | str | Unset): User's name overriding the standard field name in the output
        summary_instance (int | None | Unset): For select fields referencing summary fields, the summary_instance of the
            summary field.
    """

    query_field: QueryField | Unset = UNSET
    user_alias: None | str | Unset = UNSET
    summary_instance: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        query_field: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query_field, Unset):
            query_field = self.query_field.to_dict()

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
        if query_field is not UNSET:
            field_dict["query_field"] = query_field
        if user_alias is not UNSET:
            field_dict["user_alias"] = user_alias
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

        select_field_read = cls(
            query_field=query_field,
            user_alias=user_alias,
            summary_instance=summary_instance,
        )

        return select_field_read
