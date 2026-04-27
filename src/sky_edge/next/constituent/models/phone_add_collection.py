from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.phone_add_collection_phone import PhoneAddCollectionPhone


T = TypeVar("T", bound="PhoneAddCollection")


@_attrs_define
class PhoneAddCollection:
    """Phones store information about constituent phone numbers and where to call individuals and organizations.

    Attributes:
        constituent_id (str): The immutable system record ID of the constituent associated with the phone.
        phones (list[PhoneAddCollectionPhone]): Collection of phones to add
    """

    constituent_id: str
    phones: list[PhoneAddCollectionPhone]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        constituent_id = self.constituent_id

        phones = []
        for phones_item_data in self.phones:
            phones_item = phones_item_data.to_dict()
            phones.append(phones_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "constituent_id": constituent_id,
                "phones": phones,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.phone_add_collection_phone import PhoneAddCollectionPhone

        d = dict(src_dict)
        constituent_id = d.pop("constituent_id")

        phones = []
        _phones = d.pop("phones")
        for phones_item_data in _phones:
            phones_item = PhoneAddCollectionPhone.from_dict(phones_item_data)

            phones.append(phones_item)

        phone_add_collection = cls(
            constituent_id=constituent_id,
            phones=phones,
        )

        phone_add_collection.additional_properties = d
        return phone_add_collection

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
