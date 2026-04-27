from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.sold_stock_details_edit_gift_post_status import SoldStockDetailsEditGiftPostStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issuer_details_edit import IssuerDetailsEdit


T = TypeVar("T", bound="SoldStockDetailsEdit")


@_attrs_define
class SoldStockDetailsEdit:
    """Represents the details for selling a stock gift.

    Attributes:
        stock_sale_date (datetime.datetime): The date the stock was sold.
        stock_sale_value (float): The value of the stock sale.
        broker_fee (float | None | Unset): The sold stock broker fee.
        post_date (datetime.datetime | None | Unset): The GL post date of the sold stock.
        post_status (SoldStockDetailsEditGiftPostStatus | Unset): The GL post status of the sold stock.
        stock_issuer (IssuerDetailsEdit | Unset): Represents edits to the issuer details.
        notes (None | str | Unset): Comments on the sale of stock.
    """

    stock_sale_date: datetime.datetime
    stock_sale_value: float
    broker_fee: float | None | Unset = UNSET
    post_date: datetime.datetime | None | Unset = UNSET
    post_status: SoldStockDetailsEditGiftPostStatus | Unset = UNSET
    stock_issuer: IssuerDetailsEdit | Unset = UNSET
    notes: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        stock_sale_date = self.stock_sale_date.isoformat()

        stock_sale_value = self.stock_sale_value

        broker_fee: float | None | Unset
        if isinstance(self.broker_fee, Unset):
            broker_fee = UNSET
        else:
            broker_fee = self.broker_fee

        post_date: None | str | Unset
        if isinstance(self.post_date, Unset):
            post_date = UNSET
        elif isinstance(self.post_date, datetime.datetime):
            post_date = self.post_date.isoformat()
        else:
            post_date = self.post_date

        post_status: str | Unset = UNSET
        if not isinstance(self.post_status, Unset):
            post_status = self.post_status.value

        stock_issuer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stock_issuer, Unset):
            stock_issuer = self.stock_issuer.to_dict()

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "stock_sale_date": stock_sale_date,
                "stock_sale_value": stock_sale_value,
            }
        )
        if broker_fee is not UNSET:
            field_dict["broker_fee"] = broker_fee
        if post_date is not UNSET:
            field_dict["post_date"] = post_date
        if post_status is not UNSET:
            field_dict["post_status"] = post_status
        if stock_issuer is not UNSET:
            field_dict["stock_issuer"] = stock_issuer
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issuer_details_edit import IssuerDetailsEdit

        d = dict(src_dict)
        stock_sale_date = isoparse(d.pop("stock_sale_date"))

        stock_sale_value = d.pop("stock_sale_value")

        def _parse_broker_fee(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        broker_fee = _parse_broker_fee(d.pop("broker_fee", UNSET))

        def _parse_post_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                post_date_type_0 = isoparse(data)

                return post_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        post_date = _parse_post_date(d.pop("post_date", UNSET))

        _post_status = d.pop("post_status", UNSET)
        post_status: SoldStockDetailsEditGiftPostStatus | Unset
        if isinstance(_post_status, Unset):
            post_status = UNSET
        else:
            post_status = SoldStockDetailsEditGiftPostStatus(_post_status)

        _stock_issuer = d.pop("stock_issuer", UNSET)
        stock_issuer: IssuerDetailsEdit | Unset
        if isinstance(_stock_issuer, Unset):
            stock_issuer = UNSET
        else:
            stock_issuer = IssuerDetailsEdit.from_dict(_stock_issuer)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        sold_stock_details_edit = cls(
            stock_sale_date=stock_sale_date,
            stock_sale_value=stock_sale_value,
            broker_fee=broker_fee,
            post_date=post_date,
            post_status=post_status,
            stock_issuer=stock_issuer,
            notes=notes,
        )

        return sold_stock_details_edit
