from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_category_details import CustomFieldCategoryDetails


T = TypeVar("T", bound="CustomFieldCategoryDetailsCollection")


@_attrs_define
class CustomFieldCategoryDetailsCollection:
    """Defines a collection of Custom Fields.

    Attributes:
        custom_field_types (list[CustomFieldCategoryDetails] | None | Unset): List of custom fields.
        count (int | Unset): The total count of items.
    """

    custom_field_types: list[CustomFieldCategoryDetails] | None | Unset = UNSET
    count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        custom_field_types: list[dict[str, Any]] | None | Unset
        if isinstance(self.custom_field_types, Unset):
            custom_field_types = UNSET
        elif isinstance(self.custom_field_types, list):
            custom_field_types = []
            for custom_field_types_type_0_item_data in self.custom_field_types:
                custom_field_types_type_0_item = custom_field_types_type_0_item_data.to_dict()
                custom_field_types.append(custom_field_types_type_0_item)

        else:
            custom_field_types = self.custom_field_types

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if custom_field_types is not UNSET:
            field_dict["custom_field_types"] = custom_field_types
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_field_category_details import CustomFieldCategoryDetails

        d = dict(src_dict)

        def _parse_custom_field_types(data: object) -> list[CustomFieldCategoryDetails] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_field_types_type_0 = []
                _custom_field_types_type_0 = data
                for custom_field_types_type_0_item_data in _custom_field_types_type_0:
                    custom_field_types_type_0_item = CustomFieldCategoryDetails.from_dict(
                        custom_field_types_type_0_item_data
                    )

                    custom_field_types_type_0.append(custom_field_types_type_0_item)

                return custom_field_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CustomFieldCategoryDetails] | None | Unset, data)

        custom_field_types = _parse_custom_field_types(d.pop("custom_field_types", UNSET))

        count = d.pop("count", UNSET)

        custom_field_category_details_collection = cls(
            custom_field_types=custom_field_types,
            count=count,
        )

        return custom_field_category_details_collection
