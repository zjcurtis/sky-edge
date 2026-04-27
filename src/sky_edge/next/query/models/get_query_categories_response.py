from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_category import QueryCategory


T = TypeVar("T", bound="GetQueryCategoriesResponse")


@_attrs_define
class GetQueryCategoriesResponse:
    """Response model for GetQueryCategories

    Attributes:
        categories (list[QueryCategory] | None | Unset): The query categories
    """

    categories: list[QueryCategory] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        categories: list[dict[str, Any]] | None | Unset
        if isinstance(self.categories, Unset):
            categories = UNSET
        elif isinstance(self.categories, list):
            categories = []
            for categories_type_0_item_data in self.categories:
                categories_type_0_item = categories_type_0_item_data.to_dict()
                categories.append(categories_type_0_item)

        else:
            categories = self.categories

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_category import QueryCategory

        d = dict(src_dict)

        def _parse_categories(data: object) -> list[QueryCategory] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                categories_type_0 = []
                _categories_type_0 = data
                for categories_type_0_item_data in _categories_type_0:
                    categories_type_0_item = QueryCategory.from_dict(
                        categories_type_0_item_data
                    )

                    categories_type_0.append(categories_type_0_item)

                return categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[QueryCategory] | None | Unset, data)

        categories = _parse_categories(d.pop("categories", UNSET))

        get_query_categories_response = cls(
            categories=categories,
        )

        return get_query_categories_response
