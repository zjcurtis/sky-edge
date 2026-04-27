from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="SelectedFilter")


@_attrs_define
class SelectedFilter:
    """Represents a filter that is present but has not been applied

    Attributes:
        field_id (None | str | Unset): The identifier of the field the filter applies to
    """

    field_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        field_id: None | str | Unset
        if isinstance(self.field_id, Unset):
            field_id = UNSET
        else:
            field_id = self.field_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if field_id is not UNSET:
            field_dict["field_id"] = field_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_field_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_id = _parse_field_id(d.pop("field_id", UNSET))

        selected_filter = cls(
            field_id=field_id,
        )

        return selected_filter
