from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionGift")


@_attrs_define
class TransactionGift:
    """The gift associated to membership

    Attributes:
        transaction_gift_id (None | str | Unset): The immutable system record ID of the transaction gift link.
        gift_id (None | str | Unset): The immutable system record ID of the gift.
        applied_amount (float | Unset): The applied gift amount.
    """

    transaction_gift_id: None | str | Unset = UNSET
    gift_id: None | str | Unset = UNSET
    applied_amount: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        transaction_gift_id: None | str | Unset
        if isinstance(self.transaction_gift_id, Unset):
            transaction_gift_id = UNSET
        else:
            transaction_gift_id = self.transaction_gift_id

        gift_id: None | str | Unset
        if isinstance(self.gift_id, Unset):
            gift_id = UNSET
        else:
            gift_id = self.gift_id

        applied_amount = self.applied_amount

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if transaction_gift_id is not UNSET:
            field_dict["transaction_gift_id"] = transaction_gift_id
        if gift_id is not UNSET:
            field_dict["gift_id"] = gift_id
        if applied_amount is not UNSET:
            field_dict["applied_amount"] = applied_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_transaction_gift_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transaction_gift_id = _parse_transaction_gift_id(d.pop("transaction_gift_id", UNSET))

        def _parse_gift_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gift_id = _parse_gift_id(d.pop("gift_id", UNSET))

        applied_amount = d.pop("applied_amount", UNSET)

        transaction_gift = cls(
            transaction_gift_id=transaction_gift_id,
            gift_id=gift_id,
            applied_amount=applied_amount,
        )

        return transaction_gift
