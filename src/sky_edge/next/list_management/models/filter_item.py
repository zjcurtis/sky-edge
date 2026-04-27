from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection_filter_field import CollectionFilterField
    from ..models.filter_field import FilterField
    from ..models.filter_grouping import FilterGrouping


T = TypeVar("T", bound="FilterItem")


@_attrs_define
class FilterItem:
    """Represents an individual item in a group of filter items.  This item can contain filter information for a specific
    field or contain another group of filter items.  It cannot contain both.

        Attributes:
            field (FilterField | Unset): Represents filter information for a specific field
            grouping (FilterGrouping | Unset): Represents a group of filter items and how they relate
            collection_field (CollectionFilterField | Unset): Represents filter information for a collection.  This is used
                for filtering to records that have a single item in a collection that match a set of filters.
    """

    field: FilterField | Unset = UNSET
    grouping: FilterGrouping | Unset = UNSET
    collection_field: CollectionFilterField | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        field: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field, Unset):
            field = self.field.to_dict()

        grouping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.grouping, Unset):
            grouping = self.grouping.to_dict()

        collection_field: dict[str, Any] | Unset = UNSET
        if not isinstance(self.collection_field, Unset):
            collection_field = self.collection_field.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if grouping is not UNSET:
            field_dict["grouping"] = grouping
        if collection_field is not UNSET:
            field_dict["collection_field"] = collection_field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collection_filter_field import CollectionFilterField
        from ..models.filter_field import FilterField
        from ..models.filter_grouping import FilterGrouping

        d = dict(src_dict)
        _field = d.pop("field", UNSET)
        field: FilterField | Unset
        if isinstance(_field, Unset):
            field = UNSET
        else:
            field = FilterField.from_dict(_field)

        _grouping = d.pop("grouping", UNSET)
        grouping: FilterGrouping | Unset
        if isinstance(_grouping, Unset):
            grouping = UNSET
        else:
            grouping = FilterGrouping.from_dict(_grouping)

        _collection_field = d.pop("collection_field", UNSET)
        collection_field: CollectionFilterField | Unset
        if isinstance(_collection_field, Unset):
            collection_field = UNSET
        else:
            collection_field = CollectionFilterField.from_dict(_collection_field)

        filter_item = cls(
            field=field,
            grouping=grouping,
            collection_field=collection_field,
        )

        return filter_item
