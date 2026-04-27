from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_field import FilterField


T = TypeVar("T", bound="CollectionFilterField")


@_attrs_define
class CollectionFilterField:
    """Represents filter information for a collection.  This is used for filtering to records that have a single item in a
    collection that match a set of filters.

        Attributes:
            field_id (None | str | Unset): The identifier of the field the filter applies to
            filter_fields (list[FilterField] | None | Unset): The set of filters to be applied to items in the collection.
                An indidivudal item must meet the entire set of filter criteria.
    """

    field_id: None | str | Unset = UNSET
    filter_fields: list[FilterField] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        field_id: None | str | Unset
        if isinstance(self.field_id, Unset):
            field_id = UNSET
        else:
            field_id = self.field_id

        filter_fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.filter_fields, Unset):
            filter_fields = UNSET
        elif isinstance(self.filter_fields, list):
            filter_fields = []
            for filter_fields_type_0_item_data in self.filter_fields:
                filter_fields_type_0_item = filter_fields_type_0_item_data.to_dict()
                filter_fields.append(filter_fields_type_0_item)

        else:
            filter_fields = self.filter_fields

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if field_id is not UNSET:
            field_dict["field_id"] = field_id
        if filter_fields is not UNSET:
            field_dict["filter_fields"] = filter_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_field import FilterField

        d = dict(src_dict)

        def _parse_field_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_id = _parse_field_id(d.pop("field_id", UNSET))

        def _parse_filter_fields(data: object) -> list[FilterField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filter_fields_type_0 = []
                _filter_fields_type_0 = data
                for filter_fields_type_0_item_data in _filter_fields_type_0:
                    filter_fields_type_0_item = FilterField.from_dict(
                        filter_fields_type_0_item_data
                    )

                    filter_fields_type_0.append(filter_fields_type_0_item)

                return filter_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FilterField] | None | Unset, data)

        filter_fields = _parse_filter_fields(d.pop("filter_fields", UNSET))

        collection_filter_field = cls(
            field_id=field_id,
            filter_fields=filter_fields,
        )

        return collection_filter_field
