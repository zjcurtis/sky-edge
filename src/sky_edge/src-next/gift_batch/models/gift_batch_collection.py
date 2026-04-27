from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gift_batch import GiftBatch


T = TypeVar("T", bound="GiftBatchCollection")


@_attrs_define
class GiftBatchCollection:
    """Represents a collection of gift batches

    Attributes:
        limit (int): Limit used for the request.
        offset (int): Offset used for the request.
        count (int | Unset): The number of batch records included in the response.
        giftbatches (list[GiftBatch] | None | Unset): The set of gift batches included in the response.
    """

    limit: int
    offset: int
    count: int | Unset = UNSET
    giftbatches: list[GiftBatch] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        offset = self.offset

        count = self.count

        giftbatches: list[dict[str, Any]] | None | Unset
        if isinstance(self.giftbatches, Unset):
            giftbatches = UNSET
        elif isinstance(self.giftbatches, list):
            giftbatches = []
            for giftbatches_type_0_item_data in self.giftbatches:
                giftbatches_type_0_item = giftbatches_type_0_item_data.to_dict()
                giftbatches.append(giftbatches_type_0_item)

        else:
            giftbatches = self.giftbatches

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "limit": limit,
                "offset": offset,
            }
        )
        if count is not UNSET:
            field_dict["count"] = count
        if giftbatches is not UNSET:
            field_dict["giftbatches"] = giftbatches

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gift_batch import GiftBatch

        d = dict(src_dict)
        limit = d.pop("limit")

        offset = d.pop("offset")

        count = d.pop("count", UNSET)

        def _parse_giftbatches(data: object) -> list[GiftBatch] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                giftbatches_type_0 = []
                _giftbatches_type_0 = data
                for giftbatches_type_0_item_data in _giftbatches_type_0:
                    giftbatches_type_0_item = GiftBatch.from_dict(giftbatches_type_0_item_data)

                    giftbatches_type_0.append(giftbatches_type_0_item)

                return giftbatches_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GiftBatch] | None | Unset, data)

        giftbatches = _parse_giftbatches(d.pop("giftbatches", UNSET))

        gift_batch_collection = cls(
            limit=limit,
            offset=offset,
            count=count,
            giftbatches=giftbatches,
        )

        return gift_batch_collection
