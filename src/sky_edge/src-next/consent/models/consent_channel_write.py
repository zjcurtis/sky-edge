from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ConsentChannelWrite")


@_attrs_define
class ConsentChannelWrite:
    """Defines a model to represent a consent channel write operation.

    Attributes:
        active (bool): Flag indicating whether or not the consent channel is active.
    """

    active: bool

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "active": active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active")

        consent_channel_write = cls(
            active=active,
        )

        return consent_channel_write
