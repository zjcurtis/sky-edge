from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sort_field import SortField


T = TypeVar("T", bound="Sort")


@_attrs_define
class Sort:
    """Describes how to sort a list request
    ///

        Attributes:
            sort_fields (list[SortField] | None | Unset): Gets or sets the sort fields for a list request
    """

    sort_fields: list[SortField] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        sort_fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.sort_fields, Unset):
            sort_fields = UNSET
        elif isinstance(self.sort_fields, list):
            sort_fields = []
            for sort_fields_type_0_item_data in self.sort_fields:
                sort_fields_type_0_item = sort_fields_type_0_item_data.to_dict()
                sort_fields.append(sort_fields_type_0_item)

        else:
            sort_fields = self.sort_fields

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sort_fields is not UNSET:
            field_dict["sort_fields"] = sort_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sort_field import SortField

        d = dict(src_dict)

        def _parse_sort_fields(data: object) -> list[SortField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sort_fields_type_0 = []
                _sort_fields_type_0 = data
                for sort_fields_type_0_item_data in _sort_fields_type_0:
                    sort_fields_type_0_item = SortField.from_dict(
                        sort_fields_type_0_item_data
                    )

                    sort_fields_type_0.append(sort_fields_type_0_item)

                return sort_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SortField] | None | Unset, data)

        sort_fields = _parse_sort_fields(d.pop("sort_fields", UNSET))

        sort = cls(
            sort_fields=sort_fields,
        )

        return sort
