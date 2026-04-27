from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="EditEventCategory")


@_attrs_define
class EditEventCategory:
    """Event categories help group different types of events.

    Attributes:
        name (None | str | Unset): The name of the event category.
        inactive (bool | Unset): Whether the category is inactive. True if inactive.
    """

    name: None | str | Unset = UNSET
    inactive: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        inactive = self.inactive

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if inactive is not UNSET:
            field_dict["inactive"] = inactive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        inactive = d.pop("inactive", UNSET)

        edit_event_category = cls(
            name=name,
            inactive=inactive,
        )

        return edit_event_category
