from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linked_gift import LinkedGift


T = TypeVar("T", bound="LinkedGiftsCollection")


@_attrs_define
class LinkedGiftsCollection:
    """Defines a collection of LinkedGift.

    Attributes:
        offset (int): The offset value used for pagination or positioning within a collection.
        limit (int): The limit representing the maximum number of items to retrieve or display.
        linked_gifts (list[LinkedGift] | None | Unset): List of linked gifts.
        count (int | Unset): The total count of items.
    """

    offset: int
    limit: int
    linked_gifts: list[LinkedGift] | None | Unset = UNSET
    count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        linked_gifts: list[dict[str, Any]] | None | Unset
        if isinstance(self.linked_gifts, Unset):
            linked_gifts = UNSET
        elif isinstance(self.linked_gifts, list):
            linked_gifts = []
            for linked_gifts_type_0_item_data in self.linked_gifts:
                linked_gifts_type_0_item = linked_gifts_type_0_item_data.to_dict()
                linked_gifts.append(linked_gifts_type_0_item)

        else:
            linked_gifts = self.linked_gifts

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "offset": offset,
                "limit": limit,
            }
        )
        if linked_gifts is not UNSET:
            field_dict["linked_gifts"] = linked_gifts
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linked_gift import LinkedGift

        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        def _parse_linked_gifts(data: object) -> list[LinkedGift] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                linked_gifts_type_0 = []
                _linked_gifts_type_0 = data
                for linked_gifts_type_0_item_data in _linked_gifts_type_0:
                    linked_gifts_type_0_item = LinkedGift.from_dict(
                        linked_gifts_type_0_item_data
                    )

                    linked_gifts_type_0.append(linked_gifts_type_0_item)

                return linked_gifts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LinkedGift] | None | Unset, data)

        linked_gifts = _parse_linked_gifts(d.pop("linked_gifts", UNSET))

        count = d.pop("count", UNSET)

        linked_gifts_collection = cls(
            offset=offset,
            limit=limit,
            linked_gifts=linked_gifts,
            count=count,
        )

        return linked_gifts_collection
