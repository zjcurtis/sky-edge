from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_field_read import FilterFieldRead


T = TypeVar("T", bound="GetSummaryFieldDefaultFiltersResponse")


@_attrs_define
class GetSummaryFieldDefaultFiltersResponse:
    """Response model for GetSummaryFieldDefaultFilters

    Attributes:
        default_filters (list[FilterFieldRead] | None | Unset): The required filters to apply for the summary field with
            default values
    """

    default_filters: list[FilterFieldRead] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        default_filters: list[dict[str, Any]] | None | Unset
        if isinstance(self.default_filters, Unset):
            default_filters = UNSET
        elif isinstance(self.default_filters, list):
            default_filters = []
            for default_filters_type_0_item_data in self.default_filters:
                default_filters_type_0_item = default_filters_type_0_item_data.to_dict()
                default_filters.append(default_filters_type_0_item)

        else:
            default_filters = self.default_filters

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if default_filters is not UNSET:
            field_dict["default_filters"] = default_filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_field_read import FilterFieldRead

        d = dict(src_dict)

        def _parse_default_filters(
            data: object,
        ) -> list[FilterFieldRead] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                default_filters_type_0 = []
                _default_filters_type_0 = data
                for default_filters_type_0_item_data in _default_filters_type_0:
                    default_filters_type_0_item = FilterFieldRead.from_dict(
                        default_filters_type_0_item_data
                    )

                    default_filters_type_0.append(default_filters_type_0_item)

                return default_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FilterFieldRead] | None | Unset, data)

        default_filters = _parse_default_filters(d.pop("default_filters", UNSET))

        get_summary_field_default_filters_response = cls(
            default_filters=default_filters,
        )

        return get_summary_field_default_filters_response
