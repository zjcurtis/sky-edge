from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_category_read import CustomFieldCategoryRead


T = TypeVar("T", bound="GetJobCustomFieldCategoryDetailsResponse")


@_attrs_define
class GetJobCustomFieldCategoryDetailsResponse:
    """Represents a collection of custom field category details

    Attributes:
        details (list[CustomFieldCategoryRead] | None | Unset): The collection of custom field category details
    """

    details: list[CustomFieldCategoryRead] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        details: list[dict[str, Any]] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, list):
            details = []
            for details_type_0_item_data in self.details:
                details_type_0_item = details_type_0_item_data.to_dict()
                details.append(details_type_0_item)

        else:
            details = self.details

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_field_category_read import CustomFieldCategoryRead

        d = dict(src_dict)

        def _parse_details(
            data: object,
        ) -> list[CustomFieldCategoryRead] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                details_type_0 = []
                _details_type_0 = data
                for details_type_0_item_data in _details_type_0:
                    details_type_0_item = CustomFieldCategoryRead.from_dict(
                        details_type_0_item_data
                    )

                    details_type_0.append(details_type_0_item)

                return details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CustomFieldCategoryRead] | None | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        get_job_custom_field_category_details_response = cls(
            details=details,
        )

        return get_job_custom_field_category_details_response
