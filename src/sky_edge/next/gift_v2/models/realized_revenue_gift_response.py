from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="RealizedRevenueGiftResponse")


@_attrs_define
class RealizedRevenueGiftResponse:
    """Represents a single realized revenue gift in the API response.

    Attributes:
        gift_id (None | str): The unique identifier of the gift.
        amount (Currency): An amount denominated in a specific currency.
        date (datetime.datetime): The date of the gift.
        gift_type (None | str): The gift type code.
        constituent_id (None | str): The constituent identifier associated with the gift.
        reference (None | str | Unset): The gift reference.
        constituent_name (None | str | Unset): The display name of the constituent.
    """

    gift_id: None | str
    amount: Currency
    date: datetime.datetime
    gift_type: None | str
    constituent_id: None | str
    reference: None | str | Unset = UNSET
    constituent_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        gift_id: None | str
        gift_id = self.gift_id

        amount = self.amount.to_dict()

        date = self.date.isoformat()

        gift_type: None | str
        gift_type = self.gift_type

        constituent_id: None | str
        constituent_id = self.constituent_id

        reference: None | str | Unset
        if isinstance(self.reference, Unset):
            reference = UNSET
        else:
            reference = self.reference

        constituent_name: None | str | Unset
        if isinstance(self.constituent_name, Unset):
            constituent_name = UNSET
        else:
            constituent_name = self.constituent_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "gift_id": gift_id,
                "amount": amount,
                "date": date,
                "gift_type": gift_type,
                "constituent_id": constituent_id,
            }
        )
        if reference is not UNSET:
            field_dict["reference"] = reference
        if constituent_name is not UNSET:
            field_dict["constituent_name"] = constituent_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency

        d = dict(src_dict)

        def _parse_gift_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        gift_id = _parse_gift_id(d.pop("gift_id"))

        amount = Currency.from_dict(d.pop("amount"))

        date = isoparse(d.pop("date"))

        def _parse_gift_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        gift_type = _parse_gift_type(d.pop("gift_type"))

        def _parse_constituent_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        constituent_id = _parse_constituent_id(d.pop("constituent_id"))

        def _parse_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference = _parse_reference(d.pop("reference", UNSET))

        def _parse_constituent_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constituent_name = _parse_constituent_name(d.pop("constituent_name", UNSET))

        realized_revenue_gift_response = cls(
            gift_id=gift_id,
            amount=amount,
            date=date,
            gift_type=gift_type,
            constituent_id=constituent_id,
            reference=reference,
            constituent_name=constituent_name,
        )

        return realized_revenue_gift_response
