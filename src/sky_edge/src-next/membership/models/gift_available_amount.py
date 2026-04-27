from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GiftAvailableAmount")


@_attrs_define
class GiftAvailableAmount:
    """Gift available amount

    Attributes:
        gift_amount (float | Unset): Gift amount
        available_amount (float | Unset): Gift available amount
        currency_symbol (None | str | Unset): Non Nullable field currency symbol
    """

    gift_amount: float | Unset = UNSET
    available_amount: float | Unset = UNSET
    currency_symbol: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        gift_amount = self.gift_amount

        available_amount = self.available_amount

        currency_symbol: None | str | Unset
        if isinstance(self.currency_symbol, Unset):
            currency_symbol = UNSET
        else:
            currency_symbol = self.currency_symbol

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if gift_amount is not UNSET:
            field_dict["gift_amount"] = gift_amount
        if available_amount is not UNSET:
            field_dict["available_amount"] = available_amount
        if currency_symbol is not UNSET:
            field_dict["currency_symbol"] = currency_symbol

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gift_amount = d.pop("gift_amount", UNSET)

        available_amount = d.pop("available_amount", UNSET)

        def _parse_currency_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_symbol = _parse_currency_symbol(d.pop("currency_symbol", UNSET))

        gift_available_amount = cls(
            gift_amount=gift_amount,
            available_amount=available_amount,
            currency_symbol=currency_symbol,
        )

        return gift_available_amount
