from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.volunteer_type import VolunteerType


T = TypeVar("T", bound="GetVolunteerTypesResponse")


@_attrs_define
class GetVolunteerTypesResponse:
    """Response model for getting volunteer types

    Attributes:
        total_count (int | Unset): Gets or sets the total count of volunteer types
        types (list[VolunteerType] | None | Unset): Gets or sets the collection of volunteer types
    """

    total_count: int | Unset = UNSET
    types: list[VolunteerType] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        types: list[dict[str, Any]] | None | Unset
        if isinstance(self.types, Unset):
            types = UNSET
        elif isinstance(self.types, list):
            types = []
            for types_type_0_item_data in self.types:
                types_type_0_item = types_type_0_item_data.to_dict()
                types.append(types_type_0_item)

        else:
            types = self.types

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if types is not UNSET:
            field_dict["types"] = types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.volunteer_type import VolunteerType

        d = dict(src_dict)
        total_count = d.pop("total_count", UNSET)

        def _parse_types(data: object) -> list[VolunteerType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                types_type_0 = []
                _types_type_0 = data
                for types_type_0_item_data in _types_type_0:
                    types_type_0_item = VolunteerType.from_dict(types_type_0_item_data)

                    types_type_0.append(types_type_0_item)

                return types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VolunteerType] | None | Unset, data)

        types = _parse_types(d.pop("types", UNSET))

        get_volunteer_types_response = cls(
            total_count=total_count,
            types=types,
        )

        return get_volunteer_types_response
