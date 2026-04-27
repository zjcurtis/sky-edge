from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.membership_benefit import MembershipBenefit


T = TypeVar("T", bound="MembershipBenefitCollection")


@_attrs_define
class MembershipBenefitCollection:
    """Membership benefit collection to be returned

    Attributes:
        offset (int): The offset value used for pagination or positioning within a collection.
        limit (int): The limit representing the maximum number of items to retrieve or display.
        benefits (list[MembershipBenefit] | None | Unset): The collection of membership Benefits.
        total_value (float | Unset): The sum of all benefit values across the membership.
        send_benefits_to (None | str | Unset): Indicates who receives the benefits: PrimaryMember or Donor
        waive_benefits (bool | Unset): Indicates whether benefits are waived for this membership transaction
        count (int | Unset): The total count of items.
    """

    offset: int
    limit: int
    benefits: list[MembershipBenefit] | None | Unset = UNSET
    total_value: float | Unset = UNSET
    send_benefits_to: None | str | Unset = UNSET
    waive_benefits: bool | Unset = UNSET
    count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        benefits: list[dict[str, Any]] | None | Unset
        if isinstance(self.benefits, Unset):
            benefits = UNSET
        elif isinstance(self.benefits, list):
            benefits = []
            for benefits_type_0_item_data in self.benefits:
                benefits_type_0_item = benefits_type_0_item_data.to_dict()
                benefits.append(benefits_type_0_item)

        else:
            benefits = self.benefits

        total_value = self.total_value

        send_benefits_to: None | str | Unset
        if isinstance(self.send_benefits_to, Unset):
            send_benefits_to = UNSET
        else:
            send_benefits_to = self.send_benefits_to

        waive_benefits = self.waive_benefits

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "offset": offset,
                "limit": limit,
            }
        )
        if benefits is not UNSET:
            field_dict["benefits"] = benefits
        if total_value is not UNSET:
            field_dict["total_value"] = total_value
        if send_benefits_to is not UNSET:
            field_dict["send_benefits_to"] = send_benefits_to
        if waive_benefits is not UNSET:
            field_dict["waive_benefits"] = waive_benefits
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.membership_benefit import MembershipBenefit

        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        def _parse_benefits(data: object) -> list[MembershipBenefit] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                benefits_type_0 = []
                _benefits_type_0 = data
                for benefits_type_0_item_data in _benefits_type_0:
                    benefits_type_0_item = MembershipBenefit.from_dict(
                        benefits_type_0_item_data
                    )

                    benefits_type_0.append(benefits_type_0_item)

                return benefits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MembershipBenefit] | None | Unset, data)

        benefits = _parse_benefits(d.pop("benefits", UNSET))

        total_value = d.pop("total_value", UNSET)

        def _parse_send_benefits_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        send_benefits_to = _parse_send_benefits_to(d.pop("send_benefits_to", UNSET))

        waive_benefits = d.pop("waive_benefits", UNSET)

        count = d.pop("count", UNSET)

        membership_benefit_collection = cls(
            offset=offset,
            limit=limit,
            benefits=benefits,
            total_value=total_value,
            send_benefits_to=send_benefits_to,
            waive_benefits=waive_benefits,
            count=count,
        )

        return membership_benefit_collection
