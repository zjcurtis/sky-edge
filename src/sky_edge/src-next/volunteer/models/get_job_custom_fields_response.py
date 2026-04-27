from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_read import CustomFieldRead


T = TypeVar("T", bound="GetJobCustomFieldsResponse")


@_attrs_define
class GetJobCustomFieldsResponse:
    """Response model for job custom fields

    Attributes:
        custom_fields (list[CustomFieldRead] | None | Unset): List of custom fields for the job
    """

    custom_fields: list[CustomFieldRead] | None | Unset = UNSET

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_field_read import CustomFieldRead

        d = dict(src_dict)

        def _parse_custom_fields(data: object) -> list[CustomFieldRead] | None | Unset:
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
                    custom_fields_type_0_item = CustomFieldRead.from_dict(custom_fields_type_0_item_data)

                    custom_fields_type_0.append(custom_fields_type_0_item)

                return custom_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CustomFieldRead] | None | Unset, data)

        custom_fields = _parse_custom_fields(d.pop("custom_fields", UNSET))

        get_job_custom_fields_response = cls(
            custom_fields=custom_fields,
        )

        return get_job_custom_fields_response
