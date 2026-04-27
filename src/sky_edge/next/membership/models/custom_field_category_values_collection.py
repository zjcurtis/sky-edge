from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldCategoryValuesCollection")


@_attrs_define
class CustomFieldCategoryValuesCollection:
    """Defines a collection of Custom Fields.

    Attributes:
        custom_field_category_values (list[str] | None | Unset): List of custom fields.
        count (int | Unset): The total count of items.
    """

    custom_field_category_values: list[str] | None | Unset = UNSET
    count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        custom_field_category_values: list[str] | None | Unset
        if isinstance(self.custom_field_category_values, Unset):
            custom_field_category_values = UNSET
        elif isinstance(self.custom_field_category_values, list):
            custom_field_category_values = self.custom_field_category_values

        else:
            custom_field_category_values = self.custom_field_category_values

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if custom_field_category_values is not UNSET:
            field_dict["custom_field_category_values"] = custom_field_category_values
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_custom_field_category_values(
            data: object,
        ) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_field_category_values_type_0 = cast(list[str], data)

                return custom_field_category_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        custom_field_category_values = _parse_custom_field_category_values(
            d.pop("custom_field_category_values", UNSET)
        )

        count = d.pop("count", UNSET)

        custom_field_category_values_collection = cls(
            custom_field_category_values=custom_field_category_values,
            count=count,
        )

        return custom_field_category_values_collection
