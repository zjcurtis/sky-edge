from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditParticipationLevel")


@_attrs_define
class EditParticipationLevel:
    """Participation levels are the level of involvement participants have in an event.

    Attributes:
        name (None | str | Unset): Description of the participation level.
        is_inactive (bool | Unset): Whether the participation level is active or not.
    """

    name: None | str | Unset = UNSET
    is_inactive: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        is_inactive = self.is_inactive

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if is_inactive is not UNSET:
            field_dict["is_inactive"] = is_inactive

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

        is_inactive = d.pop("is_inactive", UNSET)

        edit_participation_level = cls(
            name=name,
            is_inactive=is_inactive,
        )

        return edit_participation_level
