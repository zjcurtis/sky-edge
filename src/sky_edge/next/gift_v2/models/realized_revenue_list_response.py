from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.currency import Currency
    from ..models.realized_revenue_gift_response import RealizedRevenueGiftResponse


T = TypeVar("T", bound="RealizedRevenueListResponse")


@_attrs_define
class RealizedRevenueListResponse:
    """Represents the paginated list response for realized revenue gifts.

    Attributes:
        count (int): The total number of realized revenue gifts.
        total_realized_amount (Currency): An amount denominated in a specific currency.
        offset (int): The number of records that were skipped in the current request.
        limit (int): The maximum number of records that were requested.
        realized_revenue_gifts (list[RealizedRevenueGiftResponse]): The list of realized revenue gifts.
    """

    count: int
    total_realized_amount: Currency
    offset: int
    limit: int
    realized_revenue_gifts: list[RealizedRevenueGiftResponse]

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        total_realized_amount = self.total_realized_amount.to_dict()

        offset = self.offset

        limit = self.limit

        realized_revenue_gifts = []
        for realized_revenue_gifts_item_data in self.realized_revenue_gifts:
            realized_revenue_gifts_item = realized_revenue_gifts_item_data.to_dict()
            realized_revenue_gifts.append(realized_revenue_gifts_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "total_realized_amount": total_realized_amount,
                "offset": offset,
                "limit": limit,
                "realized_revenue_gifts": realized_revenue_gifts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency
        from ..models.realized_revenue_gift_response import RealizedRevenueGiftResponse

        d = dict(src_dict)
        count = d.pop("count")

        total_realized_amount = Currency.from_dict(d.pop("total_realized_amount"))

        offset = d.pop("offset")

        limit = d.pop("limit")

        realized_revenue_gifts = []
        _realized_revenue_gifts = d.pop("realized_revenue_gifts")
        for realized_revenue_gifts_item_data in _realized_revenue_gifts:
            realized_revenue_gifts_item = RealizedRevenueGiftResponse.from_dict(
                realized_revenue_gifts_item_data
            )

            realized_revenue_gifts.append(realized_revenue_gifts_item)

        realized_revenue_list_response = cls(
            count=count,
            total_realized_amount=total_realized_amount,
            offset=offset,
            limit=limit,
            realized_revenue_gifts=realized_revenue_gifts,
        )

        return realized_revenue_list_response
