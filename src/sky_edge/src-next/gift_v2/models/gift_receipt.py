from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.gift_receipt_receipt_status import GiftReceiptReceiptStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_table_entry import CodeTableEntry
    from ..models.currency import Currency


T = TypeVar("T", bound="GiftReceipt")


@_attrs_define
class GiftReceipt:
    """Receipt information for a gift.

    Attributes:
        gift_legacy_id (None | str | Unset): The legacy ID of the receipt's associated gift. Example: 12345.
        receipt_amount (Currency | Unset): An amount denominated in a specific currency.
        receipt_status (GiftReceiptReceiptStatus | Unset): The receipt status. Example: Receipted.
        receipt_date (datetime.datetime | None | Unset): The receipt date. Deprecated. Please use the date property
            instead.
        date (datetime.date | None | Unset): The receipt date.
        receipt_number (int | None | Unset): The receipt number. Example: 5555.
        sequence (int | None | Unset): The receipt's sequence. Example: 1.
        receipt_stack (CodeTableEntry | Unset): A predefined entry in a code table.
    """

    gift_legacy_id: None | str | Unset = UNSET
    receipt_amount: Currency | Unset = UNSET
    receipt_status: GiftReceiptReceiptStatus | Unset = UNSET
    receipt_date: datetime.datetime | None | Unset = UNSET
    date: datetime.date | None | Unset = UNSET
    receipt_number: int | None | Unset = UNSET
    sequence: int | None | Unset = UNSET
    receipt_stack: CodeTableEntry | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        gift_legacy_id: None | str | Unset
        if isinstance(self.gift_legacy_id, Unset):
            gift_legacy_id = UNSET
        else:
            gift_legacy_id = self.gift_legacy_id

        receipt_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.receipt_amount, Unset):
            receipt_amount = self.receipt_amount.to_dict()

        receipt_status: str | Unset = UNSET
        if not isinstance(self.receipt_status, Unset):
            receipt_status = self.receipt_status.value

        receipt_date: None | str | Unset
        if isinstance(self.receipt_date, Unset):
            receipt_date = UNSET
        elif isinstance(self.receipt_date, datetime.datetime):
            receipt_date = self.receipt_date.isoformat()
        else:
            receipt_date = self.receipt_date

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.date):
            date = self.date.isoformat()
        else:
            date = self.date

        receipt_number: int | None | Unset
        if isinstance(self.receipt_number, Unset):
            receipt_number = UNSET
        else:
            receipt_number = self.receipt_number

        sequence: int | None | Unset
        if isinstance(self.sequence, Unset):
            sequence = UNSET
        else:
            sequence = self.sequence

        receipt_stack: dict[str, Any] | Unset = UNSET
        if not isinstance(self.receipt_stack, Unset):
            receipt_stack = self.receipt_stack.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if gift_legacy_id is not UNSET:
            field_dict["gift_legacy_id"] = gift_legacy_id
        if receipt_amount is not UNSET:
            field_dict["receipt_amount"] = receipt_amount
        if receipt_status is not UNSET:
            field_dict["receipt_status"] = receipt_status
        if receipt_date is not UNSET:
            field_dict["receipt_date"] = receipt_date
        if date is not UNSET:
            field_dict["date"] = date
        if receipt_number is not UNSET:
            field_dict["receipt_number"] = receipt_number
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if receipt_stack is not UNSET:
            field_dict["receipt_stack"] = receipt_stack

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.code_table_entry import CodeTableEntry
        from ..models.currency import Currency

        d = dict(src_dict)

        def _parse_gift_legacy_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gift_legacy_id = _parse_gift_legacy_id(d.pop("gift_legacy_id", UNSET))

        _receipt_amount = d.pop("receipt_amount", UNSET)
        receipt_amount: Currency | Unset
        if isinstance(_receipt_amount, Unset):
            receipt_amount = UNSET
        else:
            receipt_amount = Currency.from_dict(_receipt_amount)

        _receipt_status = d.pop("receipt_status", UNSET)
        receipt_status: GiftReceiptReceiptStatus | Unset
        if isinstance(_receipt_status, Unset):
            receipt_status = UNSET
        else:
            receipt_status = GiftReceiptReceiptStatus(_receipt_status)

        def _parse_receipt_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                receipt_date_type_0 = isoparse(data)

                return receipt_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        receipt_date = _parse_receipt_date(d.pop("receipt_date", UNSET))

        def _parse_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data).date()

                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_receipt_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        receipt_number = _parse_receipt_number(d.pop("receipt_number", UNSET))

        def _parse_sequence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequence = _parse_sequence(d.pop("sequence", UNSET))

        _receipt_stack = d.pop("receipt_stack", UNSET)
        receipt_stack: CodeTableEntry | Unset
        if isinstance(_receipt_stack, Unset):
            receipt_stack = UNSET
        else:
            receipt_stack = CodeTableEntry.from_dict(_receipt_stack)

        gift_receipt = cls(
            gift_legacy_id=gift_legacy_id,
            receipt_amount=receipt_amount,
            receipt_status=receipt_status,
            receipt_date=receipt_date,
            date=date,
            receipt_number=receipt_number,
            sequence=sequence,
            receipt_stack=receipt_stack,
        )

        return gift_receipt
