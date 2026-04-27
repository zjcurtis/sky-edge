from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="MembershipJunctionIdsCollection")


@_attrs_define
class MembershipJunctionIdsCollection:
    """Collection of IDs.

    Attributes:
        offset (int): The offset value used for pagination or positioning within a collection.
        limit (int): The limit representing the maximum number of items to retrieve or display.
        membership_junction_ids (list[str] | None | Unset): The collection of membership junction IDs.
        count (int | Unset): The total count of items.
    """

    offset: int
    limit: int
    membership_junction_ids: list[str] | None | Unset = UNSET
    count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        membership_junction_ids: list[str] | None | Unset
        if isinstance(self.membership_junction_ids, Unset):
            membership_junction_ids = UNSET
        elif isinstance(self.membership_junction_ids, list):
            membership_junction_ids = self.membership_junction_ids

        else:
            membership_junction_ids = self.membership_junction_ids

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "offset": offset,
                "limit": limit,
            }
        )
        if membership_junction_ids is not UNSET:
            field_dict["membership_junction_ids"] = membership_junction_ids
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        def _parse_membership_junction_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                membership_junction_ids_type_0 = cast(list[str], data)

                return membership_junction_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        membership_junction_ids = _parse_membership_junction_ids(
            d.pop("membership_junction_ids", UNSET)
        )

        count = d.pop("count", UNSET)

        membership_junction_ids_collection = cls(
            offset=offset,
            limit=limit,
            membership_junction_ids=membership_junction_ids,
            count=count,
        )

        return membership_junction_ids_collection
