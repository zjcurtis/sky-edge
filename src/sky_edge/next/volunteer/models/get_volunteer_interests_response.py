from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.volunteer_interest import VolunteerInterest


T = TypeVar("T", bound="GetVolunteerInterestsResponse")


@_attrs_define
class GetVolunteerInterestsResponse:
    """Response model for getting volunteer interests

    Attributes:
        total_count (int | Unset): Gets or sets the total count of volunteer interests
        interests (list[VolunteerInterest] | None | Unset): Gets or sets the collection of volunteer interests
    """

    total_count: int | Unset = UNSET
    interests: list[VolunteerInterest] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        interests: list[dict[str, Any]] | None | Unset
        if isinstance(self.interests, Unset):
            interests = UNSET
        elif isinstance(self.interests, list):
            interests = []
            for interests_type_0_item_data in self.interests:
                interests_type_0_item = interests_type_0_item_data.to_dict()
                interests.append(interests_type_0_item)

        else:
            interests = self.interests

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if interests is not UNSET:
            field_dict["interests"] = interests

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.volunteer_interest import VolunteerInterest

        d = dict(src_dict)
        total_count = d.pop("total_count", UNSET)

        def _parse_interests(data: object) -> list[VolunteerInterest] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                interests_type_0 = []
                _interests_type_0 = data
                for interests_type_0_item_data in _interests_type_0:
                    interests_type_0_item = VolunteerInterest.from_dict(
                        interests_type_0_item_data
                    )

                    interests_type_0.append(interests_type_0_item)

                return interests_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VolunteerInterest] | None | Unset, data)

        interests = _parse_interests(d.pop("interests", UNSET))

        get_volunteer_interests_response = cls(
            total_count=total_count,
            interests=interests,
        )

        return get_volunteer_interests_response
