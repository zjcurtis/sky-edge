from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="ApiCollectionString")


@_attrs_define
class ApiCollectionString:
    """Fetching data all at once quickly becomes unmanageable. The collection entity helps by returning paginated chunks of
    large data sets. This entity includes helpful metadata and properties to paginate and iterate through the data.

        Attributes:
            count (int | Unset): The number of items available for retrieval into the collection after applying any request
                parameters. The <b>limit</b> and <b>offset</b> parameters do not affect the <b>count</b>, but to facilitate
                paging, they may affect the number of items in the <b>value</b> result set.
            next_link (str | Unset): For paginated responses, the URI for the next page of results.
            value (list[str] | Unset): The set of items included in the response. This may be a subset of the items in the
                collection.
    """

    count: int | Unset = UNSET
    next_link: str | Unset = UNSET
    value: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        next_link = self.next_link

        value: list[str] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if next_link is not UNSET:
            field_dict["next_link"] = next_link
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        next_link = d.pop("next_link", UNSET)

        value = cast(list[str], d.pop("value", UNSET))

        api_collection_string = cls(
            count=count,
            next_link=next_link,
            value=value,
        )

        api_collection_string.additional_properties = d
        return api_collection_string

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
