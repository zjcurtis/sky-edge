from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.membership_category import MembershipCategory


T = TypeVar("T", bound="Membership")


@_attrs_define
class Membership:
    """Membership information for the participant.

    Attributes:
        category (MembershipCategory | Unset): The individual's membership category.
    """

    category: MembershipCategory | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.membership_category import MembershipCategory

        d = dict(src_dict)
        _category = d.pop("category", UNSET)
        category: MembershipCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = MembershipCategory.from_dict(_category)

        membership = cls(
            category=category,
        )

        return membership
