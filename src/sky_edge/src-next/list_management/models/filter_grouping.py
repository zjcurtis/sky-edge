from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.filter_grouping_filter_grouping_operator import FilterGroupingFilterGroupingOperator
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_item import FilterItem


T = TypeVar("T", bound="FilterGrouping")


@_attrs_define
class FilterGrouping:
    """Represents a group of filter items and how they relate

    Attributes:
        grouping_id (None | str | Unset): The identifier of the grouping the filter applies to
        items (list[FilterItem] | None | Unset): The set of filter items in the grouping
        operator (FilterGroupingFilterGroupingOperator | Unset): The operator for how the items in the group relate
    """

    grouping_id: None | str | Unset = UNSET
    items: list[FilterItem] | None | Unset = UNSET
    operator: FilterGroupingFilterGroupingOperator | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        grouping_id: None | str | Unset
        if isinstance(self.grouping_id, Unset):
            grouping_id = UNSET
        else:
            grouping_id = self.grouping_id

        items: list[dict[str, Any]] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)

        else:
            items = self.items

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if grouping_id is not UNSET:
            field_dict["grouping_id"] = grouping_id
        if items is not UNSET:
            field_dict["items"] = items
        if operator is not UNSET:
            field_dict["operator"] = operator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_item import FilterItem

        d = dict(src_dict)

        def _parse_grouping_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grouping_id = _parse_grouping_id(d.pop("grouping_id", UNSET))

        def _parse_items(data: object) -> list[FilterItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in _items_type_0:
                    items_type_0_item = FilterItem.from_dict(items_type_0_item_data)

                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FilterItem] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))

        _operator = d.pop("operator", UNSET)
        operator: FilterGroupingFilterGroupingOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = FilterGroupingFilterGroupingOperator(_operator)

        filter_grouping = cls(
            grouping_id=grouping_id,
            items=items,
            operator=operator,
        )

        return filter_grouping
