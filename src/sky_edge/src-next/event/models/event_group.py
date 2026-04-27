from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventGroup")


@_attrs_define
class EventGroup:
    """Event group is the custom grouping for the event.

    Attributes:
        id (None | str | Unset): The ID of the event group.
        name (None | str | Unset): The name of the event group.
        is_inactive (bool | Unset): Whether the group is inactive. True if inactive.
    """

    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    is_inactive: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        is_inactive = self.is_inactive

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if is_inactive is not UNSET:
            field_dict["is_inactive"] = is_inactive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        is_inactive = d.pop("is_inactive", UNSET)

        event_group = cls(
            id=id,
            name=name,
            is_inactive=is_inactive,
        )

        return event_group
