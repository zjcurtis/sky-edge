from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.membership_sub_category import MembershipSubCategory


T = TypeVar("T", bound="MembershipSubCategoryCollection")


@_attrs_define
class MembershipSubCategoryCollection:
    """Defines a collection of membership subcategory.

    Attributes:
        offset (int): The offset value used for pagination or positioning within a collection.
        limit (int): The limit representing the maximum number of items to retrieve or display.
        sub_categories (list[MembershipSubCategory] | None | Unset): The list of membership subcategories.
        count (int | Unset): The total count of items.
    """

    offset: int
    limit: int
    sub_categories: list[MembershipSubCategory] | None | Unset = UNSET
    count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        sub_categories: list[dict[str, Any]] | None | Unset
        if isinstance(self.sub_categories, Unset):
            sub_categories = UNSET
        elif isinstance(self.sub_categories, list):
            sub_categories = []
            for sub_categories_type_0_item_data in self.sub_categories:
                sub_categories_type_0_item = sub_categories_type_0_item_data.to_dict()
                sub_categories.append(sub_categories_type_0_item)

        else:
            sub_categories = self.sub_categories

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "offset": offset,
                "limit": limit,
            }
        )
        if sub_categories is not UNSET:
            field_dict["sub_categories"] = sub_categories
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.membership_sub_category import MembershipSubCategory

        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        def _parse_sub_categories(data: object) -> list[MembershipSubCategory] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sub_categories_type_0 = []
                _sub_categories_type_0 = data
                for sub_categories_type_0_item_data in _sub_categories_type_0:
                    sub_categories_type_0_item = MembershipSubCategory.from_dict(sub_categories_type_0_item_data)

                    sub_categories_type_0.append(sub_categories_type_0_item)

                return sub_categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MembershipSubCategory] | None | Unset, data)

        sub_categories = _parse_sub_categories(d.pop("sub_categories", UNSET))

        count = d.pop("count", UNSET)

        membership_sub_category_collection = cls(
            offset=offset,
            limit=limit,
            sub_categories=sub_categories,
            count=count,
        )

        return membership_sub_category_collection
