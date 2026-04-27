from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LinkedGiftEdit")


@_attrs_define
class LinkedGiftEdit:
    """Edit a single linked gift on a membership.

    Attributes:
        applied_amount (float): The amount to apply from the gift to the membership.
    """

    applied_amount: float

    def to_dict(self) -> dict[str, Any]:
        applied_amount = self.applied_amount

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "applied_amount": applied_amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        applied_amount = d.pop("applied_amount")

        linked_gift_edit = cls(
            applied_amount=applied_amount,
        )

        return linked_gift_edit
