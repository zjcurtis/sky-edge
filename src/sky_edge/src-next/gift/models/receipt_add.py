from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="ReceiptAdd")


@_attrs_define
class ReceiptAdd:
    """An object that represents the gift receipt to create.
    To help donors track their giving for tax purposes, your organization should provide gift receipts.

        Attributes:
            amount (Currency | Unset): For consistency, currency is configured at the organization level. This ensures that
                all monetary amounts are consistent, regardless of where they are entered or viewed.
            date (datetime.datetime | Unset): The date that the gift was receipted. Includes an offset from UTC in <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
            status (str | Unset): The receipt status of the gift. Available values are <i>RECEIPTED</i>,
                <i>NEEDSRECEIPT</i>, and <i>DONOTRECEIPT.</i>
                When <code>receipt_status</code> is set to <i>DONOTRECEIPT</i> or <i>NEEDSRECEIPT</i>, <code>receipt_date</code>
                should be null.
                When it is set to <i>RECEIPTED</i>, <code>receipt_date</code> is required and is no longer editable.
                If no value is provided, a default value of <i>NEEDSRECEIPT</i> will be used.
            receipt_stack (str | Unset): The receipt stack associated with the gift. Only available for customers using
                receipt stacks.
    """

    amount: Currency | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    status: str | Unset = UNSET
    receipt_stack: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        status = self.status

        receipt_stack = self.receipt_stack

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if date is not UNSET:
            field_dict["date"] = date
        if status is not UNSET:
            field_dict["status"] = status
        if receipt_stack is not UNSET:
            field_dict["receipt_stack"] = receipt_stack

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency

        d = dict(src_dict)
        _amount = d.pop("amount", UNSET)
        amount: Currency | Unset
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = Currency.from_dict(_amount)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        status = d.pop("status", UNSET)

        receipt_stack = d.pop("receipt_stack", UNSET)

        receipt_add = cls(
            amount=amount,
            date=date,
            status=status,
            receipt_stack=receipt_stack,
        )

        receipt_add.additional_properties = d
        return receipt_add

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
