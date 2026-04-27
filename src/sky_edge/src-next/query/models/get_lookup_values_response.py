from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lookup_value import LookupValue


T = TypeVar("T", bound="GetLookupValuesResponse")


@_attrs_define
class GetLookupValuesResponse:
    """Get a set of lookup values

    Attributes:
        limit (int): The number of values returned based on the limit
        offset (int): The offset
        lookup_values (list[LookupValue] | None | Unset): The set of values for a lookup field
        count (int | Unset): The total number of values available for the lookup field
    """

    limit: int
    offset: int
    lookup_values: list[LookupValue] | None | Unset = UNSET
    count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        offset = self.offset

        lookup_values: list[dict[str, Any]] | None | Unset
        if isinstance(self.lookup_values, Unset):
            lookup_values = UNSET
        elif isinstance(self.lookup_values, list):
            lookup_values = []
            for lookup_values_type_0_item_data in self.lookup_values:
                lookup_values_type_0_item = lookup_values_type_0_item_data.to_dict()
                lookup_values.append(lookup_values_type_0_item)

        else:
            lookup_values = self.lookup_values

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "limit": limit,
                "offset": offset,
            }
        )
        if lookup_values is not UNSET:
            field_dict["lookup_values"] = lookup_values
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lookup_value import LookupValue

        d = dict(src_dict)
        limit = d.pop("limit")

        offset = d.pop("offset")

        def _parse_lookup_values(data: object) -> list[LookupValue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                lookup_values_type_0 = []
                _lookup_values_type_0 = data
                for lookup_values_type_0_item_data in _lookup_values_type_0:
                    lookup_values_type_0_item = LookupValue.from_dict(lookup_values_type_0_item_data)

                    lookup_values_type_0.append(lookup_values_type_0_item)

                return lookup_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LookupValue] | None | Unset, data)

        lookup_values = _parse_lookup_values(d.pop("lookup_values", UNSET))

        count = d.pop("count", UNSET)

        get_lookup_values_response = cls(
            limit=limit,
            offset=offset,
            lookup_values=lookup_values,
            count=count,
        )

        return get_lookup_values_response
