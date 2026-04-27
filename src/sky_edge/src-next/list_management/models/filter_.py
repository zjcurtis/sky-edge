from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.filter_first_day_of_week_type import FilterFirstDayOfWeekType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_item import FilterItem
    from ..models.selected_filter import SelectedFilter


T = TypeVar("T", bound="Filter")


@_attrs_define
class Filter:
    """Filter information for a query or report execution

    Attributes:
        filter_items (list[FilterItem] | None | Unset): The set of filter items in the filter
        selected_filters (list[SelectedFilter] | None | Unset): The set of selected filter items in the filter
        time_zone_offset_in_minutes (int | None | Unset): Gets or sets the time zone offset to support dynamic date
            filtering
        first_day_of_week (FilterFirstDayOfWeekType | Unset): Gets or sets the first day of week when using certain date
            filters.
    """

    filter_items: list[FilterItem] | None | Unset = UNSET
    selected_filters: list[SelectedFilter] | None | Unset = UNSET
    time_zone_offset_in_minutes: int | None | Unset = UNSET
    first_day_of_week: FilterFirstDayOfWeekType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        filter_items: list[dict[str, Any]] | None | Unset
        if isinstance(self.filter_items, Unset):
            filter_items = UNSET
        elif isinstance(self.filter_items, list):
            filter_items = []
            for filter_items_type_0_item_data in self.filter_items:
                filter_items_type_0_item = filter_items_type_0_item_data.to_dict()
                filter_items.append(filter_items_type_0_item)

        else:
            filter_items = self.filter_items

        selected_filters: list[dict[str, Any]] | None | Unset
        if isinstance(self.selected_filters, Unset):
            selected_filters = UNSET
        elif isinstance(self.selected_filters, list):
            selected_filters = []
            for selected_filters_type_0_item_data in self.selected_filters:
                selected_filters_type_0_item = selected_filters_type_0_item_data.to_dict()
                selected_filters.append(selected_filters_type_0_item)

        else:
            selected_filters = self.selected_filters

        time_zone_offset_in_minutes: int | None | Unset
        if isinstance(self.time_zone_offset_in_minutes, Unset):
            time_zone_offset_in_minutes = UNSET
        else:
            time_zone_offset_in_minutes = self.time_zone_offset_in_minutes

        first_day_of_week: str | Unset = UNSET
        if not isinstance(self.first_day_of_week, Unset):
            first_day_of_week = self.first_day_of_week.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if filter_items is not UNSET:
            field_dict["filter_items"] = filter_items
        if selected_filters is not UNSET:
            field_dict["selected_filters"] = selected_filters
        if time_zone_offset_in_minutes is not UNSET:
            field_dict["time_zone_offset_in_minutes"] = time_zone_offset_in_minutes
        if first_day_of_week is not UNSET:
            field_dict["first_day_of_week"] = first_day_of_week

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_item import FilterItem
        from ..models.selected_filter import SelectedFilter

        d = dict(src_dict)

        def _parse_filter_items(data: object) -> list[FilterItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filter_items_type_0 = []
                _filter_items_type_0 = data
                for filter_items_type_0_item_data in _filter_items_type_0:
                    filter_items_type_0_item = FilterItem.from_dict(filter_items_type_0_item_data)

                    filter_items_type_0.append(filter_items_type_0_item)

                return filter_items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FilterItem] | None | Unset, data)

        filter_items = _parse_filter_items(d.pop("filter_items", UNSET))

        def _parse_selected_filters(data: object) -> list[SelectedFilter] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                selected_filters_type_0 = []
                _selected_filters_type_0 = data
                for selected_filters_type_0_item_data in _selected_filters_type_0:
                    selected_filters_type_0_item = SelectedFilter.from_dict(selected_filters_type_0_item_data)

                    selected_filters_type_0.append(selected_filters_type_0_item)

                return selected_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SelectedFilter] | None | Unset, data)

        selected_filters = _parse_selected_filters(d.pop("selected_filters", UNSET))

        def _parse_time_zone_offset_in_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_zone_offset_in_minutes = _parse_time_zone_offset_in_minutes(d.pop("time_zone_offset_in_minutes", UNSET))

        _first_day_of_week = d.pop("first_day_of_week", UNSET)
        first_day_of_week: FilterFirstDayOfWeekType | Unset
        if isinstance(_first_day_of_week, Unset):
            first_day_of_week = UNSET
        else:
            first_day_of_week = FilterFirstDayOfWeekType(_first_day_of_week)

        filter_ = cls(
            filter_items=filter_items,
            selected_filters=selected_filters,
            time_zone_offset_in_minutes=time_zone_offset_in_minutes,
            first_day_of_week=first_day_of_week,
        )

        return filter_
