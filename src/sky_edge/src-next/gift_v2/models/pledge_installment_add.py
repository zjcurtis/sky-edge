from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PledgeInstallmentAdd")


@_attrs_define
class PledgeInstallmentAdd:
    """A single installment for a pledge.

    Attributes:
        adjustment_id (None | str | Unset): The ID of the pledge's most recent adjustment. If the pledge has not been
            adjusted, this is the ID of the pledge.
            If no value is provided, this will default to the ID of the pledge. Example: 12345.
        amount (float | Unset): The amount of the installment. Example: 25.
        year (int | None | Unset): The year field. Example: 2024.
        date (datetime.datetime | None | Unset): The date of the installment.
    """

    adjustment_id: None | str | Unset = UNSET
    amount: float | Unset = UNSET
    year: int | None | Unset = UNSET
    date: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        adjustment_id: None | str | Unset
        if isinstance(self.adjustment_id, Unset):
            adjustment_id = UNSET
        else:
            adjustment_id = self.adjustment_id

        amount = self.amount

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if adjustment_id is not UNSET:
            field_dict["adjustment_id"] = adjustment_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if year is not UNSET:
            field_dict["year"] = year
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_adjustment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        adjustment_id = _parse_adjustment_id(d.pop("adjustment_id", UNSET))

        amount = d.pop("amount", UNSET)

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

        pledge_installment_add = cls(
            adjustment_id=adjustment_id,
            amount=amount,
            year=year,
            date=date,
        )

        return pledge_installment_add
