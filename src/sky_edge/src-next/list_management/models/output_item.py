from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputItem")


@_attrs_define
class OutputItem:
    """Represents an individual item in the output of a query execution.

    Attributes:
        field_id (None | str | Unset): Filter information for a specific field
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

        output_item = cls(
            field_id=field_id,
        )

        return output_item
