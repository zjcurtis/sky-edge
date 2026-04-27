from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_read_extended import AddressReadExtended


T = TypeVar("T", bound="ApiCollectionOfAddressReadExtended")


@_attrs_define
class ApiCollectionOfAddressReadExtended:
    """Fetching data all at once quickly becomes unmanageable. The collection entity helps by returning paginated chunks of
    large data sets. This entity includes helpful metadata and properties to paginate and iterate through the data.

        Attributes:
            count (int | Unset): The number of items available for retrieval into the collection after applying any request
                parameters. The <b>limit</b> and <b>offset</b> parameters do not affect the <b>count</b>, but to facilitate
                paging, they may affect the number of items in the <b>value</b> result set.
            next_link (str | Unset): For paginated responses, the URI for the next page of results.
            value (list[AddressReadExtended] | Unset): The set of items included in the response. This may be a subset of
                the items in the collection.
    """

    count: int | Unset = UNSET
    next_link: str | Unset = UNSET
    value: list[AddressReadExtended] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        next_link = self.next_link

        value: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = []
            for value_item_data in self.value:
                value_item = value_item_data.to_dict()
                value.append(value_item)

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
        from ..models.address_read_extended import AddressReadExtended

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        next_link = d.pop("next_link", UNSET)

        _value = d.pop("value", UNSET)
        value: list[AddressReadExtended] | Unset = UNSET
        if _value is not UNSET:
            value = []
            for value_item_data in _value:
                value_item = AddressReadExtended.from_dict(value_item_data)

                value.append(value_item)

        api_collection_of_address_read_extended = cls(
            count=count,
            next_link=next_link,
            value=value,
        )

        api_collection_of_address_read_extended.additional_properties = d
        return api_collection_of_address_read_extended

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
