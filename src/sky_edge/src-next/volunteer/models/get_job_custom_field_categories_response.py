from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetJobCustomFieldCategoriesResponse")


@_attrs_define
class GetJobCustomFieldCategoriesResponse:
    """Represents a collection of custom field category names

    Attributes:
        categories (list[str] | None | Unset): The collection of custom field category names
    """

    categories: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        categories: list[str] | None | Unset
        if isinstance(self.categories, Unset):
            categories = UNSET
        elif isinstance(self.categories, list):
            categories = self.categories

        else:
            categories = self.categories

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_categories(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                categories_type_0 = cast(list[str], data)

                return categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        categories = _parse_categories(d.pop("categories", UNSET))

        get_job_custom_field_categories_response = cls(
            categories=categories,
        )

        return get_job_custom_field_categories_response
