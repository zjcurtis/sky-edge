from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AppendIdsToListRequest")


@_attrs_define
class AppendIdsToListRequest:
    """Represents request to create a list filtered to a set of unique record identifiers

    Attributes:
        list_id (str): The immutable system record ID for the list
        ids (list[str]): The unique identifiers for the records to be added to the list. Limited to a maximumum 100,000
            identifiers.
    """

    list_id: str
    ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        list_id = self.list_id

        ids = self.ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "list_id": list_id,
                "ids": ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        list_id = d.pop("list_id")

        ids = cast(list[str], d.pop("ids"))

        append_ids_to_list_request = cls(
            list_id=list_id,
            ids=ids,
        )

        append_ids_to_list_request.additional_properties = d
        return append_ids_to_list_request

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
