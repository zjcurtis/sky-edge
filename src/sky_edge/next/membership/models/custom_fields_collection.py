from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field import CustomField


T = TypeVar("T", bound="CustomFieldsCollection")


@_attrs_define
class CustomFieldsCollection:
    """Defines a collection of Custom Fields.

    Attributes:
        custom_fields (list[CustomField] | None | Unset): List of custom fields.
        count (int | Unset): The total count of items.
    """

    custom_fields: list[CustomField] | None | Unset = UNSET
    count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        custom_fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.custom_fields, Unset):
            custom_fields = UNSET
        elif isinstance(self.custom_fields, list):
            custom_fields = []
            for custom_fields_type_0_item_data in self.custom_fields:
                custom_fields_type_0_item = custom_fields_type_0_item_data.to_dict()
                custom_fields.append(custom_fields_type_0_item)

        else:
            custom_fields = self.custom_fields

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_field import CustomField

        d = dict(src_dict)

        def _parse_custom_fields(data: object) -> list[CustomField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_fields_type_0 = []
                _custom_fields_type_0 = data
                for custom_fields_type_0_item_data in _custom_fields_type_0:
                    custom_fields_type_0_item = CustomField.from_dict(
                        custom_fields_type_0_item_data
                    )

                    custom_fields_type_0.append(custom_fields_type_0_item)

                return custom_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CustomField] | None | Unset, data)

        custom_fields = _parse_custom_fields(d.pop("custom_fields", UNSET))

        count = d.pop("count", UNSET)

        custom_fields_collection = cls(
            custom_fields=custom_fields,
            count=count,
        )

        return custom_fields_collection
