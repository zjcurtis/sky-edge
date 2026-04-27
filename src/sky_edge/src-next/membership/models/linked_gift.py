from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.linked_gift_gift_type import LinkedGiftGiftType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkedGift")


@_attrs_define
class LinkedGift:
    """Linked gift for a membership record

    Attributes:
        transaction_gift_id (int | Unset): Immutable record ID of the transaction gift link between the gift and the
            membership.
        gift_id (int | Unset): Immutable record ID of the gift record linked to membership.
        gift_type (LinkedGiftGiftType | Unset): Gift type of the linked gift.
        applied_amount (float | Unset): Amount applied from gift to membership.
        constituent_name (None | str | Unset): Name of the constituent associated with the linked gift.
        gift_date (datetime.date | Unset): Gift date for the linked gift.
    """

    transaction_gift_id: int | Unset = UNSET
    gift_id: int | Unset = UNSET
    gift_type: LinkedGiftGiftType | Unset = UNSET
    applied_amount: float | Unset = UNSET
    constituent_name: None | str | Unset = UNSET
    gift_date: datetime.date | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        transaction_gift_id = self.transaction_gift_id

        gift_id = self.gift_id

        gift_type: str | Unset = UNSET
        if not isinstance(self.gift_type, Unset):
            gift_type = self.gift_type.value

        applied_amount = self.applied_amount

        constituent_name: None | str | Unset
        if isinstance(self.constituent_name, Unset):
            constituent_name = UNSET
        else:
            constituent_name = self.constituent_name

        gift_date: str | Unset = UNSET
        if not isinstance(self.gift_date, Unset):
            gift_date = self.gift_date.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if transaction_gift_id is not UNSET:
            field_dict["transaction_gift_id"] = transaction_gift_id
        if gift_id is not UNSET:
            field_dict["gift_id"] = gift_id
        if gift_type is not UNSET:
            field_dict["gift_type"] = gift_type
        if applied_amount is not UNSET:
            field_dict["applied_amount"] = applied_amount
        if constituent_name is not UNSET:
            field_dict["constituent_name"] = constituent_name
        if gift_date is not UNSET:
            field_dict["gift_date"] = gift_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        transaction_gift_id = d.pop("transaction_gift_id", UNSET)

        gift_id = d.pop("gift_id", UNSET)

        _gift_type = d.pop("gift_type", UNSET)
        gift_type: LinkedGiftGiftType | Unset
        if isinstance(_gift_type, Unset):
            gift_type = UNSET
        else:
            gift_type = LinkedGiftGiftType(_gift_type)

        applied_amount = d.pop("applied_amount", UNSET)

        def _parse_constituent_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constituent_name = _parse_constituent_name(d.pop("constituent_name", UNSET))

        _gift_date = d.pop("gift_date", UNSET)
        gift_date: datetime.date | Unset
        if isinstance(_gift_date, Unset):
            gift_date = UNSET
        else:
            gift_date = isoparse(_gift_date).date()

        linked_gift = cls(
            transaction_gift_id=transaction_gift_id,
            gift_id=gift_id,
            gift_type=gift_type,
            applied_amount=applied_amount,
            constituent_name=constituent_name,
            gift_date=gift_date,
        )

        return linked_gift
