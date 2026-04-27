from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="PledgeInstallmentRead")


@_attrs_define
class PledgeInstallmentRead:
    """A single installment for a pledge.

    Attributes:
        id (None | str | Unset): The ID of the installment.
        amount (Currency | Unset): An amount denominated in a specific currency.
        year (int | None | Unset): The year field.
        date (datetime.datetime | None | Unset): The date of the installment.
        sequence (int | None | Unset): The sequence is used to determine the display order of pledge installments.
        balance (float | None | Unset): The balance of the installment.
        remaining_pledge_balance (float | None | Unset): The remaining pledge balance.
        can_apply_payment (bool | None | Unset): Flag indicating a pledge payment can be applied to the installment.
    """

    id: None | str | Unset = UNSET
    amount: Currency | Unset = UNSET
    year: int | None | Unset = UNSET
    date: datetime.datetime | None | Unset = UNSET
    sequence: int | None | Unset = UNSET
    balance: float | None | Unset = UNSET
    remaining_pledge_balance: float | None | Unset = UNSET
    can_apply_payment: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        year: int | None | Unset
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.datetime):
            date = self.date.isoformat()
        else:
            date = self.date

        sequence: int | None | Unset
        if isinstance(self.sequence, Unset):
            sequence = UNSET
        else:
            sequence = self.sequence

        balance: float | None | Unset
        if isinstance(self.balance, Unset):
            balance = UNSET
        else:
            balance = self.balance

        remaining_pledge_balance: float | None | Unset
        if isinstance(self.remaining_pledge_balance, Unset):
            remaining_pledge_balance = UNSET
        else:
            remaining_pledge_balance = self.remaining_pledge_balance

        can_apply_payment: bool | None | Unset
        if isinstance(self.can_apply_payment, Unset):
            can_apply_payment = UNSET
        else:
            can_apply_payment = self.can_apply_payment

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if year is not UNSET:
            field_dict["year"] = year
        if date is not UNSET:
            field_dict["date"] = date
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if balance is not UNSET:
            field_dict["balance"] = balance
        if remaining_pledge_balance is not UNSET:
            field_dict["remaining_pledge_balance"] = remaining_pledge_balance
        if can_apply_payment is not UNSET:
            field_dict["can_apply_payment"] = can_apply_payment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        _amount = d.pop("amount", UNSET)
        amount: Currency | Unset
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = Currency.from_dict(_amount)

        def _parse_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        year = _parse_year(d.pop("year", UNSET))

        def _parse_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data)

                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_sequence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequence = _parse_sequence(d.pop("sequence", UNSET))

        def _parse_balance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        balance = _parse_balance(d.pop("balance", UNSET))

        def _parse_remaining_pledge_balance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        remaining_pledge_balance = _parse_remaining_pledge_balance(d.pop("remaining_pledge_balance", UNSET))

        def _parse_can_apply_payment(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_apply_payment = _parse_can_apply_payment(d.pop("can_apply_payment", UNSET))

        pledge_installment_read = cls(
            id=id,
            amount=amount,
            year=year,
            date=date,
            sequence=sequence,
            balance=balance,
            remaining_pledge_balance=remaining_pledge_balance,
            can_apply_payment=can_apply_payment,
        )

        return pledge_installment_read
