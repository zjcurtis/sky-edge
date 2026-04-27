from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="MembershipCustomFieldsCreated")


@_attrs_define
class MembershipCustomFieldsCreated:
    """Membership custom fields response model

    Attributes:
        custom_field_ids (list[str] | None | Unset): The custom field ID property.
    """

    custom_field_ids: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        custom_field_ids: list[str] | None | Unset
        if isinstance(self.custom_field_ids, Unset):
            custom_field_ids = UNSET
        elif isinstance(self.custom_field_ids, list):
            custom_field_ids = self.custom_field_ids

        else:
            custom_field_ids = self.custom_field_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if custom_field_ids is not UNSET:
            field_dict["custom_field_ids"] = custom_field_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_custom_field_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_field_ids_type_0 = cast(list[str], data)

                return custom_field_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        custom_field_ids = _parse_custom_field_ids(d.pop("custom_field_ids", UNSET))

        membership_custom_fields_created = cls(
            custom_field_ids=custom_field_ids,
        )

        return membership_custom_fields_created
