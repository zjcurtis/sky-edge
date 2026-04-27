from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.planned_gift_asset_response import PlannedGiftAssetResponse


T = TypeVar("T", bound="PlannedGiftAssetListResponse")


@_attrs_define
class PlannedGiftAssetListResponse:
    """Represents the paginated list response for planned gift assets.

    Attributes:
        count (int): The total number of assets.
        offset (int): The number of records that were skipped in the current request.
        limit (int): The maximum number of records that were requested.
        assets (list[PlannedGiftAssetResponse]): The list of planned gift assets.
    """

    count: int
    offset: int
    limit: int
    assets: list[PlannedGiftAssetResponse]

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        offset = self.offset

        limit = self.limit

        assets = []
        for assets_item_data in self.assets:
            assets_item = assets_item_data.to_dict()
            assets.append(assets_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "offset": offset,
                "limit": limit,
                "assets": assets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.planned_gift_asset_response import PlannedGiftAssetResponse

        d = dict(src_dict)
        count = d.pop("count")

        offset = d.pop("offset")

        limit = d.pop("limit")

        assets = []
        _assets = d.pop("assets")
        for assets_item_data in _assets:
            assets_item = PlannedGiftAssetResponse.from_dict(assets_item_data)

            assets.append(assets_item)

        planned_gift_asset_list_response = cls(
            count=count,
            offset=offset,
            limit=limit,
            assets=assets,
        )

        return planned_gift_asset_list_response
