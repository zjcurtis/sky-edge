from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.membership_history import MembershipHistory


T = TypeVar("T", bound="MembershipHistoryCollection")


@_attrs_define
class MembershipHistoryCollection:
    """Defines a collection of membership history.

    Attributes:
        offset (int): The offset value used for pagination or positioning within a collection.
        limit (int): The limit representing the maximum number of items to retrieve or display.
        transactions (list[MembershipHistory] | None | Unset): The membership history list.
        count (int | Unset): The total count of items.
    """

    offset: int
    limit: int
    transactions: list[MembershipHistory] | None | Unset = UNSET
    count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        transactions: list[dict[str, Any]] | None | Unset
        if isinstance(self.transactions, Unset):
            transactions = UNSET
        elif isinstance(self.transactions, list):
            transactions = []
            for transactions_type_0_item_data in self.transactions:
                transactions_type_0_item = transactions_type_0_item_data.to_dict()
                transactions.append(transactions_type_0_item)

        else:
            transactions = self.transactions

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "offset": offset,
                "limit": limit,
            }
        )
        if transactions is not UNSET:
            field_dict["transactions"] = transactions
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.membership_history import MembershipHistory

        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        def _parse_transactions(data: object) -> list[MembershipHistory] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                transactions_type_0 = []
                _transactions_type_0 = data
                for transactions_type_0_item_data in _transactions_type_0:
                    transactions_type_0_item = MembershipHistory.from_dict(
                        transactions_type_0_item_data
                    )

                    transactions_type_0.append(transactions_type_0_item)

                return transactions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MembershipHistory] | None | Unset, data)

        transactions = _parse_transactions(d.pop("transactions", UNSET))

        count = d.pop("count", UNSET)

        membership_history_collection = cls(
            offset=offset,
            limit=limit,
            transactions=transactions,
            count=count,
        )

        return membership_history_collection
