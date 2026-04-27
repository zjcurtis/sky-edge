from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.membership_card import MembershipCard


T = TypeVar("T", bound="MembershipCardsCollection")


@_attrs_define
class MembershipCardsCollection:
    """Defines a collection of membership cards.

    Attributes:
        offset (int): The offset value used for pagination or positioning within a collection.
        limit (int): The limit representing the maximum number of items to retrieve or display.
        membership_cards (list[MembershipCard] | None | Unset): The membership card list.
        count (int | Unset): The total count of items.
    """

    offset: int
    limit: int
    membership_cards: list[MembershipCard] | None | Unset = UNSET
    count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        membership_cards: list[dict[str, Any]] | None | Unset
        if isinstance(self.membership_cards, Unset):
            membership_cards = UNSET
        elif isinstance(self.membership_cards, list):
            membership_cards = []
            for membership_cards_type_0_item_data in self.membership_cards:
                membership_cards_type_0_item = (
                    membership_cards_type_0_item_data.to_dict()
                )
                membership_cards.append(membership_cards_type_0_item)

        else:
            membership_cards = self.membership_cards

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "offset": offset,
                "limit": limit,
            }
        )
        if membership_cards is not UNSET:
            field_dict["membership_cards"] = membership_cards
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.membership_card import MembershipCard

        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        def _parse_membership_cards(
            data: object,
        ) -> list[MembershipCard] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                membership_cards_type_0 = []
                _membership_cards_type_0 = data
                for membership_cards_type_0_item_data in _membership_cards_type_0:
                    membership_cards_type_0_item = MembershipCard.from_dict(
                        membership_cards_type_0_item_data
                    )

                    membership_cards_type_0.append(membership_cards_type_0_item)

                return membership_cards_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MembershipCard] | None | Unset, data)

        membership_cards = _parse_membership_cards(d.pop("membership_cards", UNSET))

        count = d.pop("count", UNSET)

        membership_cards_collection = cls(
            offset=offset,
            limit=limit,
            membership_cards=membership_cards,
            count=count,
        )

        return membership_cards_collection
