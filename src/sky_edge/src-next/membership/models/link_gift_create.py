from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkGiftCreate")


@_attrs_define
class LinkGiftCreate:
    """Create memberships link to gift

    Attributes:
        gift_id (str): Unique ID of gift
        applied_amount (float | Unset): Amount applied from gift to membership.
    """

    gift_id: str
    applied_amount: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        gift_id = self.gift_id

        applied_amount = self.applied_amount

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "gift_id": gift_id,
            }
        )
        if applied_amount is not UNSET:
            field_dict["applied_amount"] = applied_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gift_id = d.pop("gift_id")

        applied_amount = d.pop("applied_amount", UNSET)

        link_gift_create = cls(
            gift_id=gift_id,
            applied_amount=applied_amount,
        )

        return link_gift_create
