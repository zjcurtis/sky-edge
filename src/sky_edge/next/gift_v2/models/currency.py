from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Currency")


@_attrs_define
class Currency:
    """An amount denominated in a specific currency.

    Attributes:
        value (float): The amount. Example: 123.45.
    """

    value: float

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        currency = cls(
            value=value,
        )

        return currency
