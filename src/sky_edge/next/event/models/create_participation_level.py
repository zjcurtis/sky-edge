from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateParticipationLevel")


@_attrs_define
class CreateParticipationLevel:
    """Participation levels are the level of involvement participants have in an event.

    Attributes:
        name (str): The name of the participation level.
    """

    name: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        create_participation_level = cls(
            name=name,
        )

        return create_participation_level
