from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.membership_fundraiser import MembershipFundraiser


T = TypeVar("T", bound="MembershipFundraiserCollection")


@_attrs_define
class MembershipFundraiserCollection:
    """Defines a collection of membership fundraiser.

    Attributes:
        offset (int): The offset value used for pagination or positioning within a collection.
        limit (int): The limit representing the maximum number of items to retrieve or display.
        fundraisers (list[MembershipFundraiser] | None | Unset): The collection of membership fundraiser.
        count (int | Unset): The total count of items.
    """

    offset: int
    limit: int
    fundraisers: list[MembershipFundraiser] | None | Unset = UNSET
    count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        fundraisers: list[dict[str, Any]] | None | Unset
        if isinstance(self.fundraisers, Unset):
            fundraisers = UNSET
        elif isinstance(self.fundraisers, list):
            fundraisers = []
            for fundraisers_type_0_item_data in self.fundraisers:
                fundraisers_type_0_item = fundraisers_type_0_item_data.to_dict()
                fundraisers.append(fundraisers_type_0_item)

        else:
            fundraisers = self.fundraisers

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "offset": offset,
                "limit": limit,
            }
        )
        if fundraisers is not UNSET:
            field_dict["fundraisers"] = fundraisers
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.membership_fundraiser import MembershipFundraiser

        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        def _parse_fundraisers(data: object) -> list[MembershipFundraiser] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fundraisers_type_0 = []
                _fundraisers_type_0 = data
                for fundraisers_type_0_item_data in _fundraisers_type_0:
                    fundraisers_type_0_item = MembershipFundraiser.from_dict(fundraisers_type_0_item_data)

                    fundraisers_type_0.append(fundraisers_type_0_item)

                return fundraisers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MembershipFundraiser] | None | Unset, data)

        fundraisers = _parse_fundraisers(d.pop("fundraisers", UNSET))

        count = d.pop("count", UNSET)

        membership_fundraiser_collection = cls(
            offset=offset,
            limit=limit,
            fundraisers=fundraisers,
            count=count,
        )

        return membership_fundraiser_collection
